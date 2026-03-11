# YouTube Video Summarizer

Easily generate concise summaries and key points for any YouTube video!  
This tool extracts video metadata, fetches English transcripts, and uses Ollama to summarize the content—making it perfect for quick reviews or note-taking.

---

## ✨ Features

- **Extracts Video Title & Channel**  
  Automatically fetches the video's title and the publishing channel.

- **Fetches English Transcripts**  
  Retrieves and compiles English subtitles (if available) for accurate summarization.

- **Generates Summaries with Key Points**  
  Uses Ollama Model to produce a brief summary, bullet-pointed key points, and a conclusion—all in your chosen language.

---

## 🚀 Usage
**1. Install Dependencies**: `pip install -r requirements.txt`  
**2. Run**: `python main.py`

You will be prompted to enter:
- The YouTube video URL
- The language code for your summary (default: en for English)

## 🛠️ How It Works
- Extracts Video ID from your YouTube URL
- Fetches Title & Channel using BeautifulSoup
- Downloads English Transcripts with youtube-transcript-api
- Generates Summaries using OpenAI’s GPT models
  
## ⚠️ Requirements
- Python 3.7+
- OpenAI API Key
- All Python dependencies from requirements.txt

## 🤝 Contributions
Pull requests and issues are welcome!


