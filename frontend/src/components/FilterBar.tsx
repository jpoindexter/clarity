import React from "react";

type Filter = {
  tags?: string[];
  tone?: string | null;
  source?: string | null;
  rhetoric?: string[];
  manipulationRisk?: string | null;
};

type Props = {
  filters: Filter;
  onRemove: (key: keyof Filter, value: string) => void;
};

export default function FilterBar({ filters, onRemove }: Props) {
  return (
    <div className="flex flex-wrap gap-2 px-4 py-2 text-sm text-zinc-200">
      {filters.tags?.map(tag => (
        <span key={tag} className="bg-zinc-800 px-2 py-1 rounded-full flex items-center gap-1">
          {tag}
          <button onClick={() => onRemove("tags", tag)} className="text-zinc-400 hover:text-white">&times;</button>
        </span>
      ))}
      {filters.tone && (
        <span className="bg-zinc-800 px-2 py-1 rounded-full flex items-center gap-1">
          Tone: {filters.tone}
          <button onClick={() => onRemove("tone", filters.tone!)} className="text-zinc-400 hover:text-white">&times;</button>
        </span>
      )}
      {filters.source && (
        <span className="bg-zinc-800 px-2 py-1 rounded-full flex items-center gap-1">
          Source: {filters.source}
          <button onClick={() => onRemove("source", filters.source!)} className="text-zinc-400 hover:text-white">&times;</button>
        </span>
      )}
      {filters.rhetoric?.map(rhetoric => (
        <span key={rhetoric} className="bg-zinc-800 px-2 py-1 rounded-full flex items-center gap-1">
          Rhetoric: {rhetoric}
          <button onClick={() => onRemove("rhetoric", rhetoric)} className="text-zinc-400 hover:text-white">&times;</button>
        </span>
      ))}
      {filters.manipulationRisk && (
        <span className="bg-zinc-800 px-2 py-1 rounded-full flex items-center gap-1">
          Risk: {filters.manipulationRisk}
          <button onClick={() => onRemove("manipulationRisk", filters.manipulationRisk!)} className="text-zinc-400 hover:text-white">&times;</button>
        </span>
      )}
    </div>
  );
} 