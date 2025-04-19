 
 # 🧠 Clarity Frontend — Tag Display System
 
 This document defines how AI-generated metadata tags ("chips") are rendered in the Clarity frontend timeline.
 
 ---
 
 ## ✅ Tag Structure: `AgentTag` Object
 
 Clarity no longer uses `string[]` tags. All tags passed to the UI must follow this structured format:
 
 ```ts
 interface AgentTag {
   id: string;
   label: string;
   type: "emotional" | "signal" | "meta" | "custom";
   severity?: "critical" | "high" | "medium" | "low" | "info";
   confidence?: number;
   importance?: number;
   icon?: string;
   source?: string;
   color_key?: string;
   client_visible?: boolean;
 }
 ```
 
 ---
 
 ## 🎨 Color Strategy
 
 The frontend uses a `color_key` provided by the backend to map tags to a predefined Tailwind-compatible color palette.
 
 - If `tag.color_key` exists → map to a known color (e.g., `severity:high:signal` → red).
 - If missing → fallback to hash-generated HSL based on `tag.id`.
 
 ---
 
 ## 🧱 UI Rendering Rules
 
 1. **Tag display uses `TagChip` component**:
    - Background color comes from `getTagColor(tag)`
    - Label = `tag.label`
    - Tooltip shows: label + confidence + source (if available)
 
 2. **Only top N tags are shown per card**:
    - Tags are ranked by `importance` (or severity/confidence)
    - Max displayed = 3–5 (configurable)
    - If more tags exist, show a `+X more` chip
 
 3. **Chips are grouped and spaced cleanly**:
    - Chips wrap in a flex row
    - Secondary tags only revealed on click or hover
 
 ---
 
 ## 📦 Future-Proof
 
 This system allows:
 - Full white-label configuration
 - Agent-specific iconography and styling
 - Client-based suppression of low-value tags
 - Signal fusion support (e.g., multiple agents → single tag)
 
 ---
 
 For implementation details, see `/components/TagChip.tsx` and `/lib/getTagColor.ts`.