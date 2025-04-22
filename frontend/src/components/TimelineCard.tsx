"use client";

import React from "react";

interface AgentTag {
  id: string;
  label: string;
  type: "emotional" | "signal" | "meta" | "custom";
  severity?: "critical" | "high" | "medium" | "low" | "info";
  confidence?: number;
  importance?: number;
  icon?: string;
  source?: string;
  color_key?: string;
  client_visible?: boolean;
}

interface TimelineCardProps {
  title: string;
  summary: string;
  tags?: AgentTag[] | null;
  time: string;
  status?: string;
}

function getTagColor(tag: AgentTag): string {
  if (tag.color_key) {
    const map: Record<string, string> = {
      "severity:critical:signal": "hsl(0, 80%, 50%)",
      "severity:high:signal": "hsl(10, 80%, 55%)",
      "severity:medium:signal": "hsl(40, 80%, 50%)",
      "severity:info:meta": "hsl(210, 60%, 60%)",
    };
    if (map[tag.color_key]) return map[tag.color_key];
  }
  const hash = Math.abs(Array.from(tag.id).reduce((acc, char) => char.charCodeAt(0) + ((acc << 5) - acc), 0)) % 360;
  return `hsl(${hash}, 65%, 50%)`;
}

function TagChip({ tag }: { tag: AgentTag }) {
  return (
    <span
      key={tag.id}
      className="text-xs px-2 py-0.5 rounded-md text-white whitespace-nowrap"
      style={{ backgroundColor: getTagColor(tag) }}
      title={`${tag.label}${tag.source ? ` • Agent: ${tag.source}` : ""}`}
    >
      {tag.icon ? `${tag.icon} ` : ""}
      {tag.label}
    </span>
  );
}

export default function TimelineCard({ title, summary, tags, time, status }: TimelineCardProps) {
  const visibleTags = (tags || []).filter((tag) => tag.client_visible !== false).slice(0, 4);

  return (
    <div className={`w-80 rounded-lg shadow-sm p-4 flex flex-col justify-between ${status === "degraded" ? "bg-muted opacity-70 border border-yellow-300" : "bg-card"}`}>
      {status === "degraded" && (
        <div className="mb-1">
          <span className="inline-block text-xs font-medium bg-yellow-500 text-black px-2 py-0.5 rounded-md">
            ⚠️ Fallback Article
          </span>
        </div>
      )}
      <div className="mb-3">
        <h3 className="text-base font-semibold leading-snug line-clamp-2">{title}</h3>
        <p className="text-sm text-muted-foreground mt-1 line-clamp-4">{summary}</p>
      </div>
      <div className="flex flex-wrap gap-1 mb-2">
        {visibleTags.map((tag) => (
          <TagChip key={tag.id} tag={tag} />
        ))}
      </div>
      <div className="text-xs text-muted-foreground mt-auto truncate">
        {new Date(time).toLocaleDateString()}
      </div>
    </div>
  );
}