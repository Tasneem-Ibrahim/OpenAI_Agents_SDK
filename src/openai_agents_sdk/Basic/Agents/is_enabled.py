import os
from agents import Agent, Runner, function_tool, AsyncOpenAI, OpenAIChatCompletionsModel, ModelSettings
from agents.run import RunConfig
# from agents import enable_verbose_stdout_logging
from dotenv import load_dotenv

# Load .env file
load_dotenv()

# Optional: Enable verbose logs in Cursor terminal
# enable_verbose_stdout_logging()

# Get Gemini API key from .env
gemini_api_key = os.getenv("GEMINI_API_KEY")

# Raise error if missing
if not gemini_api_key:
    raise ValueError("GEMINI_API_KEY is not set. Please add it to your .env file.")

# Gemini via OpenAI-compatible wrapper (Google Gemini Docs-based)
external_client = AsyncOpenAI(
    api_key=gemini_api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
)

# Use OpenAI-style chat model
model = OpenAIChatCompletionsModel(
    model="gemini-2.0-flash",
    openai_client=external_client,
)

# Run configuration
config = RunConfig(
    model=model,
    tracing_disabled=True
)

# Tool: Weather generator
@function_tool(is_enabled=False)
def get_weather(city: str) -> str:
    return f"The weather in {city} is sunny."

# Define agent
agent = Agent(
    name="Haiku agent",
    instructions="Always responed in haiku format.",
    model=model,
    tools=[get_weather],
    
)

Result=Runner.run_sync(agent, "What is the weather in Karachi?")
print(Result.final_output)
