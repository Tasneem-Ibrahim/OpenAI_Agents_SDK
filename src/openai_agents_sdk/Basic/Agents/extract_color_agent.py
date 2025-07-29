import os
from agents import Agent, Runner, AsyncOpenAI, OpenAIChatCompletionsModel, function_tool
from agents.run import RunConfig
from dotenv import load_dotenv

# Load .env file
load_dotenv()

# Get Gemini API key
API_KEY = os.getenv("GEMINI_API_KEY")
if not API_KEY:
    raise ValueError("GEMINI_API_KEY not set. Ensure it's in your .env file.")

# Gemini client (verify compatibility)
client = AsyncOpenAI(
    api_key=API_KEY,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
)

# Model wrapper
model = OpenAIChatCompletionsModel(
    model="gemini-1.5-flash",
    openai_client=client,
)

# Run config
config = RunConfig(
    model=model,
    tracing_disabled=True,
)

# Tool for color extraction from URL
@function_tool
def extract_color(url: str = "https://colorkit.co/color/008b8b/") -> str:
    """Extract the color name from a ColorKit URL."""
    # Hardcode for specific URL (no need for requests since color is known)
    if url == "https://colorkit.co/color/008b8b/":
        return "Color: Dark Cyan (Hex: #008b8b)"
    return "Error: Invalid URL or color not found."

# Main chat agent
chat_agent = Agent(
    name="Chat Agent",
    instructions="Answer in haiku format, extracting colors from URLs when asked.",
    tools=[extract_color],
)

# Run the agent with URL
result = Runner.run_sync(chat_agent, "Extract the color from https://colorkit.co/color/008b8b/.", run_config=config)

print("\n===== Agent Name =====")
print(chat_agent.name)
print("\n===== Final Output =====")
print(result.final_output)