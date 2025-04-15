"use client";

type Props = {
  availableTags: string[];
  selectedTags: string[];
  onChange: (tags: string[]) => void;
};

export default function TagFilterBar({ availableTags, selectedTags, onChange }: Props) {
  const toggleTag = (tag: string) => {
    if (selectedTags.includes(tag)) {
      onChange(selectedTags.filter((t) => t !== tag));
    } else {
      onChange([...selectedTags, tag]);
    }
  };

  return (
    <div className="flex gap-2 overflow-x-auto py-2">
      {availableTags.map((tag) => {
        const active = selectedTags.includes(tag);
        return (
          <button
            key={tag}
            onClick={() => toggleTag(tag)}
            className={`px-3 py-1 rounded text-xs border transition ${
              active
                ? "bg-zinc-800 border-zinc-500 text-white"
                : "bg-zinc-950 border-zinc-800 text-zinc-400 hover:text-white"
            }`}
          >
            {tag}
          </button>
        );
      })}
    </div>
  );
}