"use client";
import { useState } from "react";
import TimelineView from "@/components/TimelineView";
import TagFilterBar from "@/components/TagFilterBar";

const AVAILABLE_TAGS = [
  "economy",
  "security",
  "contradiction",
  "fear",
  "narrative", 
];

export default function TimelinePage() { 
  const [selectedTags, setSelectedTags] = useState<string[]>([]);

  return (
    <div className="space-y-6">
      <h1 className="text-2xl font-bold tracking-tight">Narrative Timeline</h1>
      <TagFilterBar
        availableTags={AVAILABLE_TAGS}
        selectedTags={selectedTags}
        onChange={setSelectedTags}
      />
      <TimelineView />
    </div>
  );
}