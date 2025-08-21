from agents import Agent
from my_config.gemini_config import gemini_model

asst_agent = Agent(
    name="Assistant",
    # instructions="You are a helpful Assistant"
    model=gemini_model
)   
