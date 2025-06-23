#  Financial News Impact Analyzer

A multi-agent system built using **Python**, **Pydantic**, and **Gemini**, designed to analyze financial news articles and generate structured insights into market sentiment and potential stock impact.

---

##  Overview

**Financial News Impact Analyzer** is a case study project that showcases the use of large language models and modular AI agents to evaluate financial news. Given a news headline and article body, the system performs:

- **Sentiment analysis**
- **Event classification**
- **Impact assessment**
- **Coordinated market impact synthesis**

All outputs follow strict `Pydantic`-typed JSON schemas to ensure consistency and validation.

---

##  System Architecture

         ┌────────────────────┐
         │ Financial News     │
         │ (Headline + Body)  │
         └────────┬───────────┘
                  │
                  ▼
   ┌──────────────────────────────┐
   │     Sentiment Agent          │
   │ Classifies Positive/Negative │
   └────────────┬─────────────────┘
                │
                ▼
   ┌──────────────────────────────┐
   │    Event Impact Agent        │
   │  Detects event + impact score│
   └────────────┬─────────────────┘
                │
                ▼
   ┌──────────────────────────────┐
   │    Coordinator Agent         │
   │ Merges outputs → final report│
   └──────────────────────────────┘


---

##  Agents and Their Roles

### 1. **Sentiment Agent**
- Determines sentiment: `"Positive"`, `"Negative"`, or `"Neutral"`
- Outputs a `confidence` score (0.0–1.0)
- Adds reasoning in natural language

### 2. **Event Impact Agent**
- Extracts the main financial event (e.g., `"Earnings Beat"`, `"Product Launch"`)
- Assigns an `impact_score` (0.0–1.0)
- Includes event-related justification

### 3. **Coordinator Agent**
- Synthesizes Sentiment and Event Agent outputs
- Produces:
  - A `market_impact_summary`
  - `overall_sentiment`
  - `combined_score`
  - Explanation of final judgment

---

##  Technologies Used

-  Python 3.10+
-  [Pydantic](https://docs.pydantic.dev/) for type validation
-  Google Gemini for LLM-powered analysis
-  JSON for structured agent communication

---

##  How to Run

```bash
git clone https://github.com/yourusername/financial-news-analyzer.git
cd financial-news-analyzer
pip install -r requirements.txt
python main.py


