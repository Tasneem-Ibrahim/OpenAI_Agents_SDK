from agents import Agent, Runner, handoff, AsyncOpenAI, OpenAIChatCompletionsModel, set_tracing_disabled
from dotenv import load_dotenv
import os

set_tracing_disabled(disabled=True)
load_dotenv()

API_KEY = os.environ.get("GEMINI_API_KEY")

model = OpenAIChatCompletionsModel(
    model="gemini-1.5-flash",
    openai_client=AsyncOpenAI(
        api_key=API_KEY,
        base_url="https://generativelanguage.googleapis.com/v1beta/openai"
    ),
)


billing_agent = Agent(
    name="Billing agent", 
    instructions="Handle billing questions like invoices, charges, and subscription plans.",
    model=model,
    handoff_description="Handles all billing questions and calculations."
)

refund_agent = Agent(
    name="Refund agent", 
    instructions="Handle all refund-related queries from users, clear and precise answers to problems and concepts.",
    model=model,
    handoff_description="Handles all refund queries."
)

triage_agent = Agent(
    name="Triage agent",
    instructions=(
        "Help the user with their questions."
        "If they ask about billing, handoff to the Billing agent."
        "If they ask about refund, handoff to the refund agent."
    ),
    handoffs=[billing_agent, refund_agent],
    model=model
)

result = Runner.run_sync(starting_agent=triage_agent, input="Please brief answer the refund process")
print("\n Handled by" , result.last_agent.name)
print("---------------")
print(result.final_output)
#print(result.new_items)