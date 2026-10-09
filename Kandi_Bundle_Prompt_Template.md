# Kandi Bead Bundle Prompt — Template

Fill in the `[brackets]`, delete any line you don't need, and paste the box into Claude Code from this folder. One prompt per bundle.

**Before you paste:**
1. Put the photos in `IMGs/[CODE]_[ShortName]/` (e.g. `IMGs/EMBD1_EmberShoresBundle/`).
2. Pick an unused code: 4 letters + version digit, usually festival letters + `BD` (e.g. `HWBD1`, `EMBD1`). Claude will check it's free.
3. Create the festival collection in Shopify, or ask Claude to create it.

Built from the Hulaween (`HWBD1`) and Ember Shores (`EMBD1`) kandi bundles. Kandi bundles are clip-less, so they differ from sprout bundles in Product Type, pricing, variant names, Material, and five spots in the description.

---

```text
Kandi Bead Bundle Prompt
Create a draft Shopify listing for [Festival/Theme] Rave Kandi Bundle (bundle code [CODE]1).

Reference CLAUDE.md for Shopify setup, brand voice, banned terms, and field mapping. Use Gold_Standard_Bundle_Listing as the structural benchmark, and model this listing on the live kandi bundles HWBD1 (Hulaween) and EMBD1 (Ember Shores). Save as DRAFT only — do not publish.

PRODUCT
- These are clip-less kandi charms: no metal spring clip, no Sprocket.
- What ships: [charms only | charms + pony-bead bracelets]
- Designs in the bundle: [list each charm, e.g. festival logo, artist logo, 3D phoenix head]
- Product Type: Kandi Beads
- Collection(s): [Festival Name Music Festival]
- Material metafield: Polylactic Acid (PLA), Plastic (no Metal)

PHOTOS
- Folder: IMGs/[CODE]1_[ShortName]/
- Featured image (linked to every variant): [filename of the full-set photo]
- Upload every photo in the folder with original filenames and alt text.

PACK SIZES & PRICING (no color variants)
- 10 Pack + (1 FREE): $23 — SKU [CODE]1_PCK10 — inventory 100
- 20 Pack + (2 FREE): $45 — SKU [CODE]1_PCK20 — inventory 50
- 30 Pack + (3 FREE): $67 — SKU [CODE]1_PCK30 — inventory 30
(Delete or change lines if this bundle uses different sizes or prices.)

FESTIVAL CONTEXT
- Research links: [official site] [Instagram]
- Dates & venue: [e.g. Nov 20–22, 2026, Barceló Riviera Maya, Mexico]
- Venue type: [camping → keep "two tents over" | resort/city → adapt, e.g. "two cabanas over" / "two stages over"]
- Curator/headliner for the intro (optional): [artist name, or leave blank to use "you"]
- Closing paragraph places: [e.g. Riviera Maya, Red Rocks, Lost Lands]

DESCRIPTION
Use the bundle template with the same five kandi changes as HWBD1/EMBD1:
1. Bullet 1 → "Kandi charm that travels" (beads onto kandi bracelets, cuffs, or necklaces)
2. Bullet 4 → "Layered multi-color print" instead of Sprocket
3. Intro → "stranger's wrist" instead of "hat"
4. Closing → "kandi bracelet" instead of "festival hair clip"
5. Closing → "kandi bead" instead of "sprout clip"
Keep bullets 2, 3, 5, the K-Hole naming, and the CTA verbatim. No signoff.
If bracelets ship, say so in bullet 1 and the intro.

GENERATE
- Title: [Festival] Rave Kandi Bundle | EDM Kandi Charms | Festival Bead
- SEO title (<60 chars) and meta description (<160 chars)
- Shopify HTML description per the above, SEO keywords bolded
- SEO alt text for every photo: "[Festival] rave kandi bundle — [what the photo shows]"
- 13 Etsy tags (<20 chars each, no two starting with the same first word), saved as Shopify tags
  Focus tags to include (optional): [e.g. hulaween, spirit lake]

WHEN FINISHED
1. Run the CLAUDE.md New Listing Checklist.
2. Add [CODE]1 to the Product Roster and SKU Convention tabs in Platform_Reference.xlsx, with a Notes entry.
3. Give me a build summary: title, SKUs and prices, collection, alt text, tags, and anything that needs my decision.
```

---

## Example (Ember Shores, as built)

```text
Kandi Bead Bundle Prompt
Create a draft Shopify listing for Ember Shores Rave Kandi Bundle (bundle code EMBD1).

Reference CLAUDE.md for Shopify setup, brand voice, banned terms, and field mapping. Use Gold_Standard_Bundle_Listing as the structural benchmark, and model this listing on the live kandi bundle HWBD1 (Hulaween). Save as DRAFT only — do not publish.

PRODUCT
- These are clip-less kandi charms: no metal spring clip, no Sprocket.
- What ships: charms only
- Designs in the bundle: Ember Shores logo, ILLENIUM logo, ILLTRONICS, 3D phoenix head, flat phoenix (black, orange), ILLENIUM double-phoenix emblem
- Product Type: Kandi Beads
- Collection(s): Ember Shores Music Festival
- Material metafield: Polylactic Acid (PLA), Plastic (no Metal)

PHOTOS
- Folder: IMGs/EMBD1_EmberShoresBundle/
- Featured image (linked to every variant): ES-IM-IT-FestBeads.jpg

PACK SIZES & PRICING (no color variants)
- 10 Pack + (1 FREE): $23 — SKU EMBD1_PCK10 — inventory 100
- 20 Pack + (2 FREE): $45 — SKU EMBD1_PCK20 — inventory 50
- 30 Pack + (3 FREE): $67 — SKU EMBD1_PCK30 — inventory 30

FESTIVAL CONTEXT
- Research links: https://embershores.com/ https://www.instagram.com/embershores/
- Dates & venue: Nov 20–22, 2026, Barceló Riviera Maya, Mexico
- Venue type: resort → "two cabanas over"
- Curator/headliner for the intro: ILLENIUM
- Closing paragraph places: Riviera Maya, Red Rocks, Lost Lands
```
