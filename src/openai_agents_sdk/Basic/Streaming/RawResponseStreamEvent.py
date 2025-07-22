# Raw Response Stream Event

import os, asyncio

from agents import Agent, Runner, AsyncOpenAI, OpenAIChatCompletionsModel
from agents.run import RunConfig
from agents import enable_verbose_stdout_logging 
from dotenv import load_dotenv


# Load .env file
load_dotenv()

# Optional: Enable verbose logs in Cursor terminal
enable_verbose_stdout_logging()

# Get Gemini API key from .env
gemini_api_key = os.getenv("GEMINI_API_KEY")
# Check if the API key is present; if not, raise an error
if not gemini_api_key:
    raise ValueError("GEMINI_API_KEY is not set. Please ensure it is defined in your .env file.")

#Reference: https://ai.google.dev/gemini-api/docs/openai
external_client = AsyncOpenAI(
    api_key=gemini_api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
)

model = OpenAIChatCompletionsModel(
    model="gemini-2.0-flash",
    openai_client=external_client
)

config = RunConfig(
    model=model,
    model_provider=external_client,
    tracing_disabled=True
)

# enable_verbose_stdout_logging()

agent = Agent(
    name="Assistant",
    instructions="You are a helpful assistant",
    model=model
)

async def stream_agent():
    result = Runner.run_streamed(agent, "Write a haiku about recursion in programming.", run_config=config)

    async for event in result.stream_events():
        print(f"\n[EVENT]: {event.type}\n")
        if event.type == 'raw_response_event':
          print(f"[DATA]: {event.data}")

asyncio.run(stream_agent())