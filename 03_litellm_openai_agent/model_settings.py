import os
from agents.extensions.models.litellm_model import LitellmModel

# GEMINI MODEL SETTING
gemini_model = "gemini/gemini-2.0-flash"
gemini_api_key = os.getenv("GEMINI_API_KEY")
liteLLM_gemini20_model = LitellmModel(model=gemini_model, api_key=gemini_api_key)

# GROQ/Lama MODEL SETTING
groq_model = "groq/llama-3.3-70b-versatile"
groq_api_key = os.getenv("GROQ_API_KEY")
liteLLM_groq_model = LitellmModel(model=groq_model, api_key=groq_api_key)



