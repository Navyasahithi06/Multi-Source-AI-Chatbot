# Multi-Source-AI-Chatbot
# 🤖 Multi-Source AI Chatbot

An AI-powered chatbot that integrates multiple information sources into a single intelligent platform. The application enables users to interact with an AI assistant, summarize PDF documents, generate summaries from YouTube videos, and create AI-generated images through an intuitive and user-friendly interface.

---

# 📖 Project Overview

The **Multi-Source AI Chatbot** is a Streamlit-based web application that combines the capabilities of Large Language Models (LLMs), Natural Language Processing (NLP), document analysis, video transcript processing, and AI-powered image generation.

The application provides a unified environment where users can perform multiple AI-powered tasks without switching between different platforms. It delivers context-aware responses by integrating multiple data sources, making it suitable for learning, research, content summarization, and productivity.

---

# ✨ Key Features

* 💬 AI-powered conversational chatbot
* 📄 PDF document summarization
* 🎥 YouTube video summarization using transcripts
* 🖼️ AI image generation from text prompts
* 🔐 User Authentication (Login & Signup)
* 💾 Chat history storage using SQLite
* 🌐 Interactive Streamlit user interface
* 🌍 English & Telugu summary support
* 🔒 Secure API key management using `.env`
* ⚠️ Error handling for invalid PDFs, unavailable YouTube transcripts, API failures, and image generation errors

---

# 🛠️ Technology Stack

## 💻 Frontend

* Streamlit
* HTML (Streamlit Components)
* CSS (Custom Styling)

## ⚙️ Backend

* Python 3.x

## 🤖 Artificial Intelligence & APIs

* **Groq API**

  * Llama 3.1 8B Instant (Large Language Model)
* **Pollinations AI**

  * AI Image Generation
* Hugging Face Hub

## 📚 Natural Language Processing (NLP)

* LangChain
* YouTube Transcript API
* PyPDF
* Regular Expressions (Regex)

## 🗄️ Database

* SQLite

## 🔐 Authentication & Security

* User Authentication
* Environment Variables (.env)
* python-dotenv

## 📦 Python Libraries

* Streamlit
* Groq
* LangChain
* PyPDF
* youtube-transcript-api
* python-dotenv
* Requests
* Pillow
* huggingface_hub
* fal_client
* os
* re
* urllib.parse

## 🛠️ Development Tools

* Visual Studio Code
* Git
* GitHub
* Virtual Environment (venv)

---

# 📂 Project Structure

```text
MULTI_SOURCE_AI_CHATBOT/
│
├── app.py
├── auth.py
├── users.py
├── utils.py
├── database.db
├── requirements.txt
├── .env
├── generated_images/
├── outputs/
├── fonts/
└── README.md
```

---

# ⚙️ Installation Guide

## 1. Clone the Repository

```bash
git clone https://github.com/yourusername/MULTI_SOURCE_AI_CHATBOT.git
cd MULTI_SOURCE_AI_CHATBOT
```

## 2. Create a Virtual Environment

```bash
python -m venv .venv
```

## 3. Activate the Environment

### Windows

```bash
.venv\Scripts\activate
```

### Linux/macOS

```bash
source .venv/bin/activate
```

## 4. Install Dependencies

```bash
pip install -r requirements.txt
```

---

# 🔑 Configure Environment Variables

Create a `.env` file inside the project directory.

```env
GROQ_API_KEY=your_groq_api_key
HF_TOKEN=your_huggingface_token
```

---

# ▶️ Run the Application

```bash
streamlit run app.py
```

Open your browser and visit:

```text
http://localhost:8501
```

---

# 🚀 Application Workflow

1. Register or log in to the application.
2. Select one of the available AI features:

   * 💬 AI Chat
   * 📄 PDF Summarization
   * 🎥 YouTube Video Summarization
   * 🖼️ AI Image Generation
3. Enter your query, upload a PDF, paste a YouTube URL, or describe an image.
4. The application processes the request using the appropriate AI model and NLP techniques.
5. Results are displayed instantly through the Streamlit interface.
6. Chat history is securely stored in the SQLite database for future reference.

---

# 📸 Application Screenshots

### 🏠 Login Page

*Add Login Page Screenshot*

### 💬 AI Chat Interface

*Add AI Chat Screenshot*

### 📄 PDF Summarization

*Add PDF Summarization Screenshot*

### 🎥 YouTube Video Summarization

*Add YouTube Summarization Screenshot*

### 🖼️ AI Image Generation

*Add Image Generation Screenshot*

---

# 🎯 Project Highlights

* Multi-source AI platform with four integrated AI services
* Intelligent conversational chatbot using Groq Llama 3.1
* Automatic PDF document summarization
* YouTube transcript extraction and summarization
* AI-powered text-to-image generation
* User authentication with secure login and signup
* Persistent chat history using SQLite
* English and Telugu language support
* Responsive Streamlit interface
* Modular and scalable Python architecture
* Secure API key management using environment variables
* Comprehensive error handling and exception management

---

# 📌 Future Enhancements

* Multiple PDF upload support
* Voice-based interaction
* Speech-to-Text and Text-to-Speech integration
* Chat export to PDF and Word
* Dark Mode
* Multiple LLM support (OpenAI, Gemini, Claude, Mistral)
* Cloud database integration (MySQL/PostgreSQL)
* Docker containerization
* Deployment on Streamlit Cloud, Render, Railway, or AWS
* User profile management
* Conversation search functionality
* AI-powered document question answering

---

# 👩‍💻 Author

**Malladi Navya Sahithi**

Final Year B.Tech – Artificial Intelligence & Data Science

Aspiring Data Analyst | AI & Machine Learning Enthusiast

GitHub: https://github.com/Navyasahithi06

LinkedIn: https://www.linkedin.com/in/navyasahithi
