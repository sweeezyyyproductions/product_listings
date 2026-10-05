# Listing Build Prompt — Template

Copy everything inside the box below, fill in the `[brackets]`, and paste it into Claude Code from this folder, one prompt per product listing. Delete any line marked *(optional)* that you aren't using. Lines marked *(Standard)* or *(Bundle)* only apply to that listing type.

Before you send it, put the photos in `IMGs/[CODE]_[ShortName]/`. For Standard listings, include the color in every file name, e.g. `crankdat_yellow_1.jpg`.

---

```text
Build a new Shopify product listing following CLAUDE.md. Read CLAUDE.md, the-beat-drop-brand-identity.md, and the correct gold-standard .docx before starting. Save as DRAFT only. Do not publish.

LISTING TYPE: [Standard | Bundle]
ARTIST / BUNDLE NAME: [exact name as it should appear in copy]
DESIGN NAME: [e.g. "Logo", "Smiley Face"; leave blank if this is the artist's first/only design]
SHOPIFY PRODUCT TYPE: [Artist Sprout | Festival Sprout]
COLLECTION(S): [collection name(s)]
IMAGE FOLDER: IMGs/[CODE]_[ShortName]/

(Standard) COLORS: [Color 1, Color 2, Color 3; add Multicolor if offered]
(Standard) PACK STRUCTURE: Default
    (or describe, e.g. "Individual colors in 1-Pack only; Multicolor in 10/20/30-Pack only")
(Standard) PRICING: Default
(Bundle) PRICING: 10 Pack $[__] / 20 Pack $[__] / 30 Pack $[__]
(Bundle) THEME NOTES (optional): [venue swaps, festivals for the closing paragraph]

SKU CODE (optional): [e.g. CNKD4; leave blank to auto-generate]
DUPLICATE / BONUS (optional): [source listing + title marker, e.g. "Duplicate Crankdat Logo Rave Sprout, append (Bonus)"]
FOCUS KEYWORDS (optional): [keywords to prioritize in copy and Etsy tags]
RESEARCH LINK(S) (optional): [Spotify / official site / Insomniac profile]

When finished:
1. Run the New Listing Checklist in CLAUDE.md and fix anything that fails.
2. Update the Product Roster and SKU Convention tabs in Platform_Reference.xlsx.
3. Give me a build summary: product link, title, SKU code, variants with prices and SKUs, Etsy tags, and anything that used a default or looked off-convention.
```

---

## Filled-in example (Standard)

```text
Build a new Shopify product listing following CLAUDE.md. Read CLAUDE.md, the-beat-drop-brand-identity.md, and the correct gold-standard .docx before starting. Save as DRAFT only. Do not publish.

LISTING TYPE: Standard
ARTIST / BUNDLE NAME: Crankdat
DESIGN NAME: Logo
SHOPIFY PRODUCT TYPE: Artist Sprout
COLLECTION(S): Artist Sprouts
IMAGE FOLDER: IMGs/CNKD4_CrankdatLogo/

COLORS: Green, Pink, Purple, Multicolor
PACK STRUCTURE: Default
PRICING: Default

When finished:
1. Run the New Listing Checklist in CLAUDE.md and fix anything that fails.
2. Update the Product Roster and SKU Convention tabs in Platform_Reference.xlsx.
3. Give me a build summary: product link, title, SKU code, variants with prices and SKUs, Etsy tags, and anything that used a default or looked off-convention.
```

## Filled-in example (Bundle)

```text
Build a new Shopify product listing following CLAUDE.md. Read CLAUDE.md, the-beat-drop-brand-identity.md, and the correct gold-standard .docx before starting. Save as DRAFT only. Do not publish.

LISTING TYPE: Bundle
ARTIST / BUNDLE NAME: Seven Stars Kandi Bundle
SHOPIFY PRODUCT TYPE: Festival Sprout
COLLECTION(S): Festival Bundles
IMAGE FOLDER: IMGs/SSKB1_SevenStarsKandi/

PRICING: 10 Pack $[__] / 20 Pack $[__] / 30 Pack $[__]
THEME NOTES: Camping festival; keep camping references. Closing paragraph: Seven Stars, Lost Lands.

When finished:
1. Run the New Listing Checklist in CLAUDE.md and fix anything that fails.
2. Update the Product Roster and SKU Convention tabs in Platform_Reference.xlsx.
3. Give me a build summary: product link, title, SKU code, variants with prices and SKUs, Etsy tags, and anything that used a default or looked off-convention.
```

*The examples are for format only. Don't send them as-is: CNKD4 and the collection names are placeholders.*
