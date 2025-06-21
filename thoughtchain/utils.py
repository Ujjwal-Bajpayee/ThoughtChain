import google.generativeai as genai
from thoughtchain.config import API_KEY, MODEL

# Configure Gemini API
genai.configure(api_key=API_KEY)

def call_llm(prompt, model=MODEL):
    """
    Call Gemini to generate a response based on a text prompt.
    """
    generation_model = genai.GenerativeModel(model)
    response = generation_model.generate_content(prompt)
    return response.text.strip()
