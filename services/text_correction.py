from happytransformer import HappyTextToText, TTSettings

happy_tt = HappyTextToText("T5", "fdemelo/t5-base-spell-correction-fr")
args = TTSettings(num_beams=5, min_length=1)

def correct_text(text: str) -> str:
  return happy_tt.generate_text(f"grammaire: {text}", args=args)