"use client";

import { Card, CardContent } from "@/components/ui/card";

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
          <Card key={i} className="w-[300px] shrink-0">
            <CardContent className="p-4 space-y-2">
              <div className="text-xs text-zinc-500">{entry.time}</div>
              <div className="font-medium">{entry.title}</div>
              <div className="text-sm text-zinc-300">{entry.summary}</div>
              <div className="flex flex-wrap gap-2 text-xs text-zinc-400 pt-2">
                {entry.tags.map((tag, j) => (
                  <span
                    key={j}
                    className="border border-zinc-700 px-2 py-0.5 rounded bg-zinc-900"
                  >
                    {tag}
                  </span>
                ))}
              </div>
            </CardContent>
          </Card>
        ))}
      </div>
    </div>
  );
}