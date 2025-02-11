import { useEffect, useState } from "react";
import { fetchNews } from "../utils/api";

export default function Home() {
  const [news, setNews] = useState([]);

  useEffect(() => {
    async function getNews() {
      const data = await fetchNews();
      setNews(data);
    }
    getNews();
  }, []);

  return (
    <div>
      <h1>Latest News</h1>
      {news.length > 0 ? (
        <ul>
          {news.map((article, index) => (
            <li key={index}>
              <h3>{article.title}</h3>
              <p>{article.summary}</p>
            </li>
          ))}
        </ul>
      ) : (
        <p>Loading news...</p>
      )}
    </div>
  );
}
