import os
from dotenv import load_dotenv
from agents import AsyncOpenAI, OpenAIChatCompletionsModel, set_tracing_disabled


load_dotenv()
set_tracing_disabled(disabled=True)

groq_api_key = os.getenv("GROQ_API_KEY")
groq_base_url = os.getenv("GROQ_BASE_URL")

if groq_api_key is None:
    raise ValueError("GROQ_API_KEY environment variable is not set")

groq_client = AsyncOpenAI(
    api_key=groq_api_key,
    base_url=groq_base_url
)

groq_model = OpenAIChatCompletionsModel(
    model="llama-3.3-70b-versatile",
    openai_client=groq_client
)