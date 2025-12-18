from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
from backend.final_assessments import recommend_assessments
app = FastAPI(
    title="SHL Assessment Recommender API",
    version="1.0",
)

@app.get("/health")
def health_check():
    return {"status": "ok"}

class RecommendRequest(BaseModel):
    query: str
    top_k: int = 10
class Recommendation(BaseModel):
    assessment_name: str
    test_type: str
    url: str

@app.post("/recommend", response_model=List[Recommendation])
def recommend(request: RecommendRequest):
    results = recommend_assessments(
        query=request.query,
        top_k=request.top_k
    )
    return results


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
