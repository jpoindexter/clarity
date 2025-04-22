import { Card, CardContent } from "@/components/ui/card";
import Tag from "@/components/ui/Tag";

type AgentTag = {
  id: string;
  label: string;
  type: "emotional" | "signal" | "meta" | "custom";
  severity?: "critical" | "high" | "medium" | "low" | "info";
  confidence?: number;
  importance?: number;
  source?: string;
  icon?: string;
  color_key?: string;
  client_visible?: boolean;
};

type Props = {
  title: string;
  summary: string;
  tags?: AgentTag[];
  time?: string;
  tone?: string;
  flags?: string[];
  status?: string; // ✅ added for degraded card rendering
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
              <Tag key={i}>{tag.label}</Tag>
            ))}
          </div> 
        )}
      </CardContent>
    </Card>
  ); 
}
