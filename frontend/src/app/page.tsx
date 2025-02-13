"use client";

import { useEffect, useState } from "react";

type NewsArticle = {
  id: number;
  title: string;
  summary: string;
};

export default function Home() {
  const [news, setNews] = useState<NewsArticle[]>([]);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    fetch("http://127.0.0.1:8000/api/news")  // ✅ Ensure correct endpoint
      .then((response) => response.json())
      .then((data) => {
        console.log("Fetched news data:", data);  // ✅ Debugging log
        if (Array.isArray(data)) {
          setNews(data);
        } else {
          setError("Invalid data format received");
          console.error("Unexpected API response:", data);
        }
      })
      .catch((error) => {
        console.error("Error fetching news:", error);
        setError("Failed to fetch news");
      });
  }, []);

  return (
    <div>
      <main style={{ textAlign: "center", padding: "20px" }}>
        <h1>Clarity News</h1>
        <p>Latest news articles:</p>
        {error ? <p style={{ color: "red" }}>{error}</p> : null}
        <ul style={{ listStyleType: "none", padding: 0 }}>
          {news.map((article) => (
            <li key={article.id} style={{ marginBottom: "20px" }}>
              <h3>{article.title}</h3>
              <p>{article.summary}</p>
            </li>
          ))}
        </ul>
      </main>
    </div>
  );
}
