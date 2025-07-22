from agents import Agent, Runner, OpenAIChatCompletionsModel, AsyncOpenAI, set_tracing_disabled, AgentOutputSchema
from dotenv import load_dotenv
from pydantic import BaseModel
import os

set_tracing_disabled(disabled=True)
load_dotenv()

API_KEY = os.environ.get("GEMINI_API_KEY")

client = AsyncOpenAI(
    api_key=API_KEY,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai"
)

model = OpenAIChatCompletionsModel(
    openai_client=client,
    model="gemini-1.5-flash"
)

class Analytics_Agent(BaseModel):
    is_positive: bool
    genre: str
    summary: str

agent = Agent(
    name="Analyzer",
    instructions="Examine the customer complaint, identify the key issue, classify the severity level, and summarize the incident. Add relevant tags such as department or urgency level",
    output_type=AgentOutputSchema(Analytics_Agent, strict_json_schema=False),
    model=model,
)

result = Runner.run_sync(
    starting_agent=agent,
    input="The recent focus on AI integration gives us a strong competitive edge—well done!", # positive
    #input="We’re entering a new market without a clear marketing or logistics strategy. This seems rushed." # negative
)

print(result.final_output)