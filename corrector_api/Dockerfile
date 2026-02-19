FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app
RUN mkdir -p /app/corrector_api

RUN apt-get update && apt-get install -y \
    build-essential \
    git \
    curl \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt --extra-index-url https://download.pytorch.org/whl/cpu

COPY . /app/corrector_api/

RUN python corrector_api/download_model.py

CMD ["uvicorn", "corrector_api.main:app", "--host", "0.0.0.0", "--port", "8000"]