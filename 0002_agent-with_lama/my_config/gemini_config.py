import os
from dotenv import load_dotenv
from agents import AsyncOpenAI, OpenAIChatCompletionsModel, set_tracing_disabled
# from agentsdk_gemini_adapter import config

load_dotenv()
set_tracing_disabled(disabled=True)

gemini_api_key = os.getenv("GEMINI_API_KEY")
gemini_base_url = os.getenv("GEMINI_BASE_URL")

if gemini_api_key is None:
    raise ValueError("GEMINI_API_KEY environment variable is not set")

gemini_client = AsyncOpenAI(
    api_key=gemini_api_key,
    base_url=gemini_base_url
)

gemini_model = OpenAIChatCompletionsModel(
    model="gemini-2.5-flash",
    openai_client=gemini_client
)