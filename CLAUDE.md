# The Beat Drop — Claude Operating Instructions

*This file governs every Shopify listing task Claude performs for The Beat Drop. It supersedes ad-hoc instructions given mid-conversation unless the owner (Karol) explicitly overrides a rule for a single listing. Read `the-beat-drop-brand-identity.md` first for tone context, then treat this file as the enforceable rulebook. Actual listing copy (the words themselves) lives only in the two gold-standard `.docx` files — this file describes structure and rules, never embeds template text. See "Keeping This File in Sync" at the bottom.*

---

## Store

- **Shopify store:** thebeatdrop.myshopify.com
- **Account:** admin@thebeatdrop.store
- **Platform Claude builds listings for: Shopify only.** Products also sell on Etsy and TikTok Shop, but those channel listings are managed outside this workflow — the one exception is Etsy tag selection (see Etsy Tag Strategy below), which is still generated here.
- **Theme template:** Always assign `gp-template-581878106541785827` to every new listing. Never use Shopify's default template.

---

## CRITICAL RULES — READ FIRST

1. **Always save listings as DRAFT status only.** Never set status to ACTIVE. Never publish.
2. **Never use the words "The Beat Drop"** in any product title, description, SEO title, meta description, or image alt text.
3. **Never use "cheap," "knockoff," or similar devaluing language.**
4. **Never use "devotees."** Use "fans."
5. **Always use "colors" or "multi-color"** for the different colors a sprout comes in — never "variants" or "options" in customer-facing copy.
6. **Always use "outfit" or "clothing"** for festival attire — never "fit" in customer-facing copy.
7. **Fan-made framing is already built into the locked gold-standard templates through word choice.** Never add an explicit disclaimer sentence anywhere in listing copy (e.g., "this is not an official partnership with [Artist]") — the template's existing wording is how that positioning gets communicated. An inserted disclaimer sentence also breaks the "copy verbatim" rule on its own, since it's text the template doesn't contain.
8. **Wait for owner approval before any listing goes live.** Claude drafts; a human publishes.
9. **Set the four standing metaobject-linked metafields on every listing** (Material, Age group, Construction, Target gender) — see Shopify Category & Collections below for the exact values. These are fixed for every sprout SKU regardless of Standard/Bundle or theme, so there's nothing to ask about. **Exception: Kandi Beads have no metal clip, so Material is PLA + Plastic only.** Any other metaobject need outside these four is still not a Claude task — flag it, don't create it. **Exception (owner-approved 2026-10-09): for Kandi Beads listings, Claude may create missing `Pack Size` metaobject entries, using the exact variant name, so the Pack Size option can be linked.** Jewelry type and every other metaobject stay flag-only.
10. **If a live Shopify SKU conflicts with the naming convention below, match the live SKU** — do not silently "correct" an existing product's SKU to fit convention.
11. **If a build-out prompt specifies a variant/pack structure that differs from the defaults in this file** (e.g., individual colors offered in 1-Pack only, while multi-color is offered in 10-, 20-, and 30-Pack only), **build exactly what the prompt specifies.** The prompt's explicit instructions always override the default assumptions below.
12. **Shopify Product Type is always exactly one of three values — "Artist Sprout", "Festival Sprouts" (plural — the Festival Sprouts smart collection matches only the plural), or "Kandi Beads"** — stated per listing on the intake spec (see `BATCH_LISTING.md`); never guess between them. **Collection(s) are specified per prompt, not defaulted** — new collections are actively being introduced, never assume "Artist Sprouts" unless the prompt says so.
13. **Every build-out prompt should indicate "Standard" or "Bundle."** If neither is stated, ask before proceeding — pricing, variant structure, and description structure differ enough between the two that guessing is risky (see Bundle Listings section below).

---

## What We Sell

EDM rave sprouts — small 3D printed spring clip accessories worn by festival goers on hats, hair, bags, pashminas, and clothing. Sold as singles, multi-packs, and bundles. Each sprout features:

