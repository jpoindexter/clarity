 
 # 🧠 AI Agent Tagging Strategy — Clarity
 
 Clarity uses a multi-agent system to generate structured metadata tags for each ingested content item. These tags are then ranked, filtered, and displayed in the frontend.
 
 ---
 
 ## ✅ Agent Responsibilities
 
 Each AI agent (e.g. `summary_agent`, `contradiction_agent`, `threat_agent`, etc.) is responsible for:
 
 - Analyzing the content according to its domain logic
 - Emitting zero or more structured tag objects (see below)
 - Including a confidence score (0.0–1.0)
 - Assigning severity, type, and label where applicable
 
 ---
 
 ## 🧱 AgentTag Schema
 
 Agents return a list of structured tag objects:
 
 ```ts
 interface AgentTag {
   id: string;                         // e.g. "contradiction", "fud", "meta:longform"
   label: string;                      // Human label for UI display
   type: "emotional" | "signal" | "meta" | "custom";
   agent?: string;                     // Identifier of source agent
   importance?: number;               // Pre-ranked importance (0–100)
   severity?: "critical" | "high" | "medium" | "low" | "info";
   confidence?: number;               // Optional float between 0.0 and 1.0
   color_key?: string;                // Optional: backend-derived style key
   icon?: string;                     // Optional emoji or icon name
   client_visible?: boolean;          // Should this tag appear to users?
   raw_value?: any;                   // Full agent output, unstructured
 }
 ```
 
 ---
 
 ## 🔄 Tag Lifecycle
 
 1. **Generation** (agent): Agent analyzes content and emits `AgentTag[]`.
 2. **Standardization** (processor): Backend validates, normalizes, maps colors, filters.
 3. **Override logic**: Domain/client overrides are applied.
 4. **UI pass**: Ranked and styled tags are handed off to the frontend for display.
 
 ---
 
 ## 🎨 Agent Best Practices
 
 - Assign severity carefully: only critical tags should stand out visually.
 - Use known `type` values: emotional, signal, meta, custom.
 - Provide an `icon` if it helps differentiate agent signals.
 - Do not hardcode colors — the backend handles styling centrally.
 
 ---
 
 ## 🚫 Anti-Patterns
 
 - ❌ Do not emit tags as plain strings
 - ❌ Do not bypass the processor pipeline
 - ❌ Avoid flooding content with low-signal tags
 
 ---
 
 Agents should strive to produce clear, minimal, and highly ranked signals that guide user attention.