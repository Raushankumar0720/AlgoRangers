def calculate_readiness_score(resume_skills: list[str], jd_skills: list[str]) -> dict:
    """Calculates interview readiness score based on skill overlap."""
    if not jd_skills:
        return {"score": 0, "reasoning": "No skills requested in Job Description."}
        
    resume_set = {s.lower() for s in resume_skills}
    jd_set = {s.lower() for s in jd_skills}
    
    matches = jd_set.intersection(resume_set)
    # Score out of 100 based on percentage of jd skills matched
    score = int((len(matches) / len(jd_set)) * 100) if len(jd_set) > 0 else 0
    
    reasoning = f"Matched {len(matches)} out of {len(jd_set)} required skills. Missing: {len(jd_skills) - len(matches)}."
    
    return {
        "score": score,
        "reasoning": reasoning
    }
