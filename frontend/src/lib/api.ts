export interface AgentTag {
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
}

export interface Article {
  id: string;
  title: string;
  summary: string;
  tags: AgentTag[];
  tone: string;
  contradictions: string[];
  source_url: string;
  published_at: string;
  status?: string; // ✅ added for degraded card support
}

export async function getArticles(limit = 50, sort: 'asc' | 'desc' = 'desc'): Promise<Article[]> {
  const query = new URLSearchParams({ limit: limit.toString(), sort });
  const res = await fetch(`http://localhost:8000/articles?${query.toString()}`);

  if (!res.ok) {
    console.error("Failed to fetch articles:", res.statusText);
    return [];
  }

  const data = await res.json();
  return data.articles ?? [];
}