import React, { useState, useEffect } from 'react';
import { getNews } from '../api/api';

function NewsList() {
  const [news, setNews] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    const loadNews = async () => {
      try {
        const fetchedNews = await getNews();
        setNews(fetchedNews);
      } catch (err) {
        setError(err);
      } finally {
        setLoading(false);
      }
    };

    loadNews();
  }, []);

  if (loading) {
    return <p>Loading news...</p>;
  }

  if (error) {
    return <p>Error: {error.message}</p>;
  }

  return (
    <ul>
      {news.map((item) => (
        <li key={item.id}>
          <h3>{item.title}</h3>
          <p>{item.content}</p>
        </li>
      ))}
    </ul>
  );
}

export default NewsList;
