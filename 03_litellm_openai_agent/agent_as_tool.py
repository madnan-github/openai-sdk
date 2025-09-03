import os
from agents import Agent, Runner, function_tool, set_tracing_disabled, enable_verbose_stdout_logging
from agents.extensions.models.litellm_model import LitellmModel
from rich import print
set_tracing_disabled(disabled=True)
# enable_verbose_stdout_logging()

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
    # handoff_description="Weather Assistant is specialized for all weather Queries."
)

healthcare_agent = Agent(
    name="HealthCare Assistant",
    instructions="You will answer all Healthcare releated queries.",
    model=LitellmModel(model=gemini_model, api_key=gemini_api_key),
    tools=[get_weather],
    # handoff_description="HealtCare Assistant is specialized for all HealthCare Queries."
)

triage_agent = Agent(
    name="General Assistant",
    instructions="You will chat user with general question, handoff to weather assistant about all weather releated quries,  handoff to  healthcare assistant about all healthcare and medical releated queries.",
    model=LitellmModel(model=gemini_model, api_key=gemini_api_key),
    tools=[weather_agent.as_tool(tool_name="Weather_Tool", tool_description="Weather Assistant is specialized for all weather Queries."),
           healthcare_agent.as_tool(tool_name="HealthCare_Tool", tool_description="HealtCare Assistant is specialized for all HealthCare Queries.")]
)
# Runner.run_sync
result = Runner.run_sync(triage_agent,"How are you? What is the weather of Islamabad also advice can I excercise daily for fitness.")
print(result.final_output)
print(result.last_agent.name)
