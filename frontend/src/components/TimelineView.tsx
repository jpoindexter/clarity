"use client"; 

import ResultCard from "@/components/ResultCard";

export default function TimelineView() {
  const mockData = [
    {
      title: "Article 1",
      summary: "This is a short summary about topic A.",
      time: "2025-04-10",
      tags: ["politics", "eu", "conflict"],
    },
    {
      title: "Article 2",
      summary: "A summary on narrative shift in economic policy.",
      time: "2025-04-11",
      tags: ["economy", "tax", "narrative"],
    },
    {
      title: "Article 3",
      summary: "Contradiction flagged between statements on migration.",
      time: "2025-04-12",
      tags: ["immigration", "contradiction", "security"],
    },
  ];

  return (
    <div className="overflow-x-auto py-4">
      <div className="flex gap-4 min-w-[800px]">
        {mockData.map((entry, i) => (
          <ResultCard
            key={i}
            title={entry.title}
            summary={entry.summary}
            tags={entry.tags}
            time={entry.time}
          />
        ))}
      </div>
    </div>
  );
}