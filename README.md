# Real-Time Speech-to-Text R\&D Project

## Overview

This project is an experimental **real-time speech-to-text system** that combines **browser-based transcription** using the **Web Speech API** with **backend refinement** using **OpenAI’s Whisper model**. The main goal is to explore **low-latency transcription** while simultaneously improving accuracy with server-side processing.

---

## Features Implemented So Far

1. **Real-time speech capture in browser**:

   * Uses the **Web Speech API** for live transcription.
   * Displays what the user speaks instantly.
   * Measures **Web Speech API latency** for each transcription segment.

2. **Backend Whisper processing**:

   * A **FastAPI WebSocket server** receives transcripts from the browser.
   * Simulates **Whisper model latency** (can be replaced with real audio transcription).
   * Returns processed text along with **Whisper latency** to the frontend.

3. **UI / Frontend**:

   * Single page HTML interface.
   * **Three transcription boxes**:

     * **Common box**: shows the spoken content live.
     * **Web Speech API box**: shows real-time transcript with latency.
     * **Whisper box**: shows backend-refined transcript with latency.
   * Black background, white text boxes, and buttons for a clean interface.
   * Start/Stop buttons to control recording.

4. **Real-time streaming concept**:

   * Audio is captured continuously.
   * Transcripts are updated live in the browser.
   * Backend can refine transcripts asynchronously.

---

## Tech Stack

| Component              | Technology / Library                |
| ---------------------- | ----------------------------------- |
| Frontend               | HTML, CSS, JavaScript               |
| Browser Speech-to-Text | Web Speech API (SpeechRecognition)  |
| Backend API            | FastAPI, WebSockets                 |
| Speech-to-Text Model   | OpenAI Whisper                      |
| Audio Transmission     | Base64-encoded text (prototype)     |
| Environment            | Python 3.x, modern browser (Chrome) |

---

## Workflow Diagram

```
          +-----------------+
          |  User Microphone |
          +--------+--------+
                   |
                   v
          +-----------------+
          | Web Speech API  |
          | (Browser)       |
          +--------+--------+
                   |  Live transcript + Web Speech latency
                   v
         +--------------------+
         | Common Text Box     |
         +--------------------+
                   |
                   v
          +-----------------+
          | WebSocket to     |
          | FastAPI Backend  |
          +--------+--------+
                   |
                   v
          +-----------------+
          | Whisper Model    |
          | (Server-side)    |
          +--------+--------+
                   | Refined transcript + Whisper latency
                   v
          +-----------------+
          | Whisper Text Box |
          +-----------------+
```

---

## Current Workflow

1. User clicks **Start** on the webpage.
2. Browser starts **Web Speech API** recording.
3. Spoken content is immediately shown in the **common box**.
4. Each transcription segment is:

   * Updated in the **Web Speech API box** with latency.
   * Sent to the **FastAPI WebSocket backend** (base64 encoded).
5. Backend receives transcript and:

   * Measures **Whisper processing latency**.
   * Sends the refined text and latency back to the frontend.
6. Frontend updates the **Whisper box** with the processed text.

---

## How to Run Locally

### 1. Backend (FastAPI + Whisper)

```bash
# Install dependencies
pip install fastapi uvicorn whisper

# Run WebSocket server
uvicorn ws_whisper:app --reload --host 0.0.0.0 --port 8000
```

### 2. Frontend

* Open `index.html` in a modern browser (Chrome recommended).
* Click **Start** to begin live transcription.
* Click **Stop** to end the session.

---

## Next Steps / Future Improvements

* **Send real audio chunks** instead of text to Whisper for **true backend transcription**.
* **Combine Web Speech API + Whisper** in real-time for **live refined text**.
* Support **multiple languages and accents**.
* Display **timestamps** for each word or segment.
* Implement **noise suppression and audio preprocessing**.
* Deploy on a **web server** with proper latency measurements.

---

## Notes

* This project is **still in R\&D** and is a prototype.
* Latency values are currently **simulated for Whisper**; real audio transcription is not yet implemented.
* Frontend is optimized for **desktop browsers**.
