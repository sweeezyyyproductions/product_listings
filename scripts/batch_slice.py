"""Batch-slice Cody's Bambu .3mf projects into sliced .gcode.3mf files, one per plate.

Usage:
    python batch_slice.py                      # slice everything under Sprout Designs
    python batch_slice.py "Festivals\\Boo Seattle"   # slice one subfolder only

- Originals are never modified; sliced files go to this folder, mirroring the source subfolders.
- Each plate is sliced on its own (empty plates are skipped; slicing "all plates" fails on them).
- Already-sliced plates are skipped, so the script can be stopped and re-run safely.
- Every plate gets a row in _slice_log.csv (ok / skipped / empty / FAILED + reason).
"""
import csv, json, os, re, subprocess, sys, tempfile, time, zipfile

BAMBU = r"C:\Program Files\Bambu Studio\bambu-studio.exe"
SRC = os.path.join("G:" + os.sep, "Other computers", "My Mac", "The_Beat_Drop", "Sprout Designs")
# Fixed output folder, so the repo copy of this script never writes sliced files into the repo.
OUT = os.path.join("C:" + os.sep, "Users", "DATA A", "Desktop", "Sliced Exports")
LOG = os.path.join(OUT, "_slice_log.csv")
TIMEOUT = 900  # seconds per plate


def plates(path):
    """Return {plate_number: object_count} from the project's model_settings.config."""
    z = zipfile.ZipFile(path)
    if "Metadata/model_settings.config" not in z.namelist():
        return {}
    cfg = z.read("Metadata/model_settings.config").decode("utf-8", "ignore")
    res = {}
    for block in re.findall(r"<plate>(.*?)</plate>", cfg, re.S):
        m = re.search(r'key="plater_id" value="(\d+)"', block)  # first match = the plate's own id
        if m:
            res[int(m.group(1))] = len(re.findall(r"<model_instance>", block))
    return res


def main():
    sub = sys.argv[1] if len(sys.argv) > 1 else ""
    root = os.path.join(SRC, sub)
    new_log = not os.path.exists(LOG)
    log = open(LOG, "a", newline="", encoding="utf-8")
    w = csv.writer(log)
    if new_log:
        w.writerow(["time", "status", "source file", "plate", "objects", "output", "note"])
    files = []
    for dp, dn, fn in os.walk(root):
        dn[:] = [d for d in dn if not re.search(r"inspo", d, re.I)]
        files += [os.path.join(dp, f) for f in fn if f.lower().endswith(".3mf") and not f.lower().endswith(".gcode.3mf")]
    print(f"{len(files)} project files under {root}")
    done = 0
    for i, f in enumerate(sorted(files), 1):
        rel = os.path.relpath(f, SRC)
        dest = os.path.join(OUT, os.path.dirname(rel))
        os.makedirs(dest, exist_ok=True)
        base = os.path.splitext(os.path.basename(f))[0].strip()
        try:
            pl = plates(f)
        except Exception as e:
            w.writerow([time.strftime("%H:%M:%S"), "FAILED", rel, "", "", "", f"can't read file: {e}"]); continue
        if not pl:
            w.writerow([time.strftime("%H:%M:%S"), "FAILED", rel, "", "", "", "no plate info (not a Bambu project?)"]); continue
        for n, objs in sorted(pl.items()):
            name = f"{base}_plate_{n}.gcode.3mf"
            if objs == 0:
                w.writerow([time.strftime("%H:%M:%S"), "empty", rel, n, 0, "", "plate has no objects"]); continue
            if os.path.exists(os.path.join(dest, name)):
                w.writerow([time.strftime("%H:%M:%S"), "skipped", rel, n, objs, name, "already sliced"]); continue
            with tempfile.TemporaryDirectory() as tmp:
                try:
                    subprocess.run([BAMBU, "--slice", str(n), "--outputdir", tmp, "--export-3mf", name, f],
                                   timeout=TIMEOUT, capture_output=True)
                    note = ""
                    rj = os.path.join(tmp, "result.json")
                    if os.path.exists(rj):
                        note = json.load(open(rj, encoding="utf-8")).get("error_string", "")
                    if os.path.exists(os.path.join(tmp, name)):
                        os.replace(os.path.join(tmp, name), os.path.join(dest, name))
                        w.writerow([time.strftime("%H:%M:%S"), "ok", rel, n, objs, name, ""]); done += 1
                    else:
                        w.writerow([time.strftime("%H:%M:%S"), "FAILED", rel, n, objs, "", note or "no output"])
                except subprocess.TimeoutExpired:
                    w.writerow([time.strftime("%H:%M:%S"), "FAILED", rel, n, objs, "", f"timed out after {TIMEOUT}s"])
            log.flush()
        print(f"[{i}/{len(files)}] {rel}")
    log.close()
    print(f"done: {done} plates sliced. Log: {LOG}")


if __name__ == "__main__":
    main()
