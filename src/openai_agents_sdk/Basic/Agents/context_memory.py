import os
from dotenv import load_dotenv

# Ensure required env variables are available early
os.environ["OPENAI_API_KEY"] = "dummy_value"  # <- Prevents OpenAIError

from agents import Agent, function_tool, AsyncOpenAI, OpenAIChatCompletionsModel, Runner
from agents.run import RunConfig
from dataclasses import dataclass

# Load .env values
load_dotenv()

gemini_api_key = os.getenv("GEMINI_API_KEY")
if not gemini_api_key:
    raise ValueError("GEMINI_API_KEY is not set. Please add it to your .env file.")

# Gemini client
external_client = AsyncOpenAI(
    api_key=gemini_api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
)

# Chat model
model = OpenAIChatCompletionsModel(
    model="gemini-2.0-flash",
    openai_client=external_client,
)

# Config
config = RunConfig(
    model=model,
    model_provider=external_client,
    tracing_disabled=True
)

# User class
@dataclass
class User:
    name: str
    phone: str
    current_conversation: list[str]

    def get_memory(self):
        return f"User {self.name} has a phone number {self.phone}"

    def update_memory(self, memory: str):
        self.memory = memory

    def update_conversation(self, message: str):
        self.current_conversation.append(message)

# System prompt function
async def get_system_prompt(ctx, start_agent):
    print("\n[context]", ctx)
    print("\n[agent]", start_agent)
    print("\n[start_agent.tools]", start_agent.tools)

    ctx.context.update_memory(f"User {ctx.context.name} has a phone number {ctx.context.phone}")
    ctx.context.update_conversation(f"User {ctx.context.name} has a phone number {ctx.context.phone}")

    return f"You are a helpful assistant. MEMORY: {ctx.context.get_memory()}"

# Agent setup
agent = Agent(
    name="Haiku agent",
    instructions=get_system_prompt,
    model=model  # ✅ Important!
)

# User
user_1 = User(name="Aariz", phone="123456789", current_conversation=[])

# Run
result = Runner.run_sync(agent, "Hi", context=user_1)

# Output
print("\n[result.final_output]")
print(result.final_output)
