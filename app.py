import os
import whisper
from fastapi import FastAPI, UploadFile, File
from fastapi.responses import JSONResponse

app = FastAPI()
model = whisper.load_model("base")   # load once, reuse

UPLOAD_DIR = "recordings"
os.makedirs(UPLOAD_DIR, exist_ok=True)

@app.post("/upload/")
async def upload_audio(file: UploadFile = File(...)):
    # save uploaded file
    file_path = os.path.join(UPLOAD_DIR, file.filename)
    with open(file_path, "wb") as f:
        f.write(await file.read())

    # transcribe
    result = model.transcribe(file_path)

    return JSONResponse({"text": result["text"]})
