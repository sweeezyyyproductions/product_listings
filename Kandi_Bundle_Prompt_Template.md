# Kandi Bracelet Bundle Prompt — Template

You give Claude **four things** (plus one optional line). Claude works out everything else.

**Before you paste:**
1. Name photo files with **this event's shorthand**, never the full festival or artist name (e.g. `FF-Bundle-FestBeads-15.jpg`). Check the Lightroom export name isn't left over from the last bundle.
2. Put the photos in a folder under `IMGs/`, named anything readable (e.g. `IMGs/Force Fields/`). Claude renames it to the code.
3. If the event website won't load for Claude (some need JavaScript), attach the event poster instead of a link.

---

```text
Kandi Bracelet Bundle Prompt
Build a draft Shopify listing for the kandi bracelet bundle in this folder, following Kandi_Bundle_Prompt_Template.md and CLAUDE.md. Save as DRAFT only.

1. FOLDER: IMGs/[folder name]/
2. MAIN PHOTO: [filename]
3. RESEARCH: [website link] [Instagram link]  (or attach the poster)
4. BUNDLE CONTENTS: [total] bracelets, [paid] + [free] FREE
   - [design] x [qty]
   - [design] x [qty]
   - [design] x [qty]
5. PACK OPTIONS (optional): [single bundle | 10/20/30 packs]  (default: single bundle)
```

**Check before sending:** the design quantities add up to the total.

### Example

```text
Kandi Bracelet Bundle Prompt
Build a draft Shopify listing for the kandi bracelet bundle in this folder, following Kandi_Bundle_Prompt_Template.md and CLAUDE.md. Save as DRAFT only.

1. FOLDER: IMGs/Force Fields/
2. MAIN PHOTO: FF-Bundle-FestBeads-15.jpg
3. RESEARCH: https://[website] https://www.instagram.com/[account]/
4. BUNDLE CONTENTS: 8 bracelets, 7 + 1 FREE
   - logo + title x 3
   - [second design] x 3
   - logo only x 2
```

---

## What Claude does with it (no need to include in the prompt)

**Codes and folder**
- Reads the shorthands in the filenames and looks them up in `Platform_Reference.xlsx` → **Shorthand Map** tab, then the **SKU Convention** tab, **then live Shopify** (products made outside this workflow may be missing from the sheet).
- If the event is **"presented by" an artist** (e.g. Ganja White Night presents Wobbleween), uses that **artist's code family** (`GWNT3`), matching any existing products for the event.
- Otherwise reuses the festival's existing code, or creates one (4 letters + version digit, festival bundles usually `[XX]BD1`) and checks it's unused.
- Adds any new shorthand to the Shorthand Map so the same logo always gets the same code.
- Renames the folder to `IMGs/[CODE]_[ShortName]/`.

**Collections**
- Festival/event collection: `[Festival] Music Festival` (or just the event name for one-off events like `Wobbleween`). Creates it if missing, visible on the same 11 sales channels as the other festival collections.
- `Kandi Beads & Charms` is joined automatically from the Product Type; nothing to set.
- `1 FREE Sprout` is **not** added unless the prompt asks for it.

**Research** (from the links or poster)
- Dates, venue, camping vs. resort/city, curator/headliner, and whether the event is **presented by** an artist. Asks only if none of this is clear.
- Camping → keep "two tents over"; resort → "two cabanas over"; city/indoor → "two stages over".
- Names the curator/presenting artist in the intro ("the kind of kandi bracelet [Artist] fans wear…"); uses "you" if there is none.
- Picks 2–3 fitting places for the closing paragraph.
- Artists on a lineup are **not** named in copy unless they're the curator/presenter. Unknown logos and collab designs are described by what's visible, never guessed.

**Photos**
- Reads designs and bead colors from the photos for alt text.
- Uploads every photo with original filenames; main photo is featured and linked to the variant.

**Product setup**
- Product Type: `Kandi Beads`.
- **Shopify Category: `Apparel & Accessories > Jewelry > Charms & Pendants > Charms`** — overrides the Hair Pins category CLAUDE.md uses for sprouts (matches the live Seven Stars Kandi listing).
- Material: PLA, Plastic (no Metal). Other three standing metafields per CLAUDE.md.
- **Single bundle (default):** one variant `[paid] Pack + ([free] FREE)`, e.g. `7 Pack + (1 FREE)`; customers buy as many as they want. SKU `[CODE]_PCK[total]`.
- **10/20/30 packs (if asked):** `10 Pack + (1 FREE)` / `20 Pack + (2 FREE)` / `30 Pack + (3 FREE)`, SKUs `[CODE]_PCK10/20/30`.
- **Pack-size metafield:** set when a matching option exists in Shopify (10/20/30 always do). For custom counts it's left blank and flagged — Karol can add the option under Settings → Custom data → Metaobjects → Pack size.
- Inventory: 30 per variant (placeholder until set otherwise). Shipping weight is left at 0 and flagged.
- **Price: $3.80 × paid bracelets** (e.g. 7 × $3.80 = $26.60). **Proposed rate — flagged "Needs approval: Karol"** in every summary until approved. Rule lives in `Platform_Reference.xlsx` → Pricing Master.

**Title & SEO**
- Title: `[Presenting Artist] [Festival/Event] Rave Kandi Bracelet Bundle | EDM Kandi Charms | Festival Bead` — presenting artist only when the event is "presented by" one (e.g. `Ganja White Night Wobbleween Rave Kandi Bracelet Bundle | …`).
- SEO title (<60) and meta description (<160) use the same name as the title, presenting artist included.
- Hook uses the same name: "This fan-made **[Presenting Artist] [Event] Rave Kandi Bracelet Bundle** is…"
- 13 Etsy tags (<20 chars, no repeated first word), saved as Shopify tags.

**Description**
- Bundle template with the kandi changes: bullet 1 → finished kandi bracelets ready to wear or trade; bullet 4 → layered multi-color print instead of Sprocket; intro → "stranger's wrist"; closing → "kandi bracelet" / "kandi bead" instead of clip wording; stock-up bullet → the bundle count ("7 bracelets plus 1 FREE…") or the 10/20/30 packs. Bullets 2, 3, K-Hole and the CTA stay verbatim. No signoff.

**When finished**
- Runs the CLAUDE.md checklist, adds the code to the Product Roster and SKU Convention tabs, and gives a build summary with a **"Needs Karol's review"** list (price, anything assumed).
- Nothing is published. Karol reviews every listing before it goes live.
