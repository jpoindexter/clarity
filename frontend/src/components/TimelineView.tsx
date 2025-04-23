"use client";

import { useEffect, useState, useCallback } from "react";
import ResultCard from "@/components/ResultCard";
import { getArticles, Article } from "@/lib/api";
import FilterBar from "@/components/FilterBar";

export default function TimelineView() {
  const [articles, setArticles] = useState<Article[]>([]);
  const [loading, setLoading] = useState(true);

  const [filters, setFilters] = useState({
    tags: ["AI", "Politics"],
    tone: "Critical",
    source: "BBC"
  });

  const handleRemoveFilter = (key: keyof typeof filters, value: string) => {
    setFilters(prev => {
      if (key === "tags") {
        return { ...prev, tags: prev.tags?.filter(tag => tag !== value) };
      }
      return { ...prev, [key]: null };
    });
  };

  const fetchArticles = useCallback(async () => {
    try {
      setLoading(true);
      const data = await getArticles(filters);
      setArticles(data);
    } catch (error) {
      console.error("Failed to fetch articles", error);
    } finally {
      setLoading(false);
    }
  }, [filters]); 
 
  useEffect(() => {
    fetchArticles();
  }, [fetchArticles]);
 
  return (
    <div className="w-full px-4 py-6 overflow-y-auto">
      <div className="flex flex-col gap-6 max-w-3xl mx-auto">
        <FilterBar filters={filters} onRemove={handleRemoveFilter} />
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
              status={entry.status}
              tone={entry.tone}
            />
          ))
        )}
      </div>
    </div>
  );
}  