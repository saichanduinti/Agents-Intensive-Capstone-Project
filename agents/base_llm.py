import google.generativeai as genai
from dotenv import load_dotenv
import os
from observability.logger import logger

# Load .env
load_dotenv()

# Get API key from environment
api_key = os.getenv("GEMINI_API_KEY")
if not api_key:
    raise ValueError("GEMINI_API_KEY not found in environment. Please add it to your .env file.")

# Configure Gemini
genai.configure(api_key=api_key)

def call_gemini(prompt: str, model: str = "gemini-2.5-flash"):
    """
    Sends a prompt to Google Gemini LLM and returns the generated text.
    
    Args:
        prompt (str): The prompt to send to the LLM.
        model (str): The Gemini model to use. Default is 'gemini-pro'.
    
    Returns:
        str: Generated text from Gemini.
    """
    try:
        logger.log("Calling Gemini LLM...")
        response = genai.GenerativeModel(model).generate_content(prompt)
        return response.text
    except Exception as e:
        logger.log(f"Error calling Gemini: {e}")
        return f"Error: {e}"
