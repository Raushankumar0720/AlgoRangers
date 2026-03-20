from pydantic import BaseModel
from typing import List, Optional

class SkillExtractionResponse(BaseModel):
    skills: List[str]

class GapAnalysisRequest(BaseModel):
    resume_skills: List[str]
    jd_skills: List[str]

class GapAnalysisResponse(BaseModel):
    missing_skills: List[str]

class RoadmapStep(BaseModel):
    step: int
    title: str
    type: str
    reasoning: Optional[str] = None

class RoadmapRequest(BaseModel):
    missing_skills: List[str]
    user_skills: List[str]

class RoadmapResponse(BaseModel):
    roadmap: List[RoadmapStep]

class ScoreRequest(BaseModel):
    resume_skills: List[str]
    jd_skills: List[str]

class ScoreResponse(BaseModel):
    score: int
    reasoning: str
