# Kandi Bundle Prompt — Template

You give Claude **six things**. Claude works out everything else. Model listing: the live **Seven Stars Rave Kandi Bundle (SSMF2)**.

**Before you paste:**
1. Name photo files with **this event's shorthand**, never the full festival or artist name (e.g. `FF-Bundle-FestBeads-15.jpg`). Check the Lightroom export name isn't left over from the last bundle.
2. Put the photos in a folder under `IMGs/`, named anything readable (e.g. `IMGs/Force Fields/`). Claude renames it to the code.
3. Update the **folder path** — don't reuse the last prompt's.
4. Check the contents add up to the total.
5. If the event website won't load for Claude (some need JavaScript), attach the event poster instead of a link.

---

```text
Kandi Bundle Prompt
Build a draft Shopify listing for the kandi bundle in this folder, following Kandi_Bundle_Prompt_Template.md and CLAUDE.md. Model it on the live Seven Stars Rave Kandi Bundle (SSMF2). Save as DRAFT only.

1. FOLDER: IMGs/[folder name]/
2. MAIN PHOTO: [filename]
3. RESEARCH: [website link] [Instagram link]   (or attach the poster)
4. WHAT SHIPS: [charms only | charms + pony-bead bracelets]
5. ONE BUNDLE = [total] pieces + FREE ITEM: [1 sprout | none]
   - [design] x [qty]   ([colors, if more than one])
   - [design] x [qty]
   - [design] x [qty]
6. PACK SIZES & PRICING (optional — leave blank to copy the event's sprout bundle):
   - [N] Pack: $[price] — inventory [qty]
```

### Example (Wobbleween, as built)

```text
Kandi Bundle Prompt
Build a draft Shopify listing for the kandi bundle in this folder, following Kandi_Bundle_Prompt_Template.md and CLAUDE.md. Model it on the live Seven Stars Rave Kandi Bundle (SSMF2). Save as DRAFT only.

1. FOLDER: IMGs/WW/
2. MAIN PHOTO: WW-Bundle-FestBeads-43.jpg
3. RESEARCH: (poster attached)
4. WHAT SHIPS: charms + pony-bead bracelets
5. ONE BUNDLE = 19 pieces + FREE ITEM: 1 sprout
   - CollabTitle1 x 3 (3 colors)
   - CollabTitle2 x 3 (3 colors)
   - Title x 5
   - skeleton x 2
   - pumpkin x 1
   - doll x 1
   - 3 headed flower x 1
   - flower x 3 (3 colors)
6. PACK SIZES & PRICING (optional — leave blank to copy the event's sprout bundle):
```
Result: copied from the Wobbleween sprout bundle (GWNT2) → `10 Pack + (1 FREE)` $52 / `20 Pack + (2 FREE)` $99 / `30 Pack + (3 FREE)` $144.50, inventory 100 / 50 / 30.

---

## What Claude does with it (no need to include in the prompt)

**Codes and folder**
- Reads the shorthands in the filenames and looks them up in `Platform_Reference.xlsx` → **Shorthand Map**, then the **SKU Convention** tab, **then live Shopify** (products made outside this workflow may be missing from the sheet).
- If the event is **"presented by" an artist** (e.g. Ganja White Night presents Wobbleween), uses that **artist's code family** (`GWNT3`), matching any existing products for the event.
- Otherwise reuses the festival's existing code, or creates one (4 letters + version digit, festival bundles usually `[XX]BD1`) and checks it's unused.
- Adds any new shorthand to the Shorthand Map so the same logo always gets the same code.
- Renames the folder to `IMGs/[CODE]_[ShortName]/`.

**Research** (from the links or poster)
- Dates, venue, camping vs. resort/city, curator/headliner, and whether the event is **presented by** an artist. Asks only if none of this is clear.
- Camping → "two tents over"; resort → "two cabanas over"; city/indoor → "two stages over".
- Names the curator/presenting artist in the intro ("the kind of kandi bracelet [Artist] fans wear…"); uses "you" if there is none.
- Picks 2–3 fitting places for the closing paragraph.
- Lineup artists are **not** named in copy unless they're the curator/presenter. Unknown logos and collab designs are described by what's visible, never guessed.

