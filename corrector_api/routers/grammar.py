from fastapi import APIRouter
from corrector_api.models import TextRequest
from corrector_api.services.text_correction import correct_text

router = APIRouter()

@router.post("/correct_grammar_fr")
def correct_grammar_from_text_fr(request: TextRequest):
  corrected_text = correct_text(request.text)
  return {"corrected_text": corrected_text.text}