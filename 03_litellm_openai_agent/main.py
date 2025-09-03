import os
from dotenv import load_dotenv
from agents import Agent, Runner
from agents.extensions.models.litellm_model import LitellmModel
from rich import print

load_dotenv()

gemini_model="gemini/gemini-2.0-flash"
gemini_api_key = os.getenv("GEMINI_API_KEY")

agent = Agent(
    name="Assistant",
    instructions="You are a helpful assistant",
    model=LitellmModel(model=gemini_model, api_key=gemini_api_key)
)

result = Runner.run_sync(agent,"How are you, and what is the capital of Pakistan?")
print(result.final_output)

