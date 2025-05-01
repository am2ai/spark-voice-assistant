# spark-voice-assistant

A modular, speech-powered assistant built using GPT, ElevenLabs, and LangGraph. Designed for simplicity, clarity, and future expansion.

## S.P.A.R.K. — Speech-Powered Agent for Reasoning & Knowledge

**S.P.A.R.K.** is a lightweight voice assistant prototype enabling natural conversation with AI through text and voice. It is structured for rapid interaction, modularity, and extensibility.

Built during the [Microsoft AI Agents Hackathon 2025](https://microsoft.github.io/AI_Agents_Hackathon/), the system demonstrates agentic flow control with:

- **OpenAI GPT-4o** — Language reasoning & dialogue
- **ElevenLabs** — Expressive voice synthesis
- **LangGraph** — Modular state graph for agent logic

> ⚠️ This is a prototype built for experimentation and learning. It is not a production system and requires API keys, Python setup, and **FFmpeg** installed for audio playback. Technical setup knowledge is assumed.

---

## 🔧 Features

- ✉️ Text-based AI assistant (powered by GPT-4o)
- 🎧 Natural voice replies using ElevenLabs
- 📂 Audio replies saved as `.wav` files in `voice_samples/`
- ⚖️ Modular agent logic via LangGraph
- ❄️ Graceful fallback to text-only output

---

## 📆 Technologies Used

| Tool         | Role                               |
|--------------|------------------------------------|
| OpenAI GPT-4o| Language model                     |
| ElevenLabs   | Text-to-speech voice generation   |
| LangGraph    | State management & agent logic    |
| Python       | Core language                     |
| Cursor IDE   | AI-native coding environment      |

---

## 🚀 Quick Start

### 🔑 Requirements
- Python 3.10+
- `.env` file with your OpenAI and ElevenLabs API keys
- **FFmpeg** must be installed and in your system PATH for audio playback to work:
  - [Download FFmpeg](https://ffmpeg.org/download.html)
  - Windows: extract ZIP → copy `bin/` folder path → add it to your system environment `PATH`
  - Linux/macOS: install via package manager (e.g., `brew install ffmpeg`)

### ⚒️ Setup
```bash
pip install -r requirements.txt
```

Create a `.env` file with:
```
OPENAI_API_KEY=your_openai_key
ELEVENLABS_API_KEY=your_elevenlabs_key
```

### ▶️ Run the Assistant
```bash
python src/main.py
```

You'll be prompted to type a message to the assistant. It will respond using GPT-4o and play the response aloud (if FFmpeg is installed).

All replies are also saved as `.wav` audio files in the `assets/voice_samples/` folder.

Type `exit` to quit.

---

## 📁 Project Structure
```
spark-voice-assistant/
├── src/
│   ├── main.py             # Entry point
│   ├── graph.py            # LangGraph agent logic
│   └── voice.py            # ElevenLabs interface
├── assets/
│   └── voice_samples/      # Auto-saved audio outputs (recommended: add to .gitignore)
├── .env.example            # API key template
├── requirements.txt
├── README.md
```

---

## 🎥 Demo Video
Submitted privately via Microsoft AI Agents Hackathon platform.

---

## 📄 Submission Note
S.P.A.R.K. was designed and submitted solo by @am2ai in under 12 hours.

> This is a **prototype** created for educational and hackathon purposes. While functional, it is a base for future exploration and experimentation.

---

## 📌 Future Enhancements (Optional)
- Integration with Notion or productivity tools
- Memory & personalization
- Web or mobile interface
- Long-form multi-turn memory

Not part of current submission, but design allows for easy evolution.

---

✨ Thank you for reviewing S.P.A.R.K. Let it ignite your curiosity.