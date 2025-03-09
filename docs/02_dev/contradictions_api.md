# 🚀 Clarity Contradiction Detection API

## 📌 Overview
The **Clarity Contradiction Detection API** analyzes financial news articles to detect **semantic contradictions** and **sentiment-based contradictions** using **NLP models (Sentence Transformers, FinBERT).**

- **Endpoint:** `/api/v1/contradictions/detect`
- **Method:** `POST`
- **Content-Type:** `application/json`
- **Response Time:** ~150ms (optimized for batch processing)
- **Features:**
  - **Detects contradictions** based on **semantic similarity** (NLP embeddings).
  - **Flags financial bias & misinformation** using **FinBERT sentiment analysis.**
  - **Ranks contradictions** with a `contradiction_strength` score.
  - **Supports real-time API calls** with efficient batch processing.

---

## 📌 Request Format
Send a **JSON payload** with a list of financial articles.

### Example Request:
```json
{
  "articles": [
    {
      "source": "Bloomberg",
      "headline": "Market stability expected",
      "content": "Experts predict continued market stability."
    },
    {
      "source": "CNBC",
      "headline": "Market instability rising",
      "content": "Analysts report concerns over increasing volatility."
    },
    {
      "source": "Reuters",
      "headline": "Stock market surges",
      "content": "Tech stocks led a major rally."
    },
    {
      "source": "Financial Times",
      "headline": "Market downturn likely",
      "content": "Bearish signals indicate a likely market pullback."
    }
  ]
}
```

📌 **Optional Query Parameter:**
- **`min_similarity_threshold`** (Default: `0.5`) – Adjusts the sensitivity of contradiction detection.

---

## 📌 API Response Format
Returns a **structured JSON** with detected contradictions, financial misinformation, and metadata.

### Example Response:
```json
{
  "contradictions": [
    {
      "headline_1": "Market stability expected",
      "headline_2": "Market instability rising",
      "score": 0.550,
      "strength": 0.900,
      "type": "sentiment",
      "sentiment_1": "Positive",
      "sentiment_2": "Negative"
    },
    {
      "headline_1": "Market downturn likely",
      "headline_2": "Stock market surges",
      "score": 0.512,
      "strength": 0.900,
      "type": "sentiment",
      "sentiment_1": "Negative",
      "sentiment_2": "Positive"
    }
  ],
  "financial_misinformation": {
    "Market stability expected": {
      "label": "Positive",
      "score": 0.999
    },
    "Market instability rising": {
      "label": "Negative",
      "score": 1.000
    }
  },
  "metadata": {
    "processing_time": 0.153,
    "articles_analyzed": 4,
    "total_contradictions": 2
  }
}
```

---

## 📌 cURL Example for Testing
Use this command to test the API:
```bash
curl -X POST "http://127.0.0.1:8000/api/v1/contradictions/detect" \
     -H "Content-Type: application/json" \
     -d '{
       "articles": [
         {"source": "Bloomberg", "headline": "Market stability expected", "content": "Experts predict continued market stability."},
         {"source": "CNBC", "headline": "Market instability rising", "content": "Analysts report concerns over increasing volatility."}
       ]
     }'
```

---

## 📌 How Contradictions Are Determined
- **Semantic Contradictions:** Articles with similarity **below `0.55`** are flagged.
- **Sentiment Contradictions:** Articles with opposite FinBERT sentiment (`Positive` vs. `Negative`) are automatically flagged, even if similarity is higher.
- **Strength Score:** Ranges from **0.0 (weak) to 1.0 (strong)** to help rank contradictions.

---

### 🚀 Next Steps
✅ **Place this file in:** `/02_dev/docs/api/contradictions_api.md`  
✅ **Mark `CLA-173 - API Documentation` as Done in Linear**  
✅ **Begin Step 2: Work on Real-Time Monitoring (CLA-95)**  
