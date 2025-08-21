import speech_recognition as sr
from googletrans import Translator
from gtts import gTTS
import os
import base64

# Initialize recognizer & translator
recognizer = sr.Recognizer()
translator = Translator()

# Supported languages mapping
LANGUAGES = {
    "English": "en",
    "Telugu": "te",
    "French": "fr",
    "Spanish": "es",
    "Kannada": "kn"
}

# Speech-to-Text Function (Supports Telugu & English Input)
def speech_to_text(selected_language):  # Accept input language
    """Convert speech to text based on user-selected input language."""
    with sr.Microphone() as source:
        print(f"Listening in {selected_language}...")
        audio = recognizer.listen(source)

        try:
            if selected_language == "English":
                text = recognizer.recognize_google(audio, language="en-IN")  # English
            elif selected_language == "Telugu":
                text = recognizer.recognize_google(audio, language="te-IN")  # Telugu
            else:
                return "Invalid input language selected."

            print(f"Recognized Text: {text}")
            return text

        except sr.UnknownValueError:
            return "Sorry, could not understand the audio."
        except sr.RequestError:
            return "Speech recognition service is down."


# Translation Function (Supports English, Telugu, French, Spanish, Kannada)
def translate_text(text, input_language, target_language):
    translator = Translator()
    
    try:
        result = translator.translate(text, src=input_language, dest=target_language)
        translated_text = result.text  # Assign the translated text
        return translated_text  # Return the correctly assigned variable
    except Exception as e:
        print("Translation Error:", e)
        return "Translation failed"


# Text-to-Speech Function (Converts Translated Text to Speech)
import base64
import streamlit.components.v1 as components
from gtts import gTTS

def text_to_speech(text, language):
    if language not in LANGUAGES:
        return None

    tts = gTTS(text=text, lang=LANGUAGES[language], slow=False)
    audio_file = "output.mp3"
    tts.save(audio_file)

    # Read audio file and convert to base64
    with open(audio_file, "rb") as audio:
        encoded_audio = base64.b64encode(audio.read()).decode()

    # Auto-play audio in Streamlit
    audio_html = f"""
        <audio autoplay>
            <source src="data:audio/mp3;base64,{encoded_audio}" type="audio/mp3">
        </audio>
    """
    components.html(audio_html)

    return audio_file


if __name__ == "__main__":
    print("Backend is running... Speak now!")
    text = speech_to_text()
    print("Recognized:", text)
    translated = translate_text(text, "French")
    print("Translated:", translated)

