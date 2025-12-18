# SHL Assessment Recommendation System (RAG-based)

## Overview
This project implements a Retrieval-Augmented Generation (RAG) based system to recommend suitable SHL assessments based on a natural language query or job description. The solution scrapes and processes the SHL product catalogue, stores assessment data in a vector database, and retrieves relevant assessments using semantic similarity and LLM-based reasoning.

---

## Key Features
- Scrapes and parses SHL product catalogue data (individual assessments only)
- Semantic search using sentence-transformer embeddings
- Vector-based retrieval for high-recall candidate selection
- Gemini LLM (`models/gemini-2.5-flash`) for context-aware recommendation generation
- FastAPI-based REST API
- Quantitative evaluation using Recall@10

---

## Architecture
1. **Data Ingestion**
   - Crawls SHL product catalogue
   - Extracts assessment name, test type, URL, and test type code
   - Ignores pre-packaged job solutions

2. **Embedding & Storage**
   - Converts assessment text into embeddings using a sentence-transformer model
   - Stores embeddings and metadata in a vector database

3. **Retrieval & Recommendation**
   - User query is embedded and matched against stored vectors
   - Top-N relevant assessments are retrieved
   - Retrieved context is passed to Gemini LLM for refined, structured recommendations

4. **API Layer**
   - Exposed via FastAPI
   - Returns JSON responses

---

## API Endpoint

### GET Recommendation Endpoint


### Response Format (JSON)
```json
{
  "query": "Looking to hire mid-level professionals proficient in Python, SQL and JavaScript",
  "recommendations": [
    {
      "assessment_name": "Python Programming",
      "test_type": "Knowledge",
      "test_type_code": "K",
      "url": "https://www.shl.com/products/..."
    }
  ]
}
Evaluation

Evaluation metric: Mean Recall@10

Ground truth derived from training dataset

URL canonicalization applied to reduce false negatives

Retrieval depth increased to improve recall

Results:

Baseline Recall@10 ≈ 0.06

Improved Recall@10 in the range 0.24 – 0.29
Running the Application Locally
1. Install dependencies
pip install -r requirements.txt

2. Start the FastAPI server
uvicorn main:app --reload

3. Test the API

Open browser or Postman:

http://localhost:8000/recommend?query=<your_query>

Deployment Note

The application could not be deployed due to payment verification issues on the hosting platform. All components were fully implemented and tested locally. Screenshots of working outputs and evaluation results are included in the submission.

Tech Stack:
Python
FastAPI
Sentence-Transformers
Vector Database (Chroma)
Gemini LLM (models/gemini-2.5-flash)
Pandas