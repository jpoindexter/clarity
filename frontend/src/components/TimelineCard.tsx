"use client";

import React from "react";

interface TimelineCardProps {
  title: string;
  summary: string;
  tags?: string[] | null;
  time: string;
  tone?: string | null;
}

export default function TimelineCard({ title, summary, tags, time, tone }: TimelineCardProps) {
  const hasContradiction = tags?.includes("contradiction");

  return (
    <div className="w-80 bg-card rounded-lg shadow-sm p-4 flex flex-col justify-between">
      <div className="mb-3">
        {hasContradiction && (
          <span className="inline-block mb-1 text-xs font-semibold bg-red-600 text-white px-2 py-0.5 rounded-md">
            ⚠ Contradiction
          </span>
        )}
        <h3 className="text-base font-semibold leading-snug line-clamp-2">{title}</h3>
        {tone && (
          <span
            className="inline-block mt-1 text-xs font-medium px-2 py-0.5 rounded-md text-white"
            style={{
              backgroundColor: `hsl(${Math.abs(
                Array.from(tone).reduce((acc, char) => char.charCodeAt(0) + ((acc << 5) - acc), 0)
              ) % 360}, 70%, 50%)`,
            }}
          >
            {tone}
          </span>
        )}
        <p className="text-sm text-muted-foreground mt-1 line-clamp-4">{summary}</p>
      </div>
      <div className="flex flex-wrap gap-1 mb-2">
        {(tags || []).map((tag) => (
          <span
            key={tag}
            className="text-xs bg-muted text-muted-foreground px-2 py-0.5 rounded-md whitespace-nowrap"
          >
            {tag}
          </span>
        ))}
      </div>
      <div className="text-xs text-muted-foreground mt-auto truncate">
        {new Date(time).toLocaleDateString()}
      </div>
    </div>
  );
}