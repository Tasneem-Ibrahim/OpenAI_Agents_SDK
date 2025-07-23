import os
from pydantic_ai import Agent
from dotenv import load_dotenv

# Load .env file
load_dotenv()

# Get Gemini API key from .env
gemini_api_key = os.getenv("GEMINI_API_KEY")

# Raise error if missing
if not gemini_api_key:
    raise ValueError("GEMINI_API_KEY is not set. Please add it to your .env file.")

# Define agent with Gemini model (using string identifier)
agent = Agent(
    'gemini-2.0-flash-exp',  # Model string identifier
    system_prompt="Always respond in haiku format",
)

# Define tools using the proper agent decorators
@agent.tool_plain
def get_weather(city: str) -> str:
    """Get the weather for a city."""
    return f"The weather in {city} is sunny."

@agent.tool_plain
def get_support_details(city: str) -> str:
    """Get support details for a city."""
    return f"The support details for {city} are 12345678."

# Run the agent using the correct method
result = agent.run_sync("What is the weather in Karachi also share the details?")
print(result.data)  # Use .data instead of .final_output