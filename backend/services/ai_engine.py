import os
from openai import AsyncOpenAI
import json

client = AsyncOpenAI(api_key=os.getenv("OPENAI_API_KEY"))

async def extract_skills(text: str, is_resume: bool = True) -> list[str]:
    """Extract skills from Resume or JD text using OpenAI."""
    doc_type = "resume" if is_resume else "job description"
    prompt = f"""
    You are an expert technical recruiter. Extract a clean, comma-separated list of technical and soft skills from the following {doc_type}:
    
    TEXT:
    {text}
    
    Return ONLY a comma-separated list of skills, nothing else. If none found, return an empty string.
    """
    
    try:
        response = await client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "user", "content": prompt}
            ],
            temperature=0.2
        )
        content = response.choices[0].message.content or ""
        skills = [s.strip() for s in content.split(",") if s.strip()]
        return skills
    except Exception as e:
        print(f"OpenAI error extracting skills: {e}")
        return []

async def generate_adaptive_roadmap(missing_skills: list[str], user_skills: list[str]) -> dict:
    """Generate an adaptive learning roadmap based on missing skills."""
    prompt = f"""
    You are an AI career mentor. Generate a personalized, adaptive learning roadmap.
    
    User already has these skills (Strong): {', '.join(user_skills)}
    User missing these skills for the target job (Weak): {', '.join(missing_skills)}
    
    Create a step-by-step roadmap. 
    - For each missing skill, assign it type 'learn'. 
    - You can also add steps with type 'revise' for skills the user has but should review.
    - Omit 'skip' steps unless they add clarity.
    
    Return pure JSON with the following structure exactly:
    {{
      "roadmap": [
        {{
          "step": 1,
          "title": "Skill/Topic Name",
          "type": "learn", 
          "reasoning": "Why the user needs this"
        }}
      ]
    }}
    """
    
    try:
        response = await client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "user", "content": prompt}
            ],
            temperature=0.4,
            response_format={"type": "json_object"}
        )
        content = response.choices[0].message.content
        return json.loads(content)
    except Exception as e:
        print(f"OpenAI error generating roadmap: {e}")
        return {"roadmap": []}
