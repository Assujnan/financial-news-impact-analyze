import json
from schemas import NewsArticle

import os
from dotenv import load_dotenv

load_dotenv()


from agents.sentiment_agent import run_sentiment_agent
from agents.event_impact_agent import run_event_impact_agent
from agents.coordinator_agent import run_coordinator_agent


INPUT_PATH = "data/test_cases.json"

def analyze_article(article_json: dict):
    article = NewsArticle(**article_json)
    sentiment = run_sentiment_agent(article)
    event_impact = run_event_impact_agent(article)
    final = run_coordinator_agent(sentiment, event_impact)

    return {
        "article_id": article.article_id,
        "sentiment": sentiment.model_dump(),
        "event_impact": event_impact.model_dump(),
        "final_impact": final.final_assessment 
    }

def main():
    with open(INPUT_PATH, "r") as f:
        articles = json.load(f)

    results = []
    for article in articles:
        result = analyze_article(article)
        print(json.dumps(result, indent=2))
        results.append(result)

    # Optionally write results to output file
    with open("output/results.json", "w") as f:
        json.dump(results, f, indent=2)

if __name__ == "__main__":
    main()
