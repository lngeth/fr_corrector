from happytransformer import HappyTextToText, TTSettings

# Charger depuis le dossier local
happy_tt = HappyTextToText(
    model_type="T5",
    model_name="t5-base",
    load_path="./corrector_api/model"
)
args = TTSettings(num_beams=5, min_length=1)

def correct_text(text: str) -> str:
  return happy_tt.generate_text(f"grammaire: {text}", args=args)