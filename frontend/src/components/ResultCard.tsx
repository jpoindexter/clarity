import { Card, CardContent } from "@/components/ui/card";
import Tag from "@/components/ui/Tag";

type Props = {
  title: string;
  summary: string;
  tags?: string[];
  time?: string;
  tone?: string;
  flags?: string[];
};

export default function ResultCard({ title, summary, tags = [], time }: Props) {
  return (
    <Card className="w-[300px] shrink-0">
      <CardContent className="p-4 space-y-2">
        {time && <div className="text-xs text-zinc-500">{time}</div>}
        <div className="font-medium">{title}</div>
        <div className="text-sm text-zinc-300">{summary}</div>
        {(tags?.length ?? 0) > 0 && (
          <div className="flex flex-wrap gap-2 text-xs text-zinc-400 pt-2">
            {tags.map((tag, i) => (
              <Tag key={i}>{tag}</Tag>
            ))}
          </div>
        )}
      </CardContent>
    </Card>
  );
} 
