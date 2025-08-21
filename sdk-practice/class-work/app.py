#type:ignore
from dotenv import load_dotenv
import os
from agents import Agent,
    Runner,
    RunConfig,
    OpenAIChatCompletionsModel,
    AsyncOpenAI,
    set_tracing_disabled,
    function_tool,
    enable_verbose_stdout_logging,

import asyncio
# enable_verbose_stdout_logging()

# from agents.run import RunConfig
from rich import print

load_dotenv()
set_tracing_disabled(disabled=True)

gemini_api_key = os.getenv("GEMINI_API_KEY")
# step 1: external client
provider = AsyncOpenAI(
     api_key=gemini_api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
)
# 2 step model
model = OpenAIChatCompletionsModel(
    model="gemini-2.0-flash",
    openai_client=provider,
)
# config: define at run level
config = RunConfig(
    model=model,
    model_provider=provider,
)

@function_tool
def get_capital(country:str) -> str:
    return f"The capital of {country} is {country.capitalize()}."

async def main():
    agent=Agent(
    name = "Assistant", #name is required
    # name = 123   # test:1 --> name in int
    instructions="You are helpful Assistent.",
    tools=[get_capital],
    )
        result = await Runner.run(agent, input="What is the capital of France?", run_config=config)
        print("Result :\n")
        print(result.final_output)


asyncio.run(main())
