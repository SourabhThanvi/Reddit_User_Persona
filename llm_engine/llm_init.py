import google.generativeai as genai
from dotenv import load_dotenv
import os

load_dotenv()

API_KEY = os.getenv('GEMINI_API_KEY')  # Use standard naming

class GeminiClient:
    def get_client(self):
        if not API_KEY:
            raise ValueError("Gemini API key not found in environment variables.")
        try:
            genai.configure(api_key=API_KEY)
            model = genai.GenerativeModel('gemini-2.5-flash')  # or your desired model name
            return model
        except Exception as e:
            print(f"[GeminiClient] Error creating LLM client: {e}")
            return None
