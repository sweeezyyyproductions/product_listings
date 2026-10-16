"""Build a 3DPrintForce bulk-model-upload CSV from sliced Bambu files (.gcode.3mf).

Usage:
    python make_3dpf_csv.py "Festivals\\Boo Seattle" --prefix "BOO Seattle" --code BSBD1 --category "Kandi Charms"

Reads every *_plate_N.gcode.3mf under Desktop\\Sliced Exports\\<folder> (made by batch_slice.py) and writes:
  - 3DPrintForce_<prefix>.csv          one row per model, in the bulk-model-upload-template.csv columns
  - 3DPrintForce_<prefix>_plates.csv   every plate with plate totals, for checking

Rules:
  - A production plate (>= --min-qty objects) is one model row; its colorway comes from the filaments it uses.
  - A design with no production plate gets one row from its first single-piece plate.
  - Time and grams are PER PIECE (plate total / objects on the plate). Plate totals are in the _plates file.
  - Prep and post-process minutes are left blank unless --prep / --post are given.
"""
import argparse, csv, json, os, re, zipfile
from collections import defaultdict

OUT_ROOT = os.path.join("C:" + os.sep, "Users", "DATA A", "Desktop", "Sliced Exports")
PRINTERS = {"C12": "Bambu Lab P1S", "C11": "Bambu Lab P1P", "BL-P001": "Bambu Lab X1 Carbon", "N2S": "Bambu Lab A1"}

# Named colors -> (display name, 4-letter SKU code). Matched by nearest RGB.
COLORS = [
    ("#FFFFFF", "White", "WHIT"), ("#000000", "Black", "BLCK"), ("#C12E1F", "Red", "REDD"), ("#FF0000", "Red", "REDD"),
    ("#FF6A13", "Orange", "ORGN"), ("#F97908", "Orange", "ORGN"), ("#B6FF43", "Neon Green", "NGRN"), ("#66FF00", "Neon Green", "NGRN"),
    ("#00AE42", "Green", "GREN"), ("#5E43B7", "Purple", "PRPL"), ("#8B00FF", "Violet", "VILT"), ("#D1D3D5", "Light Gray", "LTGR"),
    ("#C0C0C0", "Silver", "SLVR"), ("#FDF100", "Yellow", "YELW"), ("#F6DF00", "Yellow", "YELW"), ("#0A2CA5", "Blue", "BLUE"),
    ("#40B4FF", "Light Blue", "LTBL"), ("#00FFFF", "Cyan", "CYAN"), ("#FB00E2", "Pink", "PINK"), ("#F55A74", "Pink", "PINK"),
    ("#9F6E25", "Brown", "BRWN"), ("#6F5034", "Brown", "BRWN"), ("#161616", "Black", "BLCK"), ("#002364", "Navy", "NAVY"),
]


def color_name(hexcode):
    h = hexcode.lstrip("#")[:6]
    r, g, b = (int(h[i:i + 2], 16) for i in (0, 2, 4))
    best = min(COLORS, key=lambda c: sum((int(c[0][i:i + 2], 16) - v) ** 2 for i, v in zip((1, 3, 5), (r, g, b))))
    return best[1], best[2]


def filament_label(setting_id, hexcode):
    """'Bambu PLA Basic @BBL P1S 0.4 nozzle' -> 'Bambu Lab, PLA Basic, White' (template format: Brand, Material, Color)."""
    s = re.sub(r"\s*@.*$", "", setting_id or "").strip()
    color = color_name(hexcode)[0]
    if s.startswith("Bambu "):
        return f"Bambu Lab, {s[6:]}, {color}"
    if s.upper().startswith("SUNLU "):
        return f"SUNLU, {s[6:]}, {color}"
    if s.lower().startswith("generic "):
        return f"Generic, {s[8:]}, {color}"
    if "silk" in s.lower():
        # "NEW SILK SETTINGS" is Cody's custom silk profile (confirmed 2026-10-16).
        return f"Custom, PLA Silk, {color}"
    return f"Unknown, {s or 'PLA'}, {color}"


def design_name(fname, prefix):
    n = re.sub(r"_plate_\d+\.gcode\.3mf$", "", fname)
    n = re.sub(r"^(SM_)?V\d+\s*", "", n)
    n = re.sub(r"^" + re.escape(prefix) + r"\s*-\s*", "", n, flags=re.I)
    return re.sub(r"[_\s]+", " ", n).strip(" -")


