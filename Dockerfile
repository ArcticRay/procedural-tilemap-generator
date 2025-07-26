FROM python:3.11-slim AS base
WORKDIR /app
ENV PYTHONPATH=/app

RUN apt-get update \
 && apt-get install -y --no-install-recommends \
      build-essential python3-dev \
 && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Dev‑Stage 
FROM base AS dev
RUN pip install --no-cache-dir uvicorn[standard] watchdog
COPY app/    ./app
COPY tests/  ./tests
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80", "--reload"]

# Prod‑Stage 
FROM base AS prod
COPY app/ ./app

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]
