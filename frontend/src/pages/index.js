import { useEffect, useState } from "react";
import { fetchNews } from "../services/api";

export default function Home() {
  const [news, setNews] = useState([]);

  useEffect(() => {
    fetchNews()
      .then(setNews)
      .catch((error) => console.error("Failed to load news", error));
  }, []);

  return (
    <div>
      <h1>Clairity News</h1>
      <ul>
        {news.map((article, index) => (
          <li key={index}>{article.title}</li>
        ))}
      </ul>
    </div>
  );
}
