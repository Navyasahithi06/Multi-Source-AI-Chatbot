import fal_client
import os
import re
import requests
from urllib.parse import quote
from dotenv import load_dotenv
load_dotenv()

from groq import Groq
from pypdf import PdfReader

from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api._errors import VideoUnavailable, TranscriptsDisabled

from huggingface_hub import InferenceClient


# =========================
# GROQ CLIENT
# =========================
groq_client = Groq(api_key=os.getenv("GROQ_API_KEY"))
from dotenv import load_dotenv
import os

load_dotenv()

print("API Key:", os.getenv("GROQ_API_KEY"))

# =========================
# HF INFERENCE CLIENT
# =========================
def get_hf_client():
    token = os.getenv("HF_TOKEN")
    if not token:
        return None

    try:
        return InferenceClient(api_key=token, provider="hf-inference")
    except TypeError:
        # Older huggingface_hub fallback
        return InferenceClient(api_key=token)


# =========================
# TEXT CHUNKING
# =========================
def chunk_text(text, max_chars=3500):
    return [text[i:i + max_chars] for i in range(0, len(text), max_chars)]


# =========================
# YOUTUBE VIDEO ID EXTRACTOR
# =========================
def extract_video_id(url: str):
    patterns = [
        r"v=([a-zA-Z0-9_-]{11})",
        r"youtu\.be/([a-zA-Z0-9_-]{11})",
        r"shorts/([a-zA-Z0-9_-]{11})"
    ]
    for p in patterns:
        m = re.search(p, url)
        if m:
            return m.group(1)
    return None


# =========================
# CHAT WITH LLM
# =========================
def chat_with_llm(messages):
    clean_messages = []

    for msg in messages[-10:]:
        clean_messages.append({
            "role": msg["role"],
            "content": msg["content"]
        })

    completion = groq_client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=clean_messages
    )

    return completion.choices[0].message.content



# =========================
# PDF SUMMARY
# =========================
def summarize_pdf(pdf_file):
    reader = PdfReader(pdf_file)
    text = "".join((page.extract_text() or "") for page in reader.pages)

    if not text.strip():
        return "⚠️ Could not extract text from this PDF."

    partial_summaries = []
    for chunk in chunk_text(text):
        prompt = f"Summarize this part of the PDF clearly:\n{chunk}"
        res = groq_client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=[{"role": "user", "content": prompt}]
        )
        partial_summaries.append(res.choices[0].message.content)

    final_prompt = "Combine these into one clear summary:\n" + "\n".join(partial_summaries)
    final_res = groq_client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[{"role": "user", "content": final_prompt}]
    )
    return final_res.choices[0].message.content


# =========================
# YOUTUBE SUMMARY (OLD API COMPATIBLE)
# =========================
def _transcript_items_to_text(items):
    parts = []
    for it in items:
        if hasattr(it, "text"):
            parts.append(it.text)
        elif isinstance(it, dict) and "text" in it:
            parts.append(it["text"])
        else:
            parts.append(str(it))
    return " ".join(parts)


def summarize_youtube(url, output_language="English"):
    video_id = extract_video_id(url)
    if not video_id:
        return "❌ Invalid YouTube URL"

    try:
        transcript = None
        transcript_used = None

        # Try Telugu first
        try:
            transcript = YouTubeTranscriptApi().fetch(video_id, ["te"])
            transcript_used = "Telugu"
        except Exception:
            transcript = None

        # Fallback English
        if transcript is None:
            transcript = YouTubeTranscriptApi().fetch(video_id, ["en"])
            transcript_used = "English (Auto/Available)"

        text = _transcript_items_to_text(transcript)

        if not text.strip():
            return "⚠️ Transcript is empty / not available."

        summaries = []
        for chunk in chunk_text(text):
            res = groq_client.chat.completions.create(
                model="llama-3.1-8b-instant",
                messages=[{"role": "user", "content": f"Summarize this clearly:\n{chunk}"}]
            )
            summaries.append(res.choices[0].message.content)

        combined = " ".join(summaries)

        if output_language == "Telugu":
            final_prompt = (
                "Give the final summary in SIMPLE TELUGU. "
                "Use easy Telugu + English mix if needed:\n\n"
                f"{combined}"
            )
        else:
            final_prompt = "Give the final summary in SIMPLE, CLEAR ENGLISH:\n\n" + combined

        final = groq_client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=[{"role": "user", "content": final_prompt}]
        )

        return (
            f"### 📺 YouTube Video Summary\n\n"
            f"**Transcript Used:** {transcript_used}\n"
            f"**Summary Language:** {output_language}\n\n"
            f"{final.choices[0].message.content}"
        )

    except TranscriptsDisabled:
        return "⚠️ Transcripts are disabled for this video."
    except VideoUnavailable:
        return "⚠️ Video unavailable."
    except Exception as e:
        return f"❌ Error: {str(e)}"


# =========================
# IMAGE GENERATION (FIXED MODELS)
# =========================
import requests
from urllib.parse import quote

def generate_image(prompt, output_path="generated_image.png"):
    try:
        # Encode prompt
        encoded_prompt = quote(prompt)

        # Pollinations AI URL
        image_url = f"https://image.pollinations.ai/prompt/{encoded_prompt}"

        # Download image
        response = requests.get(image_url, timeout=60)

        if response.status_code == 200:
            with open(output_path, "wb") as f:
                f.write(response.content)
            return output_path
        else:
            return f"❌ Failed: HTTP {response.status_code}"

    except Exception as e:
        return f"❌ Image generation failed:\n{e}"