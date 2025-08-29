# ws_whisper.py
from fastapi import FastAPI, WebSocket
from fastapi.middleware.cors import CORSMiddleware
import base64
import time
import whisper

app = FastAPI()

app.add_middleware(
    CORSMiddleware, allow_origins=["*"], allow_methods=["*"], allow_headers=["*"]
)

# Load Whisper once
model = whisper.load_model("base")

@app.websocket("/ws/speech")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    try:
        while True:
            data = await websocket.receive_text()
            # decode base64 transcript from browser
            text = base64.b64decode(data).decode("utf-8")
            print("Browser transcript:", text)

            # Measure Whisper latency (simulate with small audio if text only)
            # If you had audio, you would transcribe it here
            start_time = time.time()
            # For demo, just send text back; in real case, transcribe audio:
            # result = model.transcribe(audio_file)
            time.sleep(0.1)  # simulate processing
            end_time = time.time()
            latency_ms = (end_time - start_time) * 1000

            await websocket.send_json({"text": text, "whisper_latency_ms": latency_ms})
    except:
        print("Client disconnected")