def read_plate(path):
    z = zipfile.ZipFile(path)
    si = z.read("Metadata/slice_info.config").decode("utf-8", "ignore")
    ps = json.loads(z.read("Metadata/project_settings.config"))
    ids = ps.get("filament_settings_id", [])
    fil = []
    for m in re.finditer(r"<filament ([^>]*)/>", si):
        a = dict(re.findall(r'(\w+)="([^"]*)"', m.group(1)))
        if float(a.get("used_g", 0)) > 0:
            i = int(a["id"]) - 1
            fil.append({"id": i + 1, "hex": a["color"], "g": float(a["used_g"]),
                        "label": filament_label(ids[i] if i < len(ids) else "", a["color"])})
    model_id = re.search(r'key="printer_model_id" value="([^"]+)"', si)
    return {"qty": len(re.findall(r"<object ", si)),
            "sec": int(re.search(r'key="prediction" value="(\d+)"', si).group(1)),
            "g": float(re.search(r'key="weight" value="([\d.]+)"', si).group(1)),
            "printer": PRINTERS.get(model_id.group(1) if model_id else "", ps.get("printer_model", "")),
            "fil": sorted(fil, key=lambda f: -f["g"])}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("folder"); ap.add_argument("--prefix", required=True); ap.add_argument("--code", default="")
    ap.add_argument("--category", default="Kandi Charms"); ap.add_argument("--min-qty", type=int, default=20)
    ap.add_argument("--prep", default=""); ap.add_argument("--post", default="")
    ap.add_argument("--alias", action="append", default=[],
                    help='rename a design, optionally under another event: "file design=New Name" or "file design=New Name@Prefix:CODE"')
    a = ap.parse_args()
    alias = {}
    for s in a.alias:
        old, new = s.split("=", 1)
        name, _, where = new.partition("@")
        pre, _, code = where.partition(":")
        alias[old.strip().lower()] = (name.strip(), pre.strip() or a.prefix, code.strip() if where else a.code)
    src = os.path.join(OUT_ROOT, a.folder)
    plates = defaultdict(list)
    for dp, dn, fn in os.walk(src):
        for f in fn:
            if f.endswith(".gcode.3mf"):
                n = int(re.search(r"_plate_(\d+)\.gcode\.3mf$", f).group(1))
                plates[design_name(f, a.prefix)].append((n, f, read_plate(os.path.join(dp, f))))

    rows, detail, max_sub = [], [], 1
    for design in sorted(plates):
        ps = sorted(plates[design])
        for n, f, p in ps:
            detail.append([design, n, p["qty"], round(p["sec"] / 60, 1), p["g"], p["printer"],
                           "; ".join(f"{x['label']} {x['g']}g" for x in p["fil"]), f])
        prod = [x for x in ps if x[2]["qty"] >= a.min_qty] or [next((x for x in ps if x[2]["qty"] == 1), ps[0])]
        shown, prefix, pcode = alias.get(design.lower(), (design, a.prefix, a.code))
        for n, f, p in prod:
            names = [color_name(x["hex"]) for x in p["fil"]]
            colorway = "/".join(dict.fromkeys(c[0] for c in names))
            code = "".join(dict.fromkeys(c[1] for c in names[:1]))
            dcode = re.sub(r"[^A-Z]", "", shown.upper().replace(" ", ""))[:4]
            per_min = round(p["sec"] / p["qty"] / 60)
            subs = [(round(x["g"] / p["qty"], 2), x["label"]) for x in p["fil"]]
            max_sub = max(max_sub, len(subs))
            rows.append({"name": f"{prefix} - {shown} - {colorway}",
                         "sku": "_".join(x for x in (pcode, dcode, code) if x),
                         "h": per_min // 60, "m": per_min % 60, "printer": p["printer"], "part": shown, "subs": subs})

    header = ["Model Name", "SKU", "Category", "Print Hours", "Print Minutes", "Printer Model",
              "Print Prep Time (Minutes)", "Post Process Time (Minutes)", "Part 1"]
    for i in range(1, max_sub + 1):
        header += [f"Part 1 SubPart {i} Grams", f"Part 1 SubPart {i} Filament"]
    base = re.sub(r"[^\w]+", "_", a.prefix).strip("_")
    out = os.path.join(OUT_ROOT, f"3DPrintForce_{base}.csv")
    with open(out, "w", newline="", encoding="utf-8") as fh:
        w = csv.writer(fh); w.writerow(header)
        for r in rows:
            line = [r["name"], r["sku"], a.category, r["h"], r["m"], r["printer"], a.prep, a.post, r["part"]]
            for g, lab in r["subs"]:
                line += [g, lab]
            w.writerow(line + [""] * (len(header) - len(line)))
    out2 = os.path.join(OUT_ROOT, f"3DPrintForce_{base}_plates.csv")
    with open(out2, "w", newline="", encoding="utf-8") as fh:
        w = csv.writer(fh)
        w.writerow(["Design", "Plate", "Objects", "Plate minutes", "Plate grams", "Printer", "Filaments (plate totals)", "Sliced file"])
        w.writerows(detail)
    print(f"{len(rows)} model rows -> {out}\n{len(detail)} plates -> {out2}")


if __name__ == "__main__":
    main()
