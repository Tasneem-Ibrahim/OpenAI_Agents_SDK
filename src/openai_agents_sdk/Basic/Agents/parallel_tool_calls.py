import os
from agents import Agent, ModelSettings, function_tool, AsyncOpenAI, OpenAIChatCompletionsModel, Runner
from agents.run import RunConfig
from agents.agent import StopAtTools
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
client = AsyncOpenAI(
    api_key=gemini_api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
)

# Use OpenAI-style chat model
model = OpenAIChatCompletionsModel(
    model="gemini-2.0-flash",
    openai_client=client,
)

# Run configuration
config = RunConfig(
    model=model,
    tracing_disabled=True
)

# Tool: Weather generator
@function_tool
def get_weather(city: str) -> str:
    return f"The weather in {city} is sunny."

@function_tool
def get_support_details(city: str) -> str:
    return f"The support details for {city} are 12345678."

# Define agent
agent = Agent(
    name="Haiku agent",
    instructions="Always responed in haiku format",
    model=model,
    tools=[get_weather, get_support_details],
    model_settings=ModelSettings( tool_choice="required", parallel_tool_calls=False) # It will generate Error beacuse of max turn limit.
)

Result=Runner.run_sync(agent, "What is the weather in Karachi? Also, what is the support details for pizza max?", max_turns=2)
print(Result.final_output)
