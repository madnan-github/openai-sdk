import asyncio
from agents import Agent, Runner, function_tool, set_tracing_disabled
from model_settings import liteLLM_gemini20_model, liteLLM_groq_model

set_tracing_disabled(disabled=True)

@function_tool
def get_weather(city:str)->str:
    return f"The weather in {city} is sunny."

agent = Agent(
    name="Assistant",
    instructions="You are a helpful assistant.",
    model=liteLLM_groq_model,
    tools=[get_weather],
)

# Runner.run
async def main():
    result = await Runner.run(agent,"How is the weather of Swat?")
    print(result.final_output)

if __name__ == "__main__":
    asyncio.run(main())

