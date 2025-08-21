#type:ignore
import os
from dotenv import load_dotenv
from agents import AsyncOpenAI, OpenAIChatCompletionsModel, Agent, Runner,set_tracing_disabled

load_dotenv()
set_tracing_disabled(disabled=True)

gemini_api_key = os.getenv("GEMINI_API_KEY")
gemini_base_url = os.getenv("GEMINI_BASE_URL")

gemini_client = AsyncOpenAI(
    api_key=gemini_api_key,
    base_url=gemini_base_url
)

gemini_model = OpenAIChatCompletionsModel(
    model="gemini-2.5-flash",
    openai_client=gemini_client
)

agent = Agent(
    name="Assistant",
    instructions="You are a helpful Assistant",
    model=gemini_model
)   
res = Runner.run_sync(starting_agent=agent, input="2+2=?")

print(res.final_output)
