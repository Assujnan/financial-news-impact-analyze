from pydantic import BaseModel

class NewsArticle(BaseModel):
    article_id: str
    headline: str
    content: str
    published_at: str

class SentimentOutput(BaseModel):
    sentiment: str  # "Positive", "Neutral", "Negative"
    confidence: float  # Between 0.0 and 1.0

class EventImpactOutput(BaseModel):
    event_type: str  # "Earnings Beat", "Recall", etc.
    impact_score: float  # Between 0.0 and 1.0

class FinalImpact(BaseModel):
    final_impact: str  # "High", "Medium", "Low"