from fastapi import FastAPI
from corrector_api.models import TextRequest
from corrector_api.routers import grammar, api_health

title = "French Corrector API"
description = "API that use LLM from HuggingFace to correct spelling mistakes in French texts."

app = FastAPI(
  title=title,
  description=description
)

app.include_router(api_health.router)
app.include_router(grammar.router)