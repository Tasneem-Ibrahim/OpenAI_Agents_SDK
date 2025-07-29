from agents import Agent, Runner, AsyncOpenAI, OpenAIChatCompletionsModel, set_tracing_disabled, RunContextWrapper, function_tool
from dotenv import load_dotenv
import os

# Load .env variables
load_dotenv()
set_tracing_disabled(disabled=True)

# Get Gemini API key from .env
gemini_api_key = os.getenv("GEMINI_API_KEY")
if not gemini_api_key:
    raise ValueError("GEMINI_API_KEY is not set. Please add it to your .env file.")

# Setup Gemini client via OpenAI-compatible wrapper
client = AsyncOpenAI(
    api_key=gemini_api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
)

# Initialize OpenAI-style chat model using Gemini
model = OpenAIChatCompletionsModel(
    model="gemini-2.0-flash",
    openai_client=client,
)


def is_weather_enabled(ctx: RunContextWrapper, start_agent: Agent) -> bool:
    context = ctx.context or {}
    return context.get("user_type", "basic") != "basic"

# Weather tool
@function_tool(is_enabled=is_weather_enabled)
def get_weather(city: str) -> str:
    return f"The weather in {city} is sunny."

# Define agent
agent = Agent(
    name="Haiku agent",
    tools=[get_weather],
    model=model
)

# Run agent with context
result = Runner.run_sync(
    agent,
    "What is the weather in Karachi?",
    context={"user_type": "basic"}  # change to "pro" to enable tool
)

print("\n[result.final_output]")
print(result.final_output)


# OUTPUT (user type if 'Basic'):
# [result.final_output]
# I'm sorry, I don't have the current weather conditions for Karachi. However, you can find that information at these sources:

# *   **Google Search:** Search "weather in Karachi" on Google.
# *   **Weather Apps:** Use a weather app like AccuWeather, The Weather Channel, or local weather apps.
# *   **Weather Websites:** Visit weather websites like Accuweather.com or Weather.com.

# OUTPUT (user type if 'pro'):
#[result.final_output]
# The weather in Karachi is sunny.