class MarketImpact(BaseModel):
    """Schema for predicting market impact of misinformation-driven events."""
    article_id: int
    predicted_impact: float  # % Change in stock price, volatility index, or risk metric
    confidence_score: float = Field(ge=0, le=1, description="Confidence in prediction")
    generated_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))