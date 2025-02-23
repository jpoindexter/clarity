from datetime import datetime, timezone

from pydantic import BaseModel, Field


class Metadata(BaseModel):
    """Schema for storing AI-generated metadata (bias, credibility, topic classification)."""

    article_id: int
    credibility_score: float = Field(
        ge=0, le=1, description="0=low credibility, 1=high credibility"
    )
    bias_score: float = Field(ge=-1, le=1, description="-1=left bias, 1=right bias")
    topics: list[str]
    generated_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
