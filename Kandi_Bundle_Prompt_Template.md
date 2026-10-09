# Kandi Bracelet Bundle Prompt — Template

You give Claude **four things**. Claude works out everything else.

**Before you paste:**
1. Name photo files with **shorthands, all lowercase or as already shorthanded**, never the full festival or artist name (e.g. `ES-IM-IT-FestBeads-2.jpg`).
2. Put the photos in a folder under `IMGs/`, named anything readable (e.g. `IMGs/Force Fields/`). Claude renames it to the code.

---

```text
Kandi Bracelet Bundle Prompt
Build a draft Shopify listing for the kandi bracelet bundle in this folder, following Kandi_Bundle_Prompt_Template.md and CLAUDE.md. Save as DRAFT only.

1. FOLDER: IMGs/[folder name]/
2. MAIN PHOTO: [filename]
3. RESEARCH: [website link] [Instagram link]
4. BUNDLE CONTENTS: [total] bracelets, [paid] + [free] FREE
   - [design] x [qty]
   - [design] x [qty]
   - [design] x [qty]
```

### Example

```text
Kandi Bracelet Bundle Prompt
Build a draft Shopify listing for the kandi bracelet bundle in this folder, following Kandi_Bundle_Prompt_Template.md and CLAUDE.md. Save as DRAFT only.

1. FOLDER: IMGs/Force Fields/
2. MAIN PHOTO: FF-FestBeads.jpg
3. RESEARCH: https://[website] https://www.instagram.com/[account]/
4. BUNDLE CONTENTS: 8 bracelets, 7 + 1 FREE
   - logo + title x 3
   - [second design] x 3
   - logo only x 2
```

---

## What Claude does with it (no need to include in the prompt)

**Codes and folder**
- Reads the shorthands in the filenames and looks them up in `Platform_Reference.xlsx` → **Shorthand Map** tab, then the **SKU Convention** tab.
- Reuses an existing code when the festival/artist already has one; otherwise creates one (4 letters + version digit, festival bundles usually `[XX]BD1`) and checks it's unused.
- Adds any new shorthand to the Shorthand Map so the same logo always gets the same code.
- Renames the folder to `IMGs/[CODE]_[ShortName]/`.

**Collection**
- Creates `[Festival] Music Festival` in Shopify if it doesn't exist, visible on the same sales channels as the other festival collections.

**Research** (from the links)
- Festival dates, venue, camping vs. resort/city, and curator/headliner. Asks only if the site and Instagram don't make the curator clear.
- Camping → keep "two tents over"; resort → "two cabanas over"; city → "two stages over".
- Picks 2–3 fitting places for the closing paragraph.

**Photos**
- Reads designs and bead colors from the photos for alt text.
- Uploads every photo with original filenames; main photo is featured and linked to the variant.

**Product setup**
- Product Type: `Kandi Beads`. Material: PLA, Plastic (no Metal). Other three standing metafields per CLAUDE.md.
- One variant: `[paid] Pack + ([free] FREE)`, e.g. `7 Pack + (1 FREE)`. Customers buy as many as they want.
- SKU: `[CODE]_PCK[total]`. Inventory: 30 (default until set otherwise).
- **Price: $3.80 × paid bracelets** (e.g. 7 × $3.80 = $26.60). **Proposed rate — flagged "Needs approval: Karol"** in every summary until approved. Rule lives in `Platform_Reference.xlsx` → Pricing Master.

**Description**
- Bundle template with the kandi changes: bullet 1 → finished kandi bracelets ready to wear or trade; bullet 4 → layered multi-color print instead of Sprocket; intro → "stranger's wrist"; closing → "kandi bracelet" / "kandi bead" instead of clip wording. Bullets 2, 3, 5, K-Hole and the CTA stay verbatim. No signoff.
- Title: `[Festival] Rave Kandi Bracelet Bundle | EDM Kandi | Festival Bead`
- SEO title (<60), meta description (<160), 13 Etsy tags (<20 chars, no repeated first word).

**When finished**
- Runs the CLAUDE.md checklist, adds the code to the Product Roster and SKU Convention tabs, and gives a build summary with a **"Needs Karol's review"** list (price, anything assumed).
- Nothing is published. Karol reviews every listing before it goes live.