**Product setup**
- Product Type `Kandi Beads`. Vendor The Beat Drop. Theme template `gp-template-581878106541785827`.
- **Category: `Apparel & Accessories > Jewelry > Charms & Pendants > Charms`**.
- Metafields: Material **PLA, Plastic** (no Metal); Age group Adults; Construction Solid; Target gender Unisex; **Color: Multicolor; Jewelry material: Plastic**. Jewelry type is left for the owner.
- **Variants — copied from the event's sprout bundle** (input 6 blank):
  - Same pack sizes as the sprout bundle (usually 10 / 20 / 30), same inventory.
  - **Price = sprout bundle price + $2 per pack** (e.g. sprout $50 / $97 / $142.50 → kandi $52 / $99 / $144.50).
  - If the event has no sprout bundle, use the standard sprout bundle prices $35 / $65 / $90 → kandi **$37 / $67 / $92**, inventory 100 / 50 / 30.
  - If input 6 is filled in, use exactly those packs, prices and inventory instead.
- **Names follow the product type — never copy the sprout wording:**

  | | Sprout | Kandi Beads |
  |---|---|---|
  | Pack name | `10 Sprout Bundle + (1 FREE)` | `10 Pack + (1 FREE)` |
  | Material | PLA, Plastic, Metal | PLA, Plastic |
  | Category | Hair Pins, Claws & Clips | Charms |

- The free item is a rave sprout: 1 per 10 (`+ (1 FREE)` / `(2 FREE)` / `(3 FREE)`); say so in the stock-up bullet.
- SKU `[CODE]_PCK[N]` per pack.
- **Pack Size option is linked** to the store's Pack Size metaobjects (like SSMF2). Standard 10 / 20 / 30 entries already exist; missing ones are created with the exact variant name, then linked.
- All variants show the main photo. Shipping weight is left at 0 and flagged.

**Collections**
- Festival/event collection: `[Festival] Music Festival`, or the event name for one-off events (e.g. `Wobbleween`). Created if missing, visible on the same 11 sales channels as the other festival collections.
- `Kandi Beads & Charms` is joined automatically from the Product Type.
- `1 FREE Sprout` is automatic too — it picks up any product with a `10 Pack + (1 FREE)` variant, so standard kandi packs join it on their own.

**Title & SEO**
- Bracelets: `[Presenting Artist] [Event] Rave Kandi Bracelet Bundle | EDM Kandi Charms | Festival Bead`
- Charms only: `[Presenting Artist] [Event] Rave Kandi Bundle | EDM Kandi Charms | Festival Bead`
- Presenting artist only when the event is "presented by" one. SEO title (<60), meta description (<160) and the hook use the same name.
- 13 Etsy tags (<20 chars, no repeated first word), saved as Shopify tags.

**Description** — `Gold_Standard_Bundle_Listing.docx` with the kandi changes:
- Bullet 1: bracelets → "Kandi bracelets ready to trade — 3D printed charms come strung on pony bead kandi bracelets…"; charms only → "Kandi charm that travels — beads onto kandi bracelets, cuffs, or necklaces…".
- Bullet 4: "Layered multi-color print" instead of Sprocket.
- Intro: "stranger's wrist" instead of "hat".
- Closing: "kandi bracelet" and "kandi bead" instead of clip wording.
- Stock-up bullet: the pack sizes, assorted designs/colors, and the free sprouts ("grab a 10-, 20-, or 30-pack of assorted [Event] designs and colors, each with FREE rave sprouts…").
- Mentions colorways when a design comes in more than one color.
- Bullets 2, 3, K-Hole and the CTA stay verbatim. No signoff.

**Alt text:** `[Event] rave kandi bracelet bundle — [what the photo shows]`, including bead colors.

**When finished**
- Runs the CLAUDE.md checklist, adds the code to the Product Roster and SKU Convention tabs (plus Shorthand Map if new), and gives a build summary with a **"Needs Karol's review"** list.
- Nothing is published. Karol reviews every listing before it goes live.
