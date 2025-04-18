"use client";

import { useEffect, useState } from "react";
import ResultCard from "@/components/ResultCard";
import { getArticles, Article } from "@/lib/api";

export default function TimelineView() {
  const [articles, setArticles] = useState<Article[]>([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    async function fetchData() {
      try {
        const data = await getArticles();
        setArticles(data);
      } catch (error) {
        console.error("Failed to fetch articles", error);
      } finally {
        setLoading(false);
      }
    }

    fetchData();
  }, []);

  return (
    <div className="overflow-x-auto py-4">
      <div className="flex gap-4 min-w-[800px]">
        {loading ? (
          <p className="text-muted">Loading articles...</p>
        ) : (
          articles.map((entry) => (
            <ResultCard
              key={entry.id}
              title={entry.title}
              summary={entry.summary}
              tags={entry.tags}
              time={entry.published_at}
            />
          ))
        )}
      </div>
    </div>
  );
}