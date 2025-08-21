from agents import Runner
from my_agent.assistant_agent import asst_agent

res = Runner.run_sync(starting_agent=asst_agent, input="what is squar root of 625?")

print(res.final_output)

