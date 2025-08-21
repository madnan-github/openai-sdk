from agents import Agent
from my_config.gemini_config import gemini_model
from my_config.qroq_config import groq_model

gemini_agent = Agent(
    name="Assistant",
    instructions="You are a helpful Assistant",
    model=gemini_model
)   

groq_agent = Agent(
    name="Assistant2",
    instructions="You are a helpful Assistant",
    model=groq_model
)   
