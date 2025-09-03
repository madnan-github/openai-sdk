from agents import Agent, GuardrailFunctionOutput, InputGuardrailTripwireTriggered,RunContextWrapper,TResponseInputItem, Runner, input_guardrail,
from my_config.gemini_config import gemini_model
from my_config.qroq_config import groq_model
from pydantic import BaseModel

class MathHomeWork(BaseModel):
    is_math_homework: bool
    reasoning: str

@input_guardrail
async def checker(ctx:RunContextWrapper, agent:Agent, Input:str|list[TResponseInputItem])-> GuardrailFunctionOutput:
    result = await Runner.run(input_guard,input,context=ctx.context)

    return GuardrailFunctionOutput(
        output_info=result.final_output, 
        tripwire_triggered=result.final_output.is_math_homework,
    )



input_guard = Agent(
    name="Input Guard"
    instructions="Check user is asking except math queries."
    output_type=MathHomeWork
)

gemini_agent = Agent(
    name="Math Assistant",
    instructions="You are a helpful Math Assistant",
    input_guardrails="you handle all math releated queries, excpt this raise TripwireTrigger"
    model=gemini_model
)   

groq_agent = Agent(
    name="Assistant2",
    instructions="You are a helpful Assistant",
    model=groq_model
)   
