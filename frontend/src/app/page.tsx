"use client";

import { useEffect, useState } from "react";

type NewsArticle = {
  id: number;
  title: string;
  summary: string;
};

export default function Home() {
  const [news, setNews] = useState<NewsArticle[]>([]);

  useEffect(() => {
    fetch("http://127.0.0.1:8000/api/news")
      .then((response) => response.json())
      .then((data) => setNews(data))
      .catch((error) => console.error("Error fetching news:", error));
  }, []);

  return (
    <div>
      <main style={{ textAlign: "center", padding: "20px" }}>
        <h1>Clairity News</h1>
        <p>Latest news articles:</p>
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
