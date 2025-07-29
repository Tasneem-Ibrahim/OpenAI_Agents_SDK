import os
from agents import Agent, Runner, AsyncOpenAI, OpenAIChatCompletionsModel, function_tool
from agents.run import RunConfig
from agents import enable_verbose_stdout_logging
from dotenv import load_dotenv
from pydantic import BaseModel

# Pydantic v2 schema (not used in function_tool for v0.1.0)
class WeatherInputSchema(BaseModel):
    city: str
    class Config:
        extra = "forbid"

# Load .env file
load_dotenv()
enable_verbose_stdout_logging()

# Get Gemini API key
gemini_api_key = os.getenv("GEMINI_API_KEY")
if not gemini_api_key:
    raise ValueError("GEMINI_API_KEY not set. Ensure it's in your .env file.")

# Gemini client
client = AsyncOpenAI(
    api_key=gemini_api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
)

# Model wrapper
model = OpenAIChatCompletionsModel(
    model="gemini-2.0-flash",
    openai_client=client,
)

# Run config
config = RunConfig(
    model=model,
    tracing_disabled=True,
)

# Tool definition without schema
@function_tool
def get_weather(city: str) -> str:
    """Get the current weather in a given city."""
    return f"The weather in {city} is sunny."

# Agent definition
agent = Agent(
    name="Haiku agent",
    instructions="Always respond in haiku format.",
    model=model,
    tools=[get_weather],
)

# Run the agent
result = Runner.run_sync(agent, "What is the weather in Tokyo?", run_config=config)

print("\n===== Agent Name ========")
print(agent.name)
print("\n===== Final Output =====")
print(result.final_output)