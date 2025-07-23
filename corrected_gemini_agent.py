import os
from pydantic_ai import Agent
from pydantic_ai.models.gemini import GeminiModel
from dotenv import load_dotenv

# Load .env file
load_dotenv()

# Get Gemini API key from .env
gemini_api_key = os.getenv("GEMINI_API_KEY")

# Raise error if missing
if not gemini_api_key:
    raise ValueError("GEMINI_API_KEY is not set. Please add it to your .env file.")

# Create Gemini model
model = GeminiModel("gemini-2.0-flash-exp", api_key=gemini_api_key)

# Tool: Weather generator
@Agent.tool_plain
def get_weather(city: str) -> str:
    """Get the weather for a city."""
    return f"The weather in {city} is sunny."

@Agent.tool_plain  
def get_support_details(city: str) -> str:
    """Get support details for a city."""
    return f"The support details for {city} are 12345678."

# Define agent
agent = Agent(
    model=model,
    name="Haiku agent",
    system_prompt="Always respond in haiku format",
    tools=[get_weather, get_support_details],
)

# Run the agent
result = agent.run_sync("What is the weather in Karachi also share the details?")
print(result.data)