# 🧠 OpenAI Agents SDK

A **Python framework** for building and running intelligent agents using **OpenAI-compatible models**
(e.g., Gemini via OpenAI API wrappers).

---

## 📦 Imports Required Classes

* `Agent`, `Runner` — Create and run AI agents
* `OpenAIChatCompletionsModel` — OpenAI-compatible wrapper (e.g., Gemini)
* `AsyncOpenAI` — Async client for OpenAI-like APIs
* `AgentOutputSchema` — Structured output format
* `BaseModel` — From `pydantic` for schema validation
* `load_dotenv`, `os` — For environment variables and secrets

---

## 🔍 Features

✅ Unified API for OpenAI and Gemini
🔧 Tool system to define function-calling logic
🎯 Force tool calls or let the agent choose
📜 Fun NLP use-cases (e.g., Haiku Agent)
🧱 Modular design (e.g., `context.py` for agent context)

---

## 🚰 Installation & Setup

```bash
git clone https://github.com/Tasneem-Ibrahim/OpenAI_Agents_SDK.git
cd OpenAI_Agents_SDK
python -m venv .venv
.venv\Scripts\activate   # On Windows
pip install -r requirements.txt
```

🔐 Create a `.env` file:

```env
GEMINI_API_KEY=your_actual_key_here
```

---

## 🚀 Usage Example

```python
from openai_agents_sdk.Basic.Agents.agent import Agent
from openai_agents_sdk.Basic.Agents.Runner import Runner
from openai_agents_sdk.Basic.Agents.is_weather_enabled import get_weather
from openai_agents_sdk.Basic.Models import model

agent = Agent(
    name="Weather agent",
    tools=[get_weather],
    model=model
)

result = Runner.run_sync(
    agent,
    "What is the weather in London?",
    context={"user_type": "pro"}
)

print(result.final_output)
```

---

## 📁 Examples Included

| File                     | Description                         |
| ------------------------ | ----------------------------------- |
| `is_weather_enabled.py`  | Weather tool with conditional logic |
| `forcing_tool_use.py`    | Forces specific tool usage          |
| `parallel_tool_calls.py` | Run tools in parallel               |
| `stop_on_first_tool.py`  | Halts after first tool call         |
| `cloning_agent.py`       | Multiple agents managing tasks      |
| `context.py`             | Runtime variables & context setup   |

---

## 🔐 Security Notice

Your `.env` file **must never be committed publicly**.

Ensure this is in your `.gitignore`:

```gitignore
.env
```

🛉 Remove `.env` from Git history if committed:

```bash
git rm --cached .env
echo ".env" >> .gitignore
git commit -m "Remove .env from version control"
git push
```

---

## 📘 Summary

**This Repository Includes:**

✅ Python SDK for intelligent agents
✅ Gemini + OpenAI model support
✅ Flexible function-calling tools
✅ Multiple agent use-cases
✅ Modular directory structure

---

## 👩‍💻 Author

**Tasneem Ibrahim**
🔗 [GitHub Profile »](https://github.com/Tasneem-Ibrahim)
