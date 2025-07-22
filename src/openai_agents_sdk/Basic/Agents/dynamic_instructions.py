from agents import Agent, Runner, AsyncOpenAI, OpenAIChatCompletionsModel, set_tracing_disabled, RunContextWrapper
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

# Define system prompt logic
def get_system_prompt(ctx, start_agent):
    print("\n[context]", ctx.context)
    print("\n[agent]", start_agent)
    return "You are a helpful assistant that can answer questions and help with tasks."

# Create agent
agent = Agent(
    name="Haiku agent",
    instructions=get_system_prompt,
    model=model,  # <- You were missing this line to assign the model
)

# Run agent synchronously
if __name__ == "__main__":
    result = Runner.run_sync(agent, "Hi")
    print("\n[Final Output]", result.final_output)
