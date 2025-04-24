export interface ArticleSearchResult {
  title: string
  summary: string
  date: string
  source: string
  tone?: string
  manipulation_risk?: number
}

export interface ArticleSearchResponse {
  articles: ArticleSearchResult[]
  total_count: number
}