import json
from collections import Counter
from typing import List

def load_results(path: str):
    with open(path, "r") as f:
        return json.load(f)

def compute_inter_agent_agreement(results: List[dict]) -> float:
    agree_count = 0
    for r in results:
        sentiment = r["sentiment"]["sentiment"]
        impact_score = r["event_impact"]["impact_score"]

        # Define agreement if both indicate same direction
        if sentiment == "Positive" and impact_score > 0.7:
            agree_count += 1
        elif sentiment == "Negative" and impact_score < 0.3:
            agree_count += 1
        elif sentiment == "Neutral" and 0.3 <= impact_score <= 0.7:
            agree_count += 1

    return agree_count / len(results)

def impact_distribution(results: List[dict]):
    dist = Counter([r["final_impact"] for r in results])
    return dict(dist)

def print_summary(results: List[dict]):
    print("===== Evaluation Summary =====")
    print(f"Total Articles Evaluated: {len(results)}")
    
    agreement_rate = compute_inter_agent_agreement(results)
    print(f"Inter-Agent Agreement Rate: {agreement_rate * 100:.2f}%")
    
    distribution = impact_distribution(results)
    print("Final Impact Distribution:", distribution)
