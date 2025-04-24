export interface EnrichedArticle {
  id: string;
  title: string;
  source: string;
  published_at: string;
  summary: string;
  tone: 'neutral' | 'supportive' | 'critical';
  rhetoric: string[];
  manipulation_score: number;
  summary_rationale: string;
  topic_id: string;
}