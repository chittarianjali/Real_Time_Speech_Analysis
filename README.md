# 🎙️ Real-time Speech Translator

This project is a **Real-time Speech Translation System** that:

* Captures **speech input** (English/Telugu) 🎤
* Converts it into **text** using Google Speech Recognition ✍️
* Translates the recognized text into multiple target languages 🌍 (English, Telugu, French, Spanish, Kannada)
* Converts the translated text back into **speech** using Google Text-to-Speech (gTTS) 🔊
* Plays the translated speech directly in the interface 🚀

---

## ✨ Features

* 🎧 **Speech-to-Text**: Supports input in **English** and **Telugu**.
* 🌐 **Translation**: Translates into **English, Telugu, French, Spanish, Kannada**.
* 🔊 **Text-to-Speech**: Generates audio output (`output.mp3`) for the translated text.
* ⚡ **Streamlit Integration**: Auto-plays the translated audio in a web interface.

---

## 📂 Project Structure

```
.
├── backend.py          # Backend logic (speech recognition, translation, text-to-speech)
├── frontend.py         # (Optional) Streamlit UI
├── utils.py            # Helper functions
├── models/             # Placeholder for ML/translation models
├── requirements.txt    # Dependencies
├── output.mp3          # Generated audio output
└── download.jpeg       # Sample image (test file)
```

---

## 🛠️ Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/realtime-speech-translator.git
   cd realtime-speech-translator
   ```

2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

---

## 🚀 Usage

1. Run the backend:

   ```bash
   python backend.py
   ```

   You’ll see:

   ```
   Backend is running... Speak now!
   ```

2. Speak into your microphone in **English or Telugu**.

   * The app will transcribe your voice.
   * Translate the recognized text into your chosen language.
   * Generate and auto-play the translated speech.

3. (Optional) If `frontend.py` is Streamlit-based:

   ```bash
   streamlit run frontend.py
   ```

---

## ⚙️ Example

**Input (Telugu speech):**

```
నమస్కారం
```

**Recognized Text:**

```
Namaskaram
```

**Translated (French):**

```
Bonjour
```

**Output Speech:** 🎶 Auto-played in French

---

## 📦 Dependencies

* `speechrecognition` – Speech-to-text
* `googletrans==4.0.0-rc1` – Translation
* `gTTS` – Text-to-speech
* `streamlit` – UI framework
* `pyaudio` – Microphone support

---

## 🔮 Future Enhancements

* Support for more input languages
* Add a **frontend UI** for selecting input/output languages
* Display real-time translation logs on the web app


