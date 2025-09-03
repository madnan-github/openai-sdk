import os
from agents import Agent, Runner, function_tool, set_tracing_disabled
from agents.extensions.models.litellm_model import LitellmModel

set_tracing_disabled(disabled=True)

gemini_model="gemini/gemini-2.0-flash"
gemini_api_key = os.getenv("GEMINI_API_KEY")

@function_tool
def get_weather(city:str)->str:
    return f"The weather in {city} is sunny."

weather_agent = Agent(
    name="Weather Assistant",
    instructions="You will answer all weather releated queries.",
    model=LitellmModel(model=gemini_model, api_key=gemini_api_key),
    tools=[get_weather],
    handoff_description="Weather Assistant is specialized for all weather Queries."
)

healthcare_agent = Agent(
    name="HealthCare Assistant",
    instructions="You will answer all Healthcare releated queries.",
    model=LitellmModel(model=gemini_model, api_key=gemini_api_key),
    tools=[get_weather],
    handoff_description="HealtCare Assistant is specialized for all HealthCare Queries."
)

triage_agent = Agent(
    name="General Assistant",
    instructions="You will chat user with general question, handoff to weather assistant about all weather releated quries,  handoff to  healthcare assistant about all healthcare and medical releated queries.",
    model=LitellmModel(model=gemini_model, api_key=gemini_api_key),
    handoffs=[weather_agent, healthcare_agent]
)
# Runner.run_sync
result = Runner.run_sync(triage_agent,"How are you?")
print(result.final_output)
print(result.last_agent.name)
print("*" * 10)

result = Runner.run_sync(triage_agent,"What is the weather in New York?")
print(result.final_output)
print(result.last_agent.name)
print("*" * 10)

result = Runner.run_sync(triage_agent,"How can I releave with Head Ach?")
print(result.final_output)
print(result.last_agent.name)
print("*" * 10)