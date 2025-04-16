import streamlit as st
from app.audio_transcription import transcribe_audio
from app.nlp_feedback import analyze_text

st.title("🎤 AI Interview Coach")

audio_file = st.file_uploader("Upload audio", type=["mp3", "wav"])
if audio_file:
    with open("temp_audio.wav", "wb") as f:
        f.write(audio_file.read())
    text = transcribe_audio("temp_audio.wav")
    st.subheader("Transcription:")
    st.write(text)

    st.subheader("NLP Feedback:")
    feedback = analyze_text(text)
    st.json(feedback)