# chatbot.py — Handles communication with the Groq API

import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv()  # Load GROQ_API_KEY from .env


class ChatBot:
    """Handles Groq API calls with conversation memory."""

    def __init__(self):
        api_key = os.getenv("GROQ_API_KEY")
        if not api_key:
            raise ValueError(
                "GROQ_API_KEY not found! Add it to your .env file like:\n"
                "GROQ_API_KEY=your-key-here"
            )
        self.client = Groq(api_key=api_key)
        self.model = "llama-3.3-70b-versatile"

    def get_response(self, history: list) -> str:
        """
        Send conversation history to Groq and get a response.
        history: list of {"role": "system"/"user"/"assistant", "content": "..."}
        """
        try:
            response = self.client.chat.completions.create(
                model=self.model,
                messages=history,
                max_tokens=1000,
                temperature=0.7,
            )
            return response.choices[0].message.content

        except Exception as e:
            return f"⚠️ Error getting response: {str(e)}"