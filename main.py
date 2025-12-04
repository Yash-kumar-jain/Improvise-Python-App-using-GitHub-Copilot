from fastapi import FastAPI
from input_text_model import InputTextModel
from checksum_util import generate_sha256_checksum

app = FastAPI()

@app.get("/")
def welcome():
    return {"message": "Welcome, Yash!"}

@app.post("/tokenize")
def tokenize_text(input: InputTextModel):
    checksum = generate_sha256_checksum(input.text)
    return {"checksum": checksum}