# Use official Python image
FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Copy requirements file if exists, else install from list
COPY requirements.txt .

# Install dependencies (ignoring errors if requirements.txt missing for some reason)
RUN pip install --no-cache-dir -r requirements.txt || true
RUN pip install fastapi uvicorn pydantic python-multipart pypdf2 docx2txt

# Copy backend source
COPY . .

# Expose port
EXPOSE 8000

# Run FastAPI server
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
