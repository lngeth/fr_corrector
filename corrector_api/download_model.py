from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

model_name = "fdemelo/t5-base-spell-correction-fr"

tokenizer = AutoTokenizer.from_pretrained(
    model_name,
    use_fast=False
)
model = AutoModelForSeq2SeqLM.from_pretrained(model_name)

tokenizer.save_pretrained("./corrector_api/model")
model.save_pretrained("./corrector_api/model")