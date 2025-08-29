import streamlit as st
from audiorecorder import audiorecorder
import whisper
import tempfile
import time

st.title("🎤 Real-Time Speech to Text with Whisper")

# Load Whisper Model (base is smaller/faster; you can use "small", "medium", "large")
@st.cache_resource
def load_model():
    return whisper.load_model("base")

model = load_model()

# Record audio
st.subheader("Record Your Voice")
audio = audiorecorder("Click to Record", "Recording...")

if len(audio) > 0:
    st.audio(audio.export().read(), format="audio/wav")

    # Save to temp file
    with tempfile.NamedTemporaryFile(suffix=".wav", delete=False) as tmp_file:
        audio.export(tmp_file.name, format="wav")
        filepath = tmp_file.name

    st.success("Audio Recorded. Transcribing...")

    # Measure latency
    start_time = time.time()
    result = model.transcribe(filepath)
    end_time = time.time()

    latency = (end_time - start_time) * 1000  # in ms

    st.write("### Transcription:")
    st.write(result["text"])

    st.write(f"⏱️ Latency: {latency:.2f} ms")