- Durable 3D printed kandi charm
- Weather-resistant adhesive
- Strong metal spring clip
- Built-in bead hole ("K-Hole") convertible into a kandi bracelet, kandi cuff, or kandi necklace
- The "Sprocket" — the reinforced connection point between the charm and the spring clip

---

## Brand Voice & Tone

Write in a **playful but professional, community-driven, PLUR-rooted, raver-native voice.** Speak the language of the festival community authentically. Full rationale in `the-beat-drop-brand-identity.md`.

**The Beat Drop uses two locked gold-standard listings, each saved as its own Word document — these `.docx` files are the single source of truth for listing copy, not this file:**

- **Standard (single-design) listings** — `Gold_Standard_Product_Listing.docx`
- **Bundle listings** — `Gold_Standard_Bundle_Listing.docx`

Never copy template text into this file. If the owner updates either gold-standard document, only that `.docx` needs to change — nothing here should ever need to change as a result (see "Keeping This File in Sync" below).

*(GRiZ, and an earlier Zeds Dead draft, were prior tone references and have been fully retired — always pull the current wording from the live `.docx` files above, never from memory of an older version.)*

---

## Which Template Applies

Every build-out prompt should say **Standard** or **Bundle**. If it doesn't say either, ask before proceeding — the two templates differ enough (pricing, variant structure, bullet count, description structure) that guessing is risky.

---

## Product Description Format

Copy body content always comes from the current gold-standard `.docx` verbatim — never rephrase, restructure, or write it fresh. What follows is the *structure* each template follows; the actual words live only in the `.docx` files.

### Standard (single-design) listings

1. **Title** (separate Shopify field, not part of the description body) — `[Artist] Rave Sprouts | EDM accessory | Festival Gift | [Color 1] [Color 2] [Color 3]`
2. **Hook** — 1–2 sentences. Fan-made framing communicated through word choice, includes the artist name and product name. *(The bolded artist-name line at the very top of `Gold_Standard_Product_Listing.docx` is a document label identifying which artist's example this is — it is not customer-facing copy and is not part of the description body.)*
3. **Intro paragraph** — 2 sentences, keyword-dense. Primary focus keyword must appear within the first 160 characters of the full description body.
4. **Benefit bullet list** — exactly 5 bullets, word for word, in the order they appear in the current `.docx`: functional snap-on/wear bullet, 3D-printed durability bullet, **"K-Hole"** bullet, **"Sprocket"** bullet, then the stock-up/colors bullet. Plain HTML `<li>` tags only — no bullet characters (●, •, or similar); Shopify renders its own bullets and a manual one causes doubles.
5. **"Perfect For" paragraph** — word for word. Festivals fixed: **Electric Forest, Lost Lands, Seven Stars.** Do not swap or add festivals.
6. **Call-to-action line** — "Share it. Trade it. Gift it. Receive it."

*(No brand signoff line, and no in-body headline — the standard template's only body-copy elements are the hook through the CTA line above.)*

### Bundle listings

*(This section previously said 4 bullets / no CTA / a real in-body headline. Checked against the live `Gold_Standard_Bundle_Listing.docx`, none of that held up — the Bundle template mirrors the Standard template's structure almost exactly. This drift is the exact failure mode "Keeping This File in Sync" warns about below.)*

1. **Hook** — 1–2 sentences, includes the bundle name/theme worked naturally into the sentence. *(The bolded line at the very top of `Gold_Standard_Bundle_Listing.docx`, e.g. "Lost Lands Bundle Description," is a document label identifying which bundle's example this is — same convention as the Standard template's artist-name label. It is not customer-facing copy and is not part of the description body; there is no separate in-body headline.)*
2. **Intro paragraph** — 2 sentences, keyword-dense.
3. **Benefit bullet list** — exactly **5 bullets**, word for word, same order as the Standard template: functional snap-on/wear bullet, 3D-printed durability bullet, **"K-Hole"** bullet, **"Sprocket"** bullet, then a stock-up/value-pack bullet in place of the colors bullet (bundles have no color variants, so this bullet points at the pack sizes instead).
4. **"Perfect For" / closing paragraph** — bundle listings are **not** bound by the Standard template's fixed festival list. Use whatever festivals/events genuinely fit that bundle's theme.
5. **Call-to-action line** — "Share it. Trade it. Gift it. Receive it." — same CTA as the Standard template.

Bundle listings have **no brand signoff** — the description ends on the CTA line.

**Fixed vs. adapts, when building a *new* bundle from a different theme than the current example:**
- Fixed (copy near-verbatim regardless of theme): the snap-on/wear bullet's shape, the durability bullet's shape, the full "K-Hole" bullet, the full "Sprocket" bullet, the stock-up/value-pack bolded lead-in, the CTA line, the absence of a signoff, and the 5-bullet count.
- Adapts per theme: the hook's scene/vibe description (including venue-appropriate details — e.g. a camping-festival reference like "two tents over" becomes something like "two stages over" for a non-camping/city festival), the intro's audience + headlining artist (if any — not every bundle needs a named artist), and the closing paragraph's festival/event references.

---

## SEO Requirements (every listing)

- **SEO title:** under 60 characters. Format: `[Artist] Rave Sprouts | EDM accessory | Festival Gift | [Color] [Color] [Color]`. Never repeat a word outside the pipe structure.
- **Meta description:** under 160 characters. Include the primary keyword naturally; include color variant names if the product has colors.
- **Focus keyword placement:** primary focus keyword must land within the first 160 characters of the description body.
- **Bold all SEO keywords** in the description body — natural, never stuffed.
- **Image alt text:** `[Artist] [design descriptor] rave sprout [color variant] — [brief descriptor]`. No pack sizes in alt text — use the color variant instead (bundle listings: use the bundle name in place of color variant).

---

## Pricing & Pack Sizes (Standard listings only — bundles use different pricing, see below)

| Pack Size | Shopify Variant Name Format | Price | Default Inv. | SKU Suffix | Standard on new listings? |
|---|---|---|---|---|---|
| 1 Pack | [Color] / 1 Pack | $3.00 | 50 | PCK1 | ✅ Default |
| 10 Pack | [Color] / 10 Pack + (1 FREE) | $28.00 | 20 | PCK10 | ✅ Default |
| 20 Pack | [Color] / 20 Pack + (2 FREE) | $55.00 | 10 | PCK20 | ✅ Default |
| 30 Pack | [Color] / 30 Pack + (3 FREE) | $81.00 | 5 | PCK30 | ✅ Default |

**Standard new listing default:** 1, 10, 20, 30-pack, unless the prompt specifies a different structure (see Critical Rule 11) — e.g., individual colors offered in 1-Pack only while multi-color is offered in 10/20/30-Pack only. Multi-quantity packs always include bonus free sprouts — mention this in copy.

**Compare-at price:** Only set when the build-out prompt is a duplicate/bonus request — i.e. the prompt asks to duplicate an existing listing with `(Bonus)` appended to the end of the source title. In that case, set the Shopify "Compare-at price" field on every variant of the duplicate to the same value as the Price listed in the table above for that pack size — e.g. 10 Pack: Price $28.00, Compare-at $28.00. Applies to all four pack sizes, including 1 Pack. For all other Standard listings (i.e. not a `(Bonus)` duplicate), leave the compare-at field blank.

**Bundle pricing does not use this table.** Bundle prices are unique per bundle and will be specified in the prompt every time — see Bundle Listings below.

### Duplicate/"(Bonus)" Listing Discount Formula

When duplicating an existing listing under this pack structure — individual colors in 1-Pack only, Multicolor in 10-/20-/30-Pack only (see Variant Rules and the Bundle-adjacent duplicate workflow) — apply this discount directly to **that source listing's own current live price** for each pack size, rather than requiring pricing to be manually supplied per listing:

| Pack Size | Discount off the source listing's live price |
|---|---|
| 1-Pack | 10% off |
| 10-Pack | 12.5% off |
| 20-Pack | 15% off |
| 30-Pack | 20% off |

- Applies the same way to Multicolor as to individual colors — the discount is keyed to the **pack size**, not the color. (Multicolor has no 1-Pack tier per the standard Variant Rules, so only the 10-/20-/30-Pack rates apply to it.)
- Round to the nearest cent using standard rounding (e.g. 10-Pack at $32.50 × 87.5% = $28.4375 → $28.44).
- This uses each source listing's **own** live price as the base — don't reuse another product's price or a static reference table. Two products with different original prices will produce different discounted prices even under the same discount percentages.
- This formula is the default whenever a duplicate/"(Bonus)" listing is requested without an explicit price override in the prompt. If a prompt gives explicit prices instead, those take priority over this formula for that batch.

---

## SKU Convention

**Format:** `[ARTIST_CODE]_[COLOR_CODE]_[PCK_SIZE]`
**Separator:** underscore ( _ ) — never dash
**Max length:** 50 characters

**Rules:**
- Artist/bundle code is **4 letters, followed by a versioning digit** (5 characters total when versioned) — no `_V2` suffixes. First design = digit `1` (e.g. `NCMF1`); second design for the same artist/bundle increments the digit (`NCMF1` → `NCMF2`). *(A number of earlier codes are shorter — 3 letters + digit, e.g. `GRZ1`, `AHE1` — from before this pattern was standardized. Per Rule 10, match the live SKU rather than renaming these; the 4-letter + digit pattern applies going forward.)*
- If the artist/design name is distinct enough on its own, a 4-character abbreviation with **no digit** is acceptable (e.g. `GRTN`, `DPCT`, `LLSS`, `LVTY`, `MRSV`, `NIKE`, `REZZ`, `RVSC`, `TAPB`).
- No-color products (single design, no color variants) omit the color segment entirely (e.g. `GTN1_PCK1`).
- **Bundle SKUs follow this same no-color-segment rule** — bundles don't carry a color code. Format: `[BUNDLE_CODE]_[PCK_SIZE]` (e.g. `NCMF1_PCK10`).
- If a live Shopify SKU conflicts with this convention, match the live SKU — do not "fix" an existing product's SKU.

**Examples:**
- `AHE1_TRQS_PCK1` — AHEE Alien, Turquoise, 1 Pack
- `GRZ4_PINK_PCK10` — Griz Grizzly Bear, Pink, 10 Pack
- `NCMF1_PCK10` — North Coast Music Festival bundle, 10 Pack (also matches live convention on `SDBD1`, `LLBD1`, `CABD1`)

**Shopify variant naming:** `[Color] / [X Pack]` for Standard listings, e.g. `Turquoise / 1 Pack`, `Black / 10 Pack + (1 FREE)`. **`[X Pack]` (no color prefix) for Bundle listings**, e.g. `10 Pack`.

**Full artist code list and all active SKUs:** see `Platform_Reference.xlsx` → SKU Convention tab. That spreadsheet is the source of truth — don't hand-maintain a second copy of the SKU bank in chat or in this file.

**Duplicate-for-testing SKU versioning:** when a prompt asks to duplicate an existing design as a new product (e.g., testing a different variant/pack structure on the same design), auto-generate the new artist code rather than requiring it to be spelled out — take the source SKU's artist code and append `v2` (e.g. `LLSS2` → `LLSS2v2`). Before finalizing, check the live catalog for that code: if `v2` is already in use, increment to `v3`, and so on. State the generated code in the build summary for owner awareness, since it's easy to collide with an existing test variant.

**Title suffix for duplicate/test listings:** unless the prompt specifies otherwise, a duplicate listing needs some distinguishing marker in the title so it doesn't read as an identical twin of the live product in the product list (e.g., appending `(Bonus)`). The exact marker is given per prompt — don't invent one silently, and don't assume no marker is needed just because the prompt didn't repeat the instruction from a prior duplicate.

---

## Standard Color Codes

AQUA · BLCK · BLUE · BRWN · CHRM · CPNK · CYAN · DKBL · DKGR · GLBL · GOLD · GREN · GRWH · LTBL · MLTC · NGRN · NGPK · OLVG · ORGN · ORPL · PINK · PKBL · PKPK · PKYW · PRPL · REDD · SLPL · SLVR · TEAL · TRQS · WBLK · WHIT · WOVG · YELW · BNDL (bundle/no-color design)

---

## Image Upload Rules

- **Source folder:** product images live in each batch's `IMGs/` subfolder (not `Listing_IMG/`).
- **Upload every image in the source subfolder** — not just those assigned to a color variant. Every image must be uploaded and get alt text, even if not linked to a variant.
- **Preserve original filenames** exactly. Do not rename images on upload.
- If a filename already exists in Shopify, append `_v2` before the extension (e.g. `ahee_black_1pack.jpg` → `ahee_black_1pack_v2.jpg`).
- **Link each color variant to its corresponding image(s).** No variant should be left unassigned. (Bundle listings: link images to the corresponding pack-size variant instead.)
- Alt text required for every uploaded image (see SEO Requirements above).
- **Known limitation:** Shopify's CDN blocks server-side image fetches (403). Image analysis or re-processing needs a client-side approach or the image provided directly — don't assume Claude can pull an already-uploaded Shopify image back down programmatically.

---

## Shopify Category & Collections

- **Shopify Product Type:** always exactly `Artist Sprout`, `Festival Sprouts`, or `Kandi Beads` — stated per listing on the intake spec (see `BATCH_LISTING.md`), never guessed. Full field mapping (Etsy category path, TikTok Shop category) for each lives in `Platform_Reference.xlsx` → Category Mapping tab.
- **Shopify Category (taxonomy):** required on every listing, never skip.
  - Sprouts (`Artist Sprout`, `Festival Sprouts`): `Apparel & Accessories > Clothing Accessories > Hair Accessories > Hair Pins, Claws & Clips`
  - Kandi (`Kandi Beads`): `Apparel & Accessories > Jewelry > Charms & Pendants > Charms`
- **Collections:** specified per prompt — new collections are actively being built out, never default to "Artist Sprouts" unless the prompt says so. Smart collections (`Festival Sprouts`, `Kandi Beads & Charms`) fill themselves from Product Type; don't assign them by hand. `1 FREE Sprout` only when the prompt asks.

**Metafields (every listing):** these four are fixed for every SKU of a given product line — the physical product doesn't change — so set them the same way every time, never per-prompt:

| Metafield | Value |
|---|---|
| Material | Polylactic Acid (PLA), Plastic, Metal — **Kandi Beads: Polylactic Acid (PLA), Plastic** (no metal clip) |
| Age group | Adults |
| Construction | Solid |
| Target gender | Unisex |

---

## Variant Rules

- **Default assumption** (used only when the prompt doesn't specify otherwise): Multicolor variants never get a 1 Pack. Multicolor is available in 10, 20, and 30-pack only.
- **When a prompt specifies a different variant/pack structure, build exactly what's requested** — e.g., individual colors offered in 1-Pack only while multicolor is offered in 10-, 20-, and 30-Pack only. The prompt's explicit structure always overrides the default above.
- Every color variant must be linked to its corresponding product image(s).
- Variant naming format: `[Color] / [X Pack]` for Standard listings; `[X Pack]` (no color) for Bundle listings.

---

## Bundle Listings

- **Trigger:** the build-out prompt will explicitly say "Bundle" or "Standard." If it doesn't say either, ask before proceeding.
- **Pricing:** bundle pricing is unique per bundle and will be specified in the prompt — never apply the Standard Pricing & Pack Sizes table to a bundle.
- **Variants:** bundles don't carry individual color names — only QTY-pack variants, no 1-Pack, no color prefix, unless the prompt explicitly says otherwise. Live naming: sprout bundles use `10 Sprout Bundle + (1 FREE)` / `20 Sprout Bundle + (2 FREE)` / `30 Sprout Bundle + (3 FREE)`; kandi bundles use `10 Pack + (1 FREE)` / `20 Pack + (2 FREE)` / `30 Pack + (3 FREE)`, or a single `[paid] Pack + ([free] FREE)` for kandi bracelet bundles.
- **Default inventory:** 10 Pack → 100, 20 Pack → 50, 30 Pack → 30, unless the prompt specifies otherwise.
- **SKU:** omit the color segment per the no-color SKU rule above — `[BUNDLE_CODE]_[PCK_SIZE]`.
- **Copy:** use `Gold_Standard_Bundle_Listing.docx` — nearly the same structure as the Standard template (5 bullets, has a CTA line, no fixed festival list, no signoff — see Product Description Format above). Never use the Standard single-design template for a bundle, and never use the Bundle template for a single-design listing.
- **Category/Collection/taxonomy:** same rules as Standard listings above — Product Type and Collection per prompt, taxonomy always set.

---

## Kandi Bead Bundles

Clip-less 3D printed kandi charms, currently sold as finished pony-bead bracelets. Full build steps live in **`Kandi_Bundle_Prompt_Template.md`** (4-input prompt: folder, main photo, research links, bundle contents) — follow it for every kandi bundle. Key rules:

- **Product Type** `Kandi Beads`; **Category** Charms (see Shopify Category & Collections); **Material** PLA + Plastic; **Color** Multicolor; **Jewelry material** Plastic; Jewelry type left for the owner.
- **Pack Size option is linked** to the `Pack Size` metaobjects (like SSMF2). Missing entries may be created for kandi listings (see Rule 9 exception).
- **Copy:** `Gold_Standard_Bundle_Listing.docx` with five kandi changes — bullet 1 (finished bracelets / beads onto kandi bracelets), bullet 4 (layered multi-color print instead of Sprocket), intro "stranger's wrist" instead of "hat", closing "kandi bracelet" and "kandi bead" instead of clip wording. Venue phrase adapts: camping "two tents over", resort "two cabanas over", city/indoor "two stages over".
- **Title:** `[Presenting Artist] [Festival/Event] Rave Kandi Bracelet Bundle | EDM Kandi Charms | Festival Bead`. Presenting artist only when the event is "presented by" one; SEO title, meta description and hook use the same name.
- **Codes:** an event presented by an artist uses that artist's code family (e.g. Wobbleween → `GWNT`). Photo shorthands map to codes in `Platform_Reference.xlsx` → **Shorthand Map**; check it, the SKU Convention tab, and live Shopify before creating a code.
- **Pricing (proposed, needs Karol's approval):** $3.80 × paid bracelets. Charm-only kandi bundles: $23 / $45 / $67 for 10 / 20 / 30. Rule lives in `Platform_Reference.xlsx` → Pricing Master.

---

## Etsy Tag Strategy (13 tags max × 20 chars each)

- **No two tags in the same listing may start with the same first word.** (❌ `rave sprout` + `rave accessory` + `rave kandi`; ✅ `rave sprout` + `sprout clip`.)
- **When focus keywords are provided in the prompt, prioritize them over the standard Always list** — swap Always tags as needed, as long as the 20-char limit and no-repeated-first-word rules hold.
- Full current tag bank (Always / Rotate / Specific / Retired, with search-volume notes) lives in `Shopify_Platform_Reference.xlsx` → Etsy Tag Bank tab. That tab is refreshed periodically with keyword performance data — check it's current before a large batch run, since retired tags should never be reused.

---

## New Listing Checklist (complete for every draft)

- [ ] Title follows format, ≤140 chars, no repeated words
- [ ] Hook frames design as fan-made/fan-inspired via the template's existing wording — **no explicit "official partnership" disclaimer sentence inserted anywhere**
- [ ] Primary focus keyword appears within first 160 characters of description body
- [ ] Correct template used: Standard (5 bullets, has CTA, no in-body headline) vs. Bundle (5 bullets, has CTA, no signoff, no in-body headline) — confirmed against the prompt before writing
- [ ] Shopify description: full HTML, `<li>` tags only (no ● characters)
- [ ] Standard listings: all 5 bullets used word for word in the order given in `Gold_Standard_Product_Listing.docx` — only the colors bullet changes. Bundle listings: all 5 bullets used per `Gold_Standard_Bundle_Listing.docx` — only the last bullet (stock-up/value-pack) and the festival references change
- [ ] Artist name (Standard) or bundle theme details (Bundle) substituted correctly from the template placeholders
- [ ] Bead hole named "K-Hole" and bolded
- [ ] Clip-to-charm connection point named "Sprocket" and bolded
- [ ] Standard colors listed inline in the colors bullet (Standard, non-Multicolor only) — Bundle listings use the multi-color/value-pack bullet instead
- [ ] Festivals unchanged — Electric Forest, Lost Lands, Seven Stars (Standard listings only; Bundle listings may use theme-appropriate festivals)
- [ ] "Devotees" not used anywhere — "fans" used instead
- [ ] SEO meta title customized (≤60 chars, no repeated words)
- [ ] Meta description written (≤160 chars, primary keyword + color names if applicable)
- [ ] Focus keywords bolded and prioritized in description (if provided)
- [ ] Variant/pack structure matches the prompt exactly — default assumptions only used when the prompt doesn't specify otherwise
- [ ] Standard listings: prices entered per the Pricing table above. Bundle listings: prices entered exactly as specified in the prompt
- [ ] SKUs entered in correct format, ≤50 chars (Bundle SKUs omit the color segment)
- [ ] No Multicolor / 1 Pack variant created (Standard listings, unless prompt says otherwise)
- [ ] Every variant linked to its image(s)
- [ ] Default inventory quantities set
- [ ] ALL images in subfolder uploaded (not just color-linked ones)
- [ ] Original filenames preserved (`_v2` appended only if duplicate)
- [ ] Image alt text written for every photo
- [ ] Theme template set to `gp-template-581878106541785827`
- [ ] Shopify Category set (Hair Pins, Claws & Clips for sprouts; Charms for Kandi Beads)
- [ ] Shopify Product Type set to `Artist Sprout`, `Festival Sprouts`, or `Kandi Beads` **per the intake spec**
- [ ] Collection(s) assigned **per prompt**
- [ ] Metafields set: Material (Polylactic Acid (PLA), Plastic, Metal — no Metal for Kandi Beads), Age group (Adults), Construction (Solid), Target gender (Unisex)
- [ ] Etsy tags applied — no two starting with the same first word
- [ ] Focus keywords prioritized in tag selection (if provided)
- [ ] 10 Always Etsy tags + 3 Rotate/Specific selected
- [ ] Product status set to **DRAFT** — never Active
- [ ] Product Roster tab updated in `Platform_Reference.xlsx`

---

## Keeping This File in Sync

**Gold-standard listing copy (Standard and Bundle) lives only in `Gold_Standard_Product_Listing.docx` and `Gold_Standard_Bundle_Listing.docx`.** This file (`CLAUDE.md`) describes structure, formatting, pricing, and process rules — it should never contain the actual template wording. When the owner updates either `.docx`, only that file needs to change. If a change ever seems to require editing both a `.docx` and this file, that's a sign template text has leaked into this file again — check the Product Description Format section above for any copy that snuck in and remove it.

---

## Reference Files (should live alongside this one)

| File | Format | What's in it |
|---|---|---|
| `the-beat-drop-brand-identity.md` | .md | Brand voice rationale, audience, positioning — read first for context |
| `Gold_Standard_Product_Listing.docx` | .docx | **Sole source of truth** for the locked Standard (single-design) listing copy |
| `Gold_Standard_Bundle_Listing.docx` | .docx | **Sole source of truth** for the locked Bundle listing copy |
| `BATCH_LISTING.md` | .md | Step-by-step multi-listing workflow + asset folder structure |
| `Shopify_Platform_Reference.xlsx` | .xlsx | Character limits, category mapping, pricing master, Etsy tag bank, keyword bank |
| `workflows.md` | .md | The most common recurring tasks, broken into executable steps |
| `Platform_Reference.xlsx` | .xlsx | Full SKU bank, product roster, **Shorthand Map** (photo shorthand → code), Pricing Master — the live catalog source of truth; this is Karol's working file, shared directly rather than recreated |
| `Kandi_Bundle_Prompt_Template.md` | .md | 4-input build prompt and full build rules for kandi bead/bracelet bundles |
| `Listing_Prompt_Template.md` | .md | Build prompt for sprout listings (Standard and Bundle) |

