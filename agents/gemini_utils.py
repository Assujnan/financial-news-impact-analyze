
from pydantic import BaseModel
from pydantic_ai import Agent
from pydantic_ai.providers.google_gla import GoogleGLAProvider
from pydantic_ai.models.gemini import GeminiModel
import os

# Shared Output Schemas

class SentimentOutput(BaseModel):
    sentiment: str  # "Positive", "Negative", "Neutral"
    confidence: float  # 0.0 - 1.0

class EventImpactOutput(BaseModel):
    event_type: str  # e.g. "Earnings Beat", "Product Launch"
    impact_score: float  # 0.0 - 1.0

class CoordinatorOutput(BaseModel):
    final_assessment: str  # e.g., "Moderately Positive market reaction expected."
    reasoning: str  # short justification for decision


def build_agent(prompt: str, output_model: type[BaseModel]) -> Agent:
     api_key = os.getenv("GEMINI_API_KEY")
     if not api_key:
        raise RuntimeError("❌ GEMINI_API_KEY is not set in environment!")

     provider = GoogleGLAProvider(api_key=api_key)
    
     model = GeminiModel("gemini-2.0-flash", provider="google-gla")
     return Agent(
        model=model,
        output_type=output_model,
        system_prompt=prompt.strip()
    )
