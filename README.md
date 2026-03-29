# NANDA arXiv Research Agent

An autonomous research agent registered on the [NANDA Index](https://projectnanda.org) — 
MIT's Internet of AI Agents infrastructure.

## What It Does

Given a research topic, this agent:
1. Fetches the latest abstracts from arXiv
2. Sends each abstract to Claude API for structured entity extraction
3. Returns enriched JSON with methods, datasets, key findings, and domain tags
4. Is globally discoverable via the NANDA index with cryptographically verified AgentFacts

## Tech Stack

- **Python** + **FastAPI** — agent logic and HTTP interface
- **Claude API (Haiku)** — LLM-powered structured extraction
- **NANDA Adapter SDK** — agent registration and AgentFacts
- **AWS EC2** — deployment

## API

### Health Check
```
GET /health
```

### Search
```
POST /search
{
  "topic": "multi-agent systems",
  "max_results": 3
}
```

## Setup
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
# Add your ANTHROPIC_API_KEY to .env
uvicorn main:app --reload
```

## Part of a Larger Vision

This agent is the ingestion layer of a broader LLM-powered ETL pipeline — 
demonstrating how NANDA's identity and discovery infrastructure enables 
trust-aware collaboration between autonomous agents.