# Clarity Frontend Component Structure

## Objective

To establish a modular, scalable, and maintainable frontend architecture using Next.js, ensuring seamless integration with Clarity’s backend and AI models.

## Folder Structure

frontend/

│── 📂 src/ 

│   │── 📂 components/        # Reusable UI components
│   │   │── 📂 common/        # Buttons, modals, loaders
│   │   │── 📂 dashboard/     # News feed, AI analysis, charts
│   │   │── 📂 forms/         # Search bars, filters, input fields
│   │── 📂 pages/             # Next.js routing pages
│   │── 📂 hooks/             # Custom React hooks
│   │── 📂 utils/             # Utility functions & helper methods
│   │── 📂 context/           # Global state management (Zustand/Redux)
│   │── 📂 services/          # API calls & data fetching
│   │── 📂 styles/            # Tailwind CSS & global styles
│   │── 📂 assets/            # Images, icons, fonts

## Core Components

### Common Components

- Button – Standard, outlined, and icon buttons.
- Modal – Popups for alerts and confirmations.
- Loader – Spinners and skeleton loaders.
- Table – Reusable table component for structured data.

### Dashboard Components

- NewsFeed – Displays AI-analyzed articles.
- ContradictionAnalysis – Highlights conflicting narratives.
- SentimentGraph – Visualizes sentiment trends over time.
- MarketImpact – Shows AI-driven financial impact predictions.

### Forms & Filters

- SearchBar – Filters news based on keywords.
- CategoryFilter – Dropdown for filtering topics.
- DateRangePicker – Select date ranges for analysis.
- UserPreferences – Allows customization of dashboard settings.

## State Management & API Calls

### State Management

- Stores global UI states (e.g., theme, user settings).
- Manages API responses & caching.
- Handles real-time updates using WebSockets.

### API Services

- useFetchNews – Fetches latest news data.
- useFetchContradictions – Retrieves AI-detected contradictions.
- useFetchSentiment – Gets sentiment analysis results.
- useFetchMarketImpact – Calls AI for market predictions.

## Styling & UI Framework

- Tailwind CSS – Utility-first styling for rapid UI development.
- Dark Mode Support – Integrated with global theme context.
- Responsive Design – Fully optimized for mobile & desktop.

## Execution Priorities

- Implement folder structure & base components.
- Connect frontend with backend APIs.
- Ensure responsive & accessible UI.
- Optimize rendering for real-time updates.

## Next Steps

Set up core components & integrate API calls. Let’s execute.