import streamlit as st
import backend  # Importing backend module for processing
import os
import base64

# ✅ **Set Page Configuration First**
st.set_page_config(page_title="Real-Time Speech Translator", layout="wide")

# Function to set background image
def set_background(image_path):
    with open(image_path, "rb") as img_file:
        encoded_string = base64.b64encode(img_file.read()).decode()

    st.markdown(f'''
        <style>
            .stApp {{
                background: url("data:image/jpeg;base64,{encoded_string}") no-repeat center center fixed;
                background-size: cover;
            }}
            /* Styling for the title box */
            .title-box {{
                background-color: rgba(34, 139, 34, 0.9); /* Green with transparency */
                padding: 20px;
                border-radius: 15px;
                text-align: center;
                font-size: 30px;
                font-weight: bold;
                color: white;
                width: 80%;
                margin: auto;
                margin-top: -10px; /* Reduce extra white space */
                box-shadow: 2px 2px 10px rgba(0, 0, 0, 0.3);
            }}
            /* Adjust font sizes and colors */
            .subheading {{
                font-size: 32px;  /* Increased font size */
                font-weight: bold;
                color: white;
                background-color: rgba(0, 0, 0, 0.6);
                padding: 10px;
                border-radius: 8px;
                text-align: center;
                width: 80%;
                margin: auto;
            }}
            .language-label {{
                font-size: 22px;
                font-weight: bold;
                color: white;
                background-color: rgba(0, 0, 0, 0.6);
                padding: 10px;
                border-radius: 8px;
                display: inline-block;
            }}
            div[data-testid="stSelectbox"] > div {{
                width: 80% !important;
                margin: auto;
            }}
            .stButton > button {{
                background-color: #4CAF50;
                color: white;
                font-size: 18px;
                padding: 12px 25px;
                border-radius: 10px;
                border: none;
                transition: 0.3s;
            }}
            .stButton > button:hover {{
                background-color: #388E3C;
                transform: scale(1.05);
            }}
        </style>
    ''', unsafe_allow_html=True)

# Set Background Image
background_image = "download.jpeg"
if os.path.exists(background_image):
    set_background(background_image)
else:
    st.warning("⚠ Background image not found! Please check the filename or path.")

# **Title Box**
st.markdown('<div class="title-box">🌍 Real-Time Speech Translator</div>', unsafe_allow_html=True)
st.write("\n")  # Add spacing

st.markdown('<p class="subheading">🎤 Speak in Telugu or English and get translations in multiple languages.</p>', unsafe_allow_html=True)

# Language Selection
st.markdown('<p class="language-label">Select your input language:</p>', unsafe_allow_html=True)
input_language = st.selectbox("", ["English", "Telugu"], key="input_language", help="Choose the language you will speak.")

st.markdown('<p class="language-label">Select your output language:</p>', unsafe_allow_html=True)
output_language = st.selectbox("", ["English", "Telugu", "French", "Spanish"], key="output_language", help="Choose the language for translation output.")

# Start Speaking Button
if st.button("Start Speaking 🎤"):
    try:
        original_text = backend.speech_to_text(input_language)  # Convert speech to text
        
        if original_text:
            translated_text = backend.translate_text(original_text, input_language, output_language)  # Translate text
            audio_file = backend.text_to_speech(translated_text, output_language)  # Convert translated text to speech

            # Display the results
            st.success(f"**You said ({input_language}):** {original_text}")
            st.info(f"**Translated ({output_language}):** {translated_text}")

            # Play audio output
            st.audio(audio_file, format='audio/mp3')
        else:
            st.warning("No speech detected. Please try again!")

    except Exception as e:
        st.error("⚠ An error occurred while processing your request.")
