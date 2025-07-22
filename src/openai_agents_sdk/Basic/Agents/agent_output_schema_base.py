import os
from dotenv import load_dotenv
from pydantic import BaseModel
from agents import Agent, Runner, OpenAIChatCompletionsModel, AsyncOpenAI, set_tracing_disabled

# ----------------------------
# ✅ Setup: Disable Tracing & Load .env
# ----------------------------
set_tracing_disabled(disabled=True)
load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY")
if not API_KEY:
    raise ValueError("GEMINI_API_KEY not found in .env")

# ----------------------------
# ✅ OpenAI-compatible Gemini Client
# ----------------------------
client = AsyncOpenAI(
    api_key=API_KEY,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai"
)

model = OpenAIChatCompletionsModel(
    openai_client=client,
    model="gemini-1.5-flash"
)

# ----------------------------
# ✅ Output Schema
# ----------------------------
class AnalyticsAgentOutput(BaseModel):
    is_positive: bool
    genre: str
    summary: str

# ----------------------------
# ✅ Custom Output Schema Base
# ----------------------------
class AgentOutputSchemaBase:
    def is_plain_text(self) -> bool:
        return False

    def name(self) -> str:
        return "AnalyticsAgentOutput"

    def json_schema(self):
        return {
            "is_positive": True,
            "genre": "Strategy",
            "summary": "The recent focus on AI integration gives us a strong competitive edge—well done!"
        }

    def is_strict_json_schema(self) -> bool:
        return True

# ----------------------------
# ✅ Define Agent
# ----------------------------
agent = Agent(
    name="Analyzer",
    instructions=(
        "Examine the customer complaint, identify the key issue, "
        "classify the severity level, and summarize the incident. "
        "Add relevant tags such as department or urgency level."
    ),
    output_type=AnalyticsAgentOutput,
    model=model,
)

# ----------------------------
# ✅ Run the Agent
# ----------------------------
result = Runner.run_sync(
    starting_agent=agent,
    input="We’re entering a new market without a clear marketing or logistics strategy. This seems rushed." 
    # if out is "is_positive=False" means that the sentiment or evaluation in question is not positive — in other words, it is negative
)

print(result.final_output)
