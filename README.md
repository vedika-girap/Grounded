# Grounded

Async, multi-tenant hybrid RAG API with automated evaluation.


## Stack
FastAPI · Celery · Redis · PostgreSQL + pgvector · Ragas

## Quick start
​```bash
cp .env.example .env
docker compose up -d
uv sync
uv run pytest
​```

## Development
​```bash
uv run ruff check .
uv run mypy
uv run pre-commit run --all-files
​```

## Roadmap
- [ ] Ingestion pipeline
- [ ] Hybrid retrieval (vector + keyword)
- [ ] Multi-tenancy
- [ ] Evaluation harness