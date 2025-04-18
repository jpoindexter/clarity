

 # UI Notes — Clarity Intelligence Platform
 
 This document tracks known frontend UI inconsistencies, visual alignment issues, and polish tasks that will be addressed in upcoming batches.
 
 ---
 
 ## 🧱 TimelineView Display Issues
 
 - Cards shown after ingest disappear if the tab is changed.
 - Timeline tab does not yet load from the `summarized_articles` database.
 - There is no "load more" or limit mechanism — ingest dumps all at once.
 - Cards vary significantly in height depending on summary length.
 - Links overflow card bounds if long (no `overflow-wrap` or `truncate`).
 
 ## 🎨 Visual Consistency
 
 - Tag chips are inconsistently sized and spaced.
 - Theme contrast is too low (gray on white is hard to read).
 - Text like “Here is the classification of the text:” is verbose and AI-sounding.
 - Colors don’t align with black/dark mode preview.
 - Some chips wrap to new lines while others overflow.
 
 ## 🧠 Recommendations
 
 - Normalize chip styles via shared component with consistent padding.
 - Clamp summary lines to 4–5 max.
 - Truncate or wrap long URLs inside cards.
 - Strip unnecessary classifier phrasing from the output.
 - Add tier badges (e.g. `via RSS summary`) to provide ingest transparency.
 - Create a `TimelineCard` subcomponent for easier visual isolation and reuse.