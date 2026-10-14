# SOP: From Print File to Product Listing

Covers the full path from Cody's Bambu print file to a draft Shopify listing, using the batch slicer
at `C:\Users\DATA A\Desktop\Sliced Exports\batch_slice.py`. A backup copy lives in this repo at
`scripts/batch_slice.py`; both write sliced files to `Desktop\Sliced Exports`, never into the repo.

Steps 10–13 (reading sliced files and filling the sheets) are done by Claude on request until that
step is saved as its own tool.

## Cody (designer)

1. Save the Bambu project in the correct folder under `Sprout Designs\` on the Mac: `ARTISTS\[Artist]\`, `Festivals\[Event]\`, or `Generic\`.
2. Name the file `V# [Artist/Event] - [Design]`, e.g. `V1 Boo Seattle - Spider.3mf`.
3. Put each pack size on its own plate (1, 10, 20, 30…) and delete empty plates.
4. Keep parts and the wipe tower away from the plate edge.
5. Let the Mac sync to Google Drive, then say which file or folder is new.

## Slicing

6. Close Bambu Studio.
7. Open PowerShell and run:
   ```bash
   cd "C:\Users\DATA A\Desktop\Sliced Exports"
   ```
8. Slice only the new folder:
   ```bash
   python batch_slice.py "Festivals\Boo Seattle"
   ```
9. Open `_slice_log.csv` and check the rows for that file:
   - **ok**: done.
   - **empty**: ignore.
   - **FAILED**: send Cody the *note* text, wait for the fix, then repeat step 8.

## Data (with Claude)

10. Tell Claude: *"New sliced files in Sliced Exports\[folder]. Run intake."*
11. Claude returns, for review:
    - Artist or event, shorthand, and product code (existing, or a proposed new one)
    - Design name, colorways, SKUs, and the photo file names to use
    - The 3DPrintForce row: print time, grams per color, printer, quantity per plate
12. Approve any new code or shorthand, and correct colorway names if needed.
13. Claude adds the rows to `Platform_Reference.xlsx` and to the 3DPrintForce bulk CSV.
    The CSV is made by `scripts/make_3dpf_csv.py` (one row per production plate = one colorway, time and grams per piece):
    ```bash
    python scripts\make_3dpf_csv.py "Festivals\Boo Seattle" --prefix "BOO Seattle" --code BSBD1
    ```
    Output: `Desktop\Sliced ExportsDPrintForce_<name>.csv` plus a `_plates.csv` with every plate's totals.
14. **Karol** uploads the CSV to 3DPrintForce and confirms pricing per sales channel.

## Printing and photos

15. Print the plates.
16. Shoot photos, mostly charms only: each design, each color, and the pack as a bunch in a bowl or cup. Take at most 1–2 bracelet styling shots.
17. Drop the photos in `Product Photos\Dump\`.
18. Tell Claude: *"Rename and file the Dump photos for [event/artist]."* Claude names them from the intake sheet and moves them to `Product Photos\[Name]\Beads\`.

## Listing

19. Tell Claude: *"Build the draft listing for [code]"*, with the main photo and pricing (or "copy [listing]").
20. Claude creates a **draft** in Shopify. It never publishes.
21. **Karol** reviews price, inventory, and photos, then publishes.
22. Push the spreadsheet updates from GitHub Desktop.

## One-time: fill 3DPrintForce for the whole back catalog

23. Set the PC to never sleep, then run `python batch_slice.py` with no folder name. It takes about 6–12 hours; if it stops, run it again and it skips plates already done.
24. Tell Claude: *"Full slice done, build the 3DPrintForce bulk CSV."*

## Notes

- Sliced files go to `Desktop\Sliced Exports\` in the same folder structure as `Sprout Designs`. Cody's originals are never changed.
- Each plate is sliced separately (`[file]_plate_[N].gcode.3mf`), because slicing all plates at once fails on any empty plate.
- Common FAILED reasons: *"G-code outside of the printable area"* (move the part or wipe tower inward) and *"Invalid parameter value(s)"* (re-save the file in the current Bambu Studio).
- Only 9 of 427 project files had slice data saved inside them (checked 2026-10-14), so slicing is needed for print time and grams.
