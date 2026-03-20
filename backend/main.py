from fastapi import FastAPI, UploadFile, File, Form, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
import os

load_dotenv()

from models.schemas import GapAnalysisResponse, RoadmapResponse, ScoreResponse, GapAnalysisRequest, RoadmapRequest, ScoreRequest
from services.ai_engine import extract_skills, generate_adaptive_roadmap
from services.scorer import calculate_readiness_score
from services.pdf_parser import extract_text_from_pdf

app = FastAPI(
    title="AlgoRangers API",
    description="AI-Adaptive Onboarding & Career Acceleration Engine API",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def home():
    return {"message": "Welcome to AlgoRangers API! Visit /docs for Swagger UI."}

@app.post("/parse-resume")
async def parse_resume(file: UploadFile = File(...)):
    """Extract skills from a Resume (PDF/Text)"""
    try:
        if file.filename.endswith(".pdf"):
            contents = await file.read()
            text = extract_text_from_pdf(contents)
        else:
            text = (await file.read()).decode("utf-8")
            
        skills = await extract_skills(text, is_resume=True)
        return {"skills": skills}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/parse-jd")
async def parse_jd(jd_text: str = Form(...)):
    """Extract skills from Job Description"""
    try:
        skills = await extract_skills(jd_text, is_resume=False)
        return {"skills": skills}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/analyze-gap", response_model=GapAnalysisResponse)
async def analyze_gap(request: GapAnalysisRequest):
    """Compare Resume skills vs JD skills"""
    r_set = {s.lower() for s in request.resume_skills}
    missing = [skill for skill in request.jd_skills if skill.lower() not in r_set]
    return GapAnalysisResponse(missing_skills=missing)

@app.post("/generate-roadmap", response_model=RoadmapResponse)
async def generate_roadmap(request: RoadmapRequest):
    """Generate adaptive learning roadmap"""
    try:
        roadmap_data = await generate_adaptive_roadmap(request.missing_skills, request.user_skills)
        return RoadmapResponse(**roadmap_data)
    except Exception as e:
        raise HTTPException(status_code=500, detail="Failed to generate roadmap: " + str(e))

@app.post("/get-score", response_model=ScoreResponse)
async def get_score(request: ScoreRequest):
    """Calculate interview readiness score"""
    score_data = calculate_readiness_score(request.resume_skills, request.jd_skills)
    return ScoreResponse(**score_data)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
