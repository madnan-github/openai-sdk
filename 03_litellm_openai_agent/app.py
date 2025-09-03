import os
from agents import Agent, Runner, set_tracing_disabled
from agents.extensions.models.litellm_model import LitellmModel

set_tracing_disabled(disabled=True)

gemini_model="gemini/gemini-2.0-flash"
gemini_api_key = os.getenv("GEMINI_API_KEY")

agent = Agent(
    name="Assistant",
    instructions="You are a helpful assistant",
    model=LitellmModel(model=gemini_model, api_key=gemini_api_key)
)
# Runner.run_sync
result = Runner.run_sync(agent,"How are you, and what is the capital of France?")
print(result.final_output)