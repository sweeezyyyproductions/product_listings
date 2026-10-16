"""Build ONE 3DPrintForce bulk-upload CSV for every sliced folder under Desktop\\Sliced Exports.

Usage:
    python make_3dpf_all.py

Writes to Desktop\\Sliced Exports:
  - 3DPrintForce_ALL.csv          bulk-model-upload-template.csv columns, one row per model (design + colorway)
  - 3DPrintForce_ALL_plates.csv   every sliced plate with plate totals (for checking)
  - 3DPrintForce_ALL_codes.csv    folder -> code family used in the SKUs (existing vs proposed, for review)

Same rules as make_3dpf_csv.py: a plate with >= 20 objects is one model (one colorway); a design with no
such plate uses its fullest plate. Time and grams are per piece. Only the highest V# of each design is used
(V3 > V2 > V1), per Cody: older versions are superseded, and non-stock plates are coloring/preview plates.
"""
import csv, os, re, sys
from collections import defaultdict

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from make_3dpf_csv import OUT_ROOT, read_plate, color_name  # noqa: E402

MIN_QTY = 20

# Code families already used in Shopify SKUs (checked 2026-10-14). Anything else gets a proposed code.
FAMILY = {
    "Ahee": "AHE", "Boogie T": "BGT", "Daily Bread": "DBS", "Deadmau5": "DM5", "Delta Heavy": "DLHV",
    "Dennett": "DENT", "Excision": "EXC", "FISHER": "FSHR", "Ganja White Night": "GWNT", "Heyz": "HEYZ",
    "John Summit": "JSM", "Kai Wachi": "KAWA", "Kaskade": "KSKD", "LSDREAM": "LSDR", "Levity": "LVTY",
    "Liquid Stranger": "LQS", "Lost Lands": "LLSS", "Maddy O'Neal": "MDON", "Mersiv": "MRSV",
    "Pretty Lights": "PLML", "Pretty Lights (1)": "PLML", "RavenScoon": "RVSC", "SUBTRONICS": "SUB",
    "Sullivan King": "SLKG", "Svdden Death": "SDV", "Voyd": "SDV", "Wooli": "WOLI", "Zedd": "ZEDD",
    "Apocalypse": "ZAMF", "Boo Seattle": "BSBD1", "Camp Alderwild": "CABD1", "EDC": "EDC",
    "Electric Forest": "EFL", "EmberShores": "EMBD1", "Escape Physco Circus": "EHBD1", "Force Fields": "FFBD1",
    "Hulaween": "HLWN", "Northcoast": "NCMF", "Secret Dreams": "SDBD1", "Seven Stars": "SSMF",
    "Wakaan": "WKN", "WobbleWeen": "GWNT", "WobbleWeen (1)": "GWNT", "Yahn Dawn": "PLYD", "Labubu": "LBBU",
}
# Display names for folders whose names are odd.
PREFIX = {"Escape Physco Circus": "Escape Halloween", "EmberShores": "Ember Shores", "DEcadence": "Decadence",
          "Northcoast": "North Coast", "SUBTRONICS": "Subtronics", "LSDREAM": "LSDream", "FISHER": "Fisher",
          "Pretty Lights (1)": "Pretty Lights", "WobbleWeen (1)": "WobbleWeen", "RavenScoon": "Ravenscoon"}
CATEGORY = {"ARTISTS": "Artist Charms", "Festivals": "Festival Charms", "Generic": "Generic", "B2B": "B2B"}


def proposed(name):
    w = re.sub(r"[^A-Z]", "", name.upper())
    return (w[0] + re.sub(r"[AEIOU]", "", w[1:]))[:4] if w else "MISC"


def design_of(fname, owner):
    n = re.sub(r"_plate_\d+\.gcode\.3mf$", "", fname)
    n = re.sub(r"^\(TP\)\s*", "", n)
    n = re.sub(r"^(SM_)?V\d+\s*[-_]?\s*", "", n)
    for p in {owner, PREFIX.get(owner, owner)}:
        n = re.sub(r"^" + re.escape(p) + r"\s*[-_]\s*", "", n, flags=re.I)
    n = re.sub(r"[_\s]+", " ", n).strip(" -.")
    return n or owner


def main():
    groups = defaultdict(lambda: defaultdict(list))  # (category, owner) -> design -> [(file, plate)]
    for dp, dn, fn in os.walk(OUT_ROOT):
        for f in fn:
            if not f.endswith(".gcode.3mf"):
                continue
            rel = os.path.relpath(dp, OUT_ROOT).split(os.sep)
            cat = rel[0]
            owner = rel[1] if len(rel) > 1 else re.sub(r"_plate_\d+\.gcode\.3mf$", "", f)
            if owner == "Custom Orders" and len(rel) > 2:
                owner = rel[2]  # customer / brand folder, e.g. "Thomas (DD Dubz)"
            try:
                p = read_plate(os.path.join(dp, f))
            except Exception as e:
                print("skip", f, e); continue
            v = re.search(r"(?:^|[\s_(])V(\d+)\b", f, re.I)
            p["version"] = int(v.group(1)) if v else 0
            groups[(cat, owner)][design_of(f, owner)].append((f, p))

    # Merge spelling variants of the same design within a folder (e.g. "DD Dubz With Cherry" vs
    # "DD Dubs - With Cherry"), so the version filter below compares V1/V2/V3 of the same design.
    import difflib
    for key in list(groups):
        merged = {}
        for design in sorted(groups[key], key=len, reverse=True):
            norm = re.sub(r"[^a-z0-9]", "", design.lower()).replace("z", "s")
            match = next((m for m in merged if difflib.SequenceMatcher(None, norm, merged[m][0]).ratio() >= 0.9), None)
            if match:
                merged[match][1].extend(groups[key][design])
            else:
                merged[design] = (norm, list(groups[key][design]))
        groups[key] = {d: v[1] for d, v in merged.items()}

    rows, plates_out, codes, used = [], [], [], set()
    max_sub = 1
    for (cat, owner) in sorted(groups):
        fam = FAMILY.get(owner) or proposed(PREFIX.get(owner, owner))
        codes.append([cat, owner, fam, "existing" if owner in FAMILY else "PROPOSED"])
        prefix = PREFIX.get(owner, owner)
        for design in sorted(groups[(cat, owner)]):
            ps = groups[(cat, owner)][design]
            for f, p in ps:
                plates_out.append([cat, owner, design, p["qty"], round(p["sec"] / 60, 1), p["g"], p["printer"],
                                   "; ".join(f"{x['label']} {x['g']}g" for x in p["fil"]), f])
            # Highest version only (Cody: V3 is the most reliable; older versions are superseded).
            top = max(x[1]["version"] for x in ps)
            latest = [x for x in ps if x[1]["version"] == top]
            # Stock plates = plates filled up with the design; other plates are coloring / preview plates.
            prod = [x for x in latest if x[1]["qty"] >= MIN_QTY] or [max(latest, key=lambda x: x[1]["qty"])]
            seen = set()
            for f, p in prod:
                if not p["qty"] or not p["fil"]:
                    continue
                names = [color_name(x["hex"]) for x in p["fil"]]
                colorway = "/".join(dict.fromkeys(c[0] for c in names))
                if (design, colorway) in seen:
                    continue
                seen.add((design, colorway))
                dcode = re.sub(r"[^A-Z0-9]", "", design.upper())[:4] or "DSGN"
                sku = f"{fam}_{dcode}_{names[0][1]}"
                n = 2
                while sku in used:
                    sku = f"{fam}_{dcode}_{names[0][1]}{n}"; n += 1
                used.add(sku)
                per_min = round(p["sec"] / p["qty"] / 60)
                subs = [(round(x["g"] / p["qty"], 2), x["label"]) for x in p["fil"]]
                max_sub = max(max_sub, len(subs))
                rows.append([f"{prefix} - {design} - {colorway}", sku, CATEGORY.get(cat, cat), per_min // 60,
                             per_min % 60, p["printer"], "", "", design, subs])

    header = ["Model Name", "SKU", "Category", "Print Hours", "Print Minutes", "Printer Model",
              "Print Prep Time (Minutes)", "Post Process Time (Minutes)", "Part 1"]
    for i in range(1, max_sub + 1):
        header += [f"Part 1 SubPart {i} Grams", f"Part 1 SubPart {i} Filament"]
    with open(os.path.join(OUT_ROOT, "3DPrintForce_ALL.csv"), "w", newline="", encoding="utf-8") as fh:
        w = csv.writer(fh); w.writerow(header)
        for r in rows:
            line = r[:9] + [v for g, lab in r[9] for v in (g, lab)]
            w.writerow(line + [""] * (len(header) - len(line)))
    with open(os.path.join(OUT_ROOT, "3DPrintForce_ALL_plates.csv"), "w", newline="", encoding="utf-8") as fh:
        w = csv.writer(fh)
        w.writerow(["Folder type", "Folder", "Design", "Objects", "Plate minutes", "Plate grams", "Printer",
                    "Filaments (plate totals)", "Sliced file"])
        w.writerows(plates_out)
    with open(os.path.join(OUT_ROOT, "3DPrintForce_ALL_codes.csv"), "w", newline="", encoding="utf-8") as fh:
        w = csv.writer(fh); w.writerow(["Folder type", "Folder", "Code family", "Status"]); w.writerows(codes)
    print(f"{len(rows)} model rows, {len(plates_out)} plates, {len(codes)} folders "
          f"({sum(c[3] == 'PROPOSED' for c in codes)} proposed codes); max colors per model {max_sub}")


if __name__ == "__main__":
    main()
