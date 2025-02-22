class Summary(BaseModel):
    """Schema for AI-generated article summaries."""
    article_id: int
    summary: str
    keywords: list[str]
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))