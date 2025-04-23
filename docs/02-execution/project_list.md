# Clarity Build Tasks – MVP Execution Plan

## 🧠 Core Features to Build First

### 1. Explore Mode (Homepage)
- [ ] Query input field (search box)
- [ ] Suggested topics (optional chips)
- [ ] Route to `/timeline/:topic_id` on submission

### 2. Narrative Timeline View
- [ ] Route `/timeline/:topic_id`
- [ ] Fetch articles based on topic
- [ ] Display Narrative Summary at top
- [ ] Render scrollable ResultCards (title, source, tone, tags)
- [ ] Add risk indicator to each ResultCard
- [ ] Top bar filters: tone, rhetoric, manipulation risk
- [ ] Timeline slider (date filter / playback)

### 3. Investigation View
- [ ] Route `/investigation/:article_id`
- [ ] Show full AI output: tone, rhetoric, fallacies, rationale
- [ ] Visual display of manipulation score
- [ ] Optional comparison to similar articles

### 4. Ingest Layer
- [ ] Google News RSS fetch for queries
- [ ] Local DeepSeek agent for summarization and narrative scoring
- [ ] Assign `topic_id` and `topic_title` via zero-shot prompt

### 5. UI Framework
- [ ] Dark theme only
- [ ] Sidebar navigation: Explore, Timeline
- [ ] Top bar filter panel in Timeline view
- [ ] Layout components matching intelligence tools (Splunk, Palantir)
