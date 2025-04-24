'use client';

import React, { useEffect, useState } from 'react';
import { useParams } from 'next/navigation';
import FilterBar from '@/components/FilterBar';
import ResultCard from '@/components/ResultCard';
import { EnrichedArticle } from '@/lib/types';

const API_BASE = process.env.NEXT_PUBLIC_API_BASE || '';

export default function TopicTimelinePage() {
  const { topic_id } = useParams();
  const [articles, setArticles] = useState<EnrichedArticle[]>([]);
  const [filters, setFilters] = useState({
    tone: null,
    rhetoric: [],
    manipulationRisk: null,
  });

  useEffect(() => {
    if (!topic_id) return;
    fetch(`${API_BASE}/timeline/${topic_id}`)
      .then(res => res.json())
      .then(data => setArticles(data))
      .catch(err => console.error('Failed to load timeline:', err));
  }, [topic_id]);

  const filteredArticles = articles.filter(article => {
    const toneMatch = !filters.tone || article.tone === filters.tone;
    const rhetoricMatch = filters.rhetoric.length === 0 || filters.rhetoric.every(r => article.rhetoric?.includes(r));
    const riskMatch =
      !filters.manipulationRisk ||
      (filters.manipulationRisk === "high" && article.manipulation_score >= 0.75) ||
      (filters.manipulationRisk === "medium" && article.manipulation_score >= 0.4 && article.manipulation_score < 0.75) ||
      (filters.manipulationRisk === "low" && article.manipulation_score < 0.4);

    return toneMatch && rhetoricMatch && riskMatch;
  });

  return (
    <>
      <FilterBar
        filters={filters}
        onRemove={(key, value) => {
          setFilters(prev => {
            if (key === "rhetoric") {
              return { ...prev, rhetoric: prev.rhetoric.filter(r => r !== value) };
            }
            return { ...prev, [key]: null };
          });
        }}
      />
      <div>
        {filteredArticles.map((article: EnrichedArticle) => (
          <ResultCard key={article.id} {...article} />
        ))}
      </div>
    </>
  );
} 