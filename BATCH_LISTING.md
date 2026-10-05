# BATCH_LISTING.md — The Beat Drop: Multi-Listing Batch Workflow

*Referenced by `CLAUDE.md`'s Reference Files table as "step-by-step multi-listing workflow + asset folder structure." This file governs how a batch of Shopify listings gets built end to end. It doesn't repeat `CLAUDE.md`'s rules — it's the process wrapper around them, plus the one thing `CLAUDE.md` can't provide on its own: a way to guarantee every field it needs is filled in before a build starts.*

---

## Why this file exists

`CLAUDE.md` is strict about not guessing on certain fields — Standard vs. Bundle, Shopify Product Type, Collection(s) — because guessing wrong is worse than asking. But asking mid-build isn't the goal either. The fix is upstream: **fill in every required field before the build starts**, using the intake spec below, so there's nothing left for Claude Code to guess *or* ask about once the batch begins.

If a batch prompt is missing a required field from Section 1, the correct response is to flag it back to you as a single upfront question before starting — not to stop partway through a 15-variant build.

---

## Section 1 — Batch Intake Spec (fill out before every batch)

One row per listing. Every column is required unless marked optional. Paste this table into the batch prompt, filled in, or attach it as a companion doc.

| Field | Required? | Notes |
|---|---|---|
| **Listing type** | Yes — Standard or Bundle | No default exists. See CLAUDE.md Rule 13. |
| **Artist / bundle name & theme** | Yes | Exact name as it should appear in copy. |
| **Research link(s)** | Optional | Spotify / official site / Insomniac profile, etc. — used only for lightweight sensory details per CLAUDE.md's "Using Research Links" section, never a bio. |
| **Colors** (Standard only) | Yes, if Standard | List every color name + its Standard Color Code (see CLAUDE.md). If a color isn't in the existing code list, flag it — don't invent a code silently. |
| **Variant / pack structure** | Yes, if different from default | Default is 1/10/20/30-Pack, all colors, Multicolor in 10/20/30 only (no 1-Pack). State explicitly if this listing uses a different structure (e.g., individual colors 1-Pack only, Multicolor 10/20/30 only). |
| **Pricing** | Standard: optional (defaults to Pricing Master table). Bundle: **required, no default exists.** | Bundle pricing must be given per pack size every time — CLAUDE.md is explicit that the Standard pricing table never applies to bundles. |
| **Shopify Product Type** | Yes — always | Must be exactly `Artist Sprout` or `Festival Sprout` (CLAUDE.md Rule 12) — stated per listing even if it's the same as the last batch. See `Platform_Reference.xlsx` → Category Mapping tab for the full field mapping of each. |
| **Collection(s)** | Yes — always | Same as above — no default. |
| **SKU code** | Optional | Auto-generated per the SKU Convention (4 letters + versioning digit) if not supplied. If supplied, must match an existing live code exactly (Rule 10) or be confirmed as a new one. |
| **Duplicate / "(Bonus)" marker** | Yes, if this is a duplicate listing | State the exact title marker to use (e.g. "(Bonus)") — CLAUDE.md won't invent one. |
| **Image folder** | Yes | Path to this listing's subfolder under `IMGs/` — see Section 2. |
| **Theme adaptation notes** (Bundle only) | Optional | Any venue-specific language swaps (e.g., camping references → city-festival language for a non-camping event), non-default festival/event references for the closing paragraph. |

**If any required field is blank when a batch starts:** ask once, up front, for the full batch — not partway through, and not per-listing. Once the batch begins, treat this table as final.

---

## Section 2 — Asset Folder Structure

```
thebeatedrop-listings/
├── CLAUDE.md
├── the-beat-drop-brand-identity.md
├── Gold_Standard_Product_Listing.docx
├── Gold_Standard_Bundle_Listing.docx
├── Platform_Reference.xlsx
├── BATCH_LISTING.md
└── IMGs/
    ├── PLML1_PrettyLights/          ← one subfolder per listing, named [code-or-working-name]_[ShortName]
    │   ├── pretty-lights_blue_1.jpg
    │   ├── pretty-lights_blue_2.jpg
    │   ├── pretty-lights_white_1.jpg
    │   ├── pretty-lights_turquoise_1.jpg
    │   └── pretty-lights_multicolor_1.jpg
    └── PLYD1_PrettyLightsBundle/
        ├── pretty-lights-bundle_1.jpg
        └── pretty-lights-bundle_2.jpg
```

**Rules:**
- **One subfolder per listing** under `IMGs/`, named with the SKU/artist code if already known, otherwise a short working name matching the intake spec's "Artist / bundle name." Never drop images for multiple listings into a shared flat folder — there's no way to know which photo belongs to which product without asking.
- **Standard listings:** filenames should include the color (e.g. `pretty-lights_blue_1.jpg`), so image-to-variant assignment never requires opening every file to guess. Multiple photos of the same color get a trailing number.
- **Bundle listings:** no color to encode, so filenames just need to be product-identifiable — a short product-name prefix is enough.
- **Preserve original filenames otherwise** — only the folder placement and, for Standard listings, a color prefix are being added on top of whatever the source filenames already are.
- If a filename already exists in the target subfolder, append `_v2` before the extension (per CLAUDE.md's existing rule).

This directly replaces the current flat `IMGs/` folder, which today holds 6 unlabeled Pretty Lights photos with no way to tell which belong to the Standard listing (`PLML1`) versus the Bundle (`PLYD1`), or which color each shows.

---

## Section 3 — Step-by-Step Batch Execution

1. **Confirm inputs are current.** Spot-check that `CLAUDE.md`, both gold-standard `.docx` files, and `Platform_Reference.xlsx` don't look stale (recent edit dates, no obvious version drift). Don't re-derive anything from an older cached copy.
2. **Read the intake spec (Section 1).** Every listing needs Listing type, Product Type, and Collection(s) filled in. If something's missing, flag it once, up front, before starting the batch — see Section 1's last row.
3. **For each listing in the batch:**
   a. Pull images from its `IMGs/[subfolder]` per Section 2.
   b. Pull the correct gold-standard `.docx` (Standard or Bundle) and copy the structure verbatim per `CLAUDE.md`'s Product Description Format — never rephrase.
   c. Build the Shopify draft: title, SEO title/meta description, description body (HTML, bolded keywords), variants + pricing + SKUs, images + alt text, theme template, Shopify Category (always Hair Pins, Claws & Clips taxonomy), Product Type (`Artist Sprout` or `Festival Sprout` per the intake spec), Collection(s), and the four standing metafields (Material, Age group, Construction, Target gender — see Section 4).
   d. Generate Etsy tags per the Etsy Tag Strategy section (10 Always + 3 Rotate/Specific, no repeated first word).
   e. Run `CLAUDE.md`'s New Listing Checklist against the finished draft before moving to the next listing.
4. **Update `Platform_Reference.xlsx`** — Product Roster and SKU Convention tabs — for every listing in the batch, including a Notes entry for anything that used a documented default, looked off-convention, or otherwise deserves your attention. Don't silently drop the Notes column in the process.
5. **Package the batch.** First build-out of a batch → downloadable Word doc per `CLAUDE.md`'s Format rule. Revisions after that → inline corrections in chat, no regenerated doc.
6. **Hand off for review.** Every listing goes live as DRAFT only (Rule 1) — Claude drafts, a human publishes.

---

## Section 4 — Defaults CLAUDE.md Already Allows (used only when Section 1 leaves the field blank)

These are the *only* fields where a documented default already exists — everything else (which of the two Product Types applies, Collection, Listing type, Bundle pricing) has no universal default and must come from Section 1, stated per listing.

| Field | Default | Source |
|---|---|---|
| Standard pack structure | 1/10/20/30-Pack, all colors; Multicolor in 10/20/30 only | CLAUDE.md Pricing & Pack Sizes, Variant Rules |
| Standard pricing | Pricing Master table ($3 / $28 / $55 / $81) | CLAUDE.md Pricing & Pack Sizes |
| Standard inventory | 50 / 20 / 10 / 5 (1/10/20/30-Pack) | CLAUDE.md Pricing & Pack Sizes |
| Bundle inventory | 100 / 50 / 30 (10/20/30-Pack) | CLAUDE.md Bundle Listings |
| Fixed festivals (Standard) | Electric Forest, Lost Lands, Seven Stars | CLAUDE.md Product Description Format |
| SKU artist/bundle code | Auto-generated, 4 letters + versioning digit | CLAUDE.md SKU Convention |
| "(Bonus)" duplicate discount | 10% / 12.5% / 15% / 20% off source's live price (1/10/20/30-Pack) | CLAUDE.md Duplicate Discount Formula |
| Compare-at price | Blank, unless this is a `(Bonus)` duplicate | CLAUDE.md Pricing & Pack Sizes |
| Theme template | `gp-template-581878106541785827` | CLAUDE.md Store |
| Shopify Category (taxonomy) | Apparel & Accessories > Clothing Accessories > Hair Accessories > Hair Pins, Claws & Clips | CLAUDE.md Shopify Category & Collections |
| Metafields (every listing) | Material: Polylactic Acid (PLA), Plastic, Metal · Age group: Adults · Construction: Solid · Target gender: Unisex | CLAUDE.md Shopify Category & Collections |
| Product status | DRAFT, always | CLAUDE.md Rule 1 |

Nothing in this table overrides an explicit value given in Section 1 — it only fills gaps Section 1 leaves open.
