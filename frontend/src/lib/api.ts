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

export async function getArticles(
  filters?: { tags?: string[]; tone?: string | null; source?: string | null },
  limit = 50,
  sort: 'asc' | 'desc' = 'desc'
): Promise<Article[]> {
  const query = new URLSearchParams({ limit: limit.toString(), sort });

  if (filters?.tone) query.append("tone", filters.tone);
  if (filters?.source) query.append("source", filters.source);
  filters?.tags?.forEach(tag => query.append("tag", tag));

  const res = await fetch(`http://localhost:8000/articles/?${query.toString()}`);

  if (!res.ok) {
    console.error("Failed to fetch articles:", res.statusText);
    return [];
  }

  const data = await res.json();
  return data.articles ?? data ?? [];
}
export interface ArticleSearchResult {
  title: string;
  summary: string;
  date: string;
  source: string;
  tone?: string;
  manipulation_risk?: number;
}

export interface ArticleSearchResponse {
  articles: ArticleSearchResult[];
  total_count: number;
}

export async function searchArticles(params: {
  query: string;
  tone?: string;
  source?: string;
  limit?: number;
  offset?: number;
}): Promise<ArticleSearchResponse> {
  const queryParams = new URLSearchParams();
  queryParams.append("query", params.query);
  if (params.tone) queryParams.append("tone", params.tone);
  if (params.source) queryParams.append("source", params.source);
  if (params.limit !== undefined) queryParams.append("limit", params.limit.toString());
  if (params.offset !== undefined) queryParams.append("offset", params.offset.toString());

  const res = await fetch(`/articles?${queryParams.toString()}`);
  if (!res.ok) {
    console.error("Failed to search articles:", res.statusText);
    return { articles: [], total_count: 0 };
  }

  const data = await res.json();
  return {
    articles: data.articles ?? [],
    total_count: data.total_count ?? 0,
  };
}