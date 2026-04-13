# Design System: The Compassionate Curator

## 1. Overview & Creative North Star
The Creative North Star for this design system is **"The Digital Sanctuary."** In the high-stakes world of cardiac health, the UI must act as a calming presence—a curated, editorial experience that replaces clinical coldness with tactile warmth.

We move beyond the "standard app" look by rejecting rigid grids and harsh dividers. Instead, the layout uses **intentional asymmetry** and **tonal depth**. By layering semi-transparent surfaces and utilizing wide "breathing room" (generous white space), we create a sense of professional serenity. This isn't just an interface; it’s a digital hand to hold.

---

## 2. Colors & Surface Philosophy
The palette is rooted in nature and comfort, utilizing the Material Design 3 token logic but elevated through custom tonal mapping.

### The Palette
- **Primary (Sage):** `#4b6552` – Used for growth, health, and primary actions.
- **Secondary (Teal):** `#3d6668` – Used for calm, stability, and secondary navigation.
- **Background (Warm Ivory):** `#faf9f6` – The foundation that ensures readability and a non-clinical feel.

### The "No-Line" Rule
**Standard 1px borders are strictly prohibited.** Sectioning must be achieved through:
1.  **Background Shifts:** Moving from `surface` to `surface-container-low`.
2.  **Tonal Transitions:** Using subtle shifts in the Ivory and Sage scales to define boundaries.

### The "Glass & Gradient" Rule
To achieve a "hyper-realistic" depth, use **Glassmorphism** for floating elements (like Bottom Sheets or Header Bars). Use the `surface-container-lowest` color at 70% opacity with a `24px` backdrop blur. 
*   **Signature Texture:** Main CTAs should use a subtle linear gradient from `primary` (#4b6552) to `primary_dim` (#3f5946) at a 135-degree angle to provide a soft, "pillowy" tactile feel.

---

## 3. Typography: Editorial Clarity
We use two distinct sans-serif families to balance authority with approachability.

*   **Display & Headlines (Plus Jakarta Sans):** Chosen for its modern, geometric clarity. High-end editorial layouts should use `display-lg` and `headline-md` with slightly tighter letter-spacing (-0.02em) to feel intentional and premium.
*   **Body & Labels (Lexend):** Specifically engineered for readability. The variable width of Lexend aids older patients in tracking lines of text, reducing cognitive load during stressful health monitoring.

**Hierarchy as Brand:** Use `title-lg` in `on_primary_container` for card headers to create a soft, professional contrast against the ivory background.

---

## 4. Elevation & Depth: The Layering Principle
Depth is not created by darkness, but by **Tonal Stacking**.

*   **Layering Hierarchy:**
    *   **Level 0 (Base):** `surface` (#faf9f6)
    *   **Level 1 (Section):** `surface-container-low` (#f4f4f0)
    *   **Level 2 (Card):** `surface-container-lowest` (#ffffff)
*   **Ambient Shadows:** For elevated elements, use a shadow with a `32px` blur, 0px Y-offset, and 6% opacity of the `on_surface` color (#303330). This mimics natural light diffusing through a room rather than a digital drop-shadow.
*   **The Ghost Border:** If a boundary is required for accessibility, use `outline-variant` (#b0b3ae) at **15% opacity**. It should be felt, not seen.

---

## 5. Components & UI Patterns

### Buttons
*   **Primary:** Rounded `full` (pill-shape). Uses the Sage gradient. Large touch targets (min 56dp height) for accessibility.
*   **Tertiary:** No background. Uses `primary` text with an icon. For low-emphasis actions like "Learn More."

### Cards & Lists
*   **The Divider Forbiddance:** Never use line dividers. Separate list items using `12px` of vertical whitespace or by placing each item in a `surface-container-low` rounded box with `xl` (1.5rem) corner radius.
*   **Glass Header:** Sticky top navigation should use the Glassmorphism rule to allow content to softly blur behind it as the user scrolls.

### Inputs
*   **Field Style:** Use `surface-container-high` backgrounds with no border. On focus, transition the background to `surface-container-highest` and add a subtle `primary` glow.
*   **Labels:** Always persistent. Never use floating labels that disappear, ensuring patients never lose context.

### Specialized Components
*   **Vitality Glow-Cards:** For heart rate or BP, use a `primary_container` card with a soft pulse animation (opacity shift 100% to 70%) to indicate "live" data.
*   **The "Buddy" Progress Ring:** A thick, soft-teal (`secondary`) stroke representing medication or goal completion, using `round` line-caps for a friendly, non-technical appearance.

---

## 6. Do’s and Don’ts

### Do
*   **Do** use `xl` (1.5rem) rounded corners for large containers to evoke "Soft UI" comfort.
*   **Do** prioritize high contrast (using `on_surface` on `surface`) for all medical data.
*   **Do** use iconography with a `2pt` stroke weight to ensure visibility for older users.

### Don’t
*   **Don’t** use pure black (#000000). Use `on_surface` (#303330) for a softer, more premium look.
*   **Don’t** use "Alert Red" for everything. Use `error_container` (#fa746f) for warnings to keep the user calm while still conveying urgency.
*   **Don’t** crowd the screen. If a screen feels full, move 20% of the content to a secondary "Info" sheet. Space is a luxury in healthcare.
