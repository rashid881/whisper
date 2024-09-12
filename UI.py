import streamlit as st
import whisper
import os

# Streamlit app title
st.title("Whisper Audio Transcription App")

# File uploader to upload the audio file
uploaded_file = st.file_uploader("Upload an audio file", type=["wav", "mp3", "m4a"])

# Dropdown to select the model size
model_option = st.selectbox(
    "Select Whisper Model",
    ["tiny", "base", "small", "medium", "large"]
)

# Path to save the uploaded audio
audio_path = "audio.wav"

if uploaded_file:
    # Save the uploaded audio file as audio.wav
    with open(audio_path, "wb") as f:
        f.write(uploaded_file.getbuffer())

    st.audio(uploaded_file, format="audio/wav")  # Display audio player
    
    # Process the audio with the selected model when user clicks the button
    if st.button("Transcribe Audio"):
        # Load the selected Whisper model
        st.write(f"Processing with '{model_option}' model...")
        model = whisper.load_model(model_option)
        
        # Transcribe the audio
        result = model.transcribe(audio_path)
        transcription = result['text']
        
        # Save the transcription to a text file
        output_file = "audio.txt"
        with open(output_file, "w") as f:
            f.write(transcription)
        
        # Display the transcription on the screen
        st.subheader("Transcription")
        st.write(transcription)
        
        # Download option for the transcription text file
        with open(output_file, "r") as f:
            st.download_button(
                label="Download transcription",
                data=f,
                file_name="audio.txt",
                mime="text/plain"
            )
