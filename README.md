# 🚀 AI-Adaptive Onboarding & Career Acceleration Engine

An intelligent system that analyzes a candidate’s resume against a target job description and generates a **personalized, adaptive learning roadmap**.

---

## 🎯 Problem Statement

Traditional onboarding systems are static and inefficient:

* Experienced users waste time
* Beginners feel overwhelmed

👉 Our solution creates a **dynamic, AI-driven personalized learning path**.

---

## 💡 Solution Overview

The system:

1. Extracts skills from Resume & JD
2. Identifies skill gaps
3. Validates skill levels
4. Generates adaptive roadmap
5. Provides reasoning
6. Calculates readiness score

---

## ⚙️ System Workflow

```
Resume + JD
     ↓
Skill Extraction
     ↓
Skill Gap Detection
     ↓
Confidence Scoring
     ↓
Adaptive Roadmap
     ↓
Reasoning + Output
```

---

# 👥 Team Structure & Responsibilities

## 🧠 Ankit (Backend + AI + Logic)

**Role:** System Brain (Core Intelligence)

### Responsibilities:

#### 🔹 Skill Extraction Engine

* Parse Resume & JD
* Extract and normalize skills

#### 🔹 Skill Gap Logic

```
Missing Skills = JD Skills - User Skills
```

#### 🔹 Confidence Scoring

* Skill frequency
* Project mentions
* Experience signals

#### 🔹 Adaptive Roadmap Generator

* Strong → Skip
* Medium → Revise
* Weak → Learn

#### 🔹 Reasoning Trace

* Explain WHY each step is added

#### 🔹 Interview Readiness Score

* Generate % score

#### 🔹 Backend APIs (FastAPI)

* `/parse-resume`
* `/parse-jd`
* `/analyze-gap`
* `/generate-roadmap`
* `/get-score`

#### 🔹 AI Integration

* Prompt design
* LLM usage
* Response formatting

---

## 💻 Raushan (Frontend + UI/UX + Integration)

**Role:** System Interface (User Experience)

### Responsibilities:

#### 🔹 UI Development (React)

* Upload Page
* Result Dashboard
* (Optional) Quiz Page

#### 🔹 File Upload System

* Resume upload
* JD input

#### 🔹 Result Visualization

Display:

* Extracted skills
* Missing skills
* Roadmap
* Readiness score

#### 🔹 Roadmap UI

* Step-by-step timeline
* Clean card layout

#### 🔹 API Integration

* Connect frontend with backend APIs

#### 🔹 Reasoning Display

* Expandable explanation section

#### 🔹 UX Enhancements

* Loading states
* Error handling
* Clean UI

---

# 🤝 Shared Responsibilities

### 🧪 Testing

* Beginner vs advanced cases
* Fake resume testing

---

### 🎥 Demo Video

* Ankit → backend logic
* Raushan → UI demo

---

### 📊 Presentation (5 Slides)

**Ankit:**

* Architecture
* Algorithm

**Raushan:**

* UI/UX
* User flow

---

### 📄 README Finalization

* Ankit → logic
* Raushan → formatting

---

## 🏗️ Tech Stack

Frontend:

* React.js

Backend:

* FastAPI (Python)

AI:

* OpenAI / LLM APIs

---

## 📂 Project Structure

```
project/
│
├── frontend/        # React UI (Raushan)
├── backend/         # FastAPI APIs (Ankit)
├── models/          # AI logic
├── data/            # Skill datasets
├── README.md
└── Dockerfile
```

---

## 🚀 Setup Instructions

### 🔧 Backend Setup (Ankit)

```
cd backend
pip install -r requirements.txt
uvicorn main:app --reload
```

---

### 💻 Frontend Setup (Raushan)

```
cd frontend
npm install
npm start
```

---

## 📥 Usage

1. Upload Resume
2. Upload / Paste JD
3. Click Analyze
4. View:

   * Skills
   * Missing skills
   * Roadmap
   * Reasoning

---

## 🧠 Core Logic

### Skill Gap

```
Missing = JD - Resume
```

### Adaptive Path

```
Strong → Skip  
Medium → Revise  
Weak → Learn  
```

---

## 🧪 Example Output

```json
{
  "missing_skills": ["React"],
  "roadmap": [
    {
      "step": 1,
      "title": "JS Advanced",
      "type": "revise"
    },
    {
      "step": 2,
      "title": "React Basics",
      "type": "learn"
    }
  ]
}
```

---

## 📅 Development Timeline

### Day 1

* Planning + setup

### Day 2

* Backend logic (Ankit)
* Basic UI (Raushan)

### Day 3

* API integration

### Day 4

* Add reasoning + score

### Day 5

* Testing + polish

### Day 6

* Demo + PPT

---

## 🏆 Final Goal

👉 Build a system that acts like:

**“An AI Mentor that understands a user’s skills and guides them step-by-step to job readiness.”**

---
