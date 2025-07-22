# 🧠 OpenAI Agents SDK

A Python framework for building and running intelligent agents using OpenAI-compatible models (e.g., Gemini via OpenAI API wrappers).

---

### ✅ **Purpose**

This project demonstrates how to use OpenAI-compatible models with custom agents and dynamic tool usage, enabling:

* Modular AI agent design
* Parallel tool calling
* Dynamic instruction control
* Forced or conditional tool use

---

### 📦 **Imports Required Classes**

* ***Agent, Runner***: For creating and running AI agents.
* ***OpenAIChatCompletionsModel***: Wrapper for OpenAI-compatible models (e.g., Gemini).
* ***AsyncOpenAI***: Async client to connect to OpenAI-compatible APIs.
* ***AgentOutputSchema***: Defines the structured output format.
* ***BaseModel***: From `pydantic`, for schema validation.
* ***load\_dotenv, os***: For loading environment variables such as API keys.

---

### 🔍 **Features**

* Support for OpenAI and Gemini models via common API
* Flexible `Tool` system to define function-calling behavior
* Force tool calls or let the agent choose
* Haiku agent example (fun NLP use)
* Modular agent contexts (`context.py`)

---

### 🛠️ **Installation & Setup**

```bash
git clone https://github.com/Tasneem-Ibrahim/OpenAI_Agents_SDK.git
cd OpenAI_Agents_SDK
python -m venv .venv
.venv\Scripts\activate   # On Windows
pip install -r requirements.txt
```

Create `.env` file:

```env
GEMINI_API_KEY=your_actual_key_here
```

---

### 🧪 **Usage Example**

```python
from openai_agents_sdk.Basic.Agents.agent import Agent
from openai_agents_sdk.Basic.Agents.Runner import Runner
from openai_agents_sdk.Basic.Agents.is_weather_enabled import get_weather
from openai_agents_sdk.Basic.Models import model

agent = Agent(name="Weather agent", tools=[get_weather], model=model)
result = Runner.run_sync(agent, "What is the weather in London?", context={"user_type": "pro"})
print(result.final_output)
```

---

### 📁 **Examples Included**

| File                     | Description                                |
| ------------------------ | ------------------------------------------ |
| `is_weather_enabled.py`  | Weather tool with conditional enablement   |
| `forcing_tool_use.py`    | Forces specific tool use                   |
| `parallel_tool_calls.py` | Executes multiple tools in parallel        |
| `stop_on_first_tool.py`  | Stops agent after the first tool execution |
| `cloning_agent.py`       | Demonstrates multiple agents handling      |
| `context.py`             | Manages runtime context & variables        |

---

### 🔐 **Security Notice**

Your `.env` file **must never be committed** publicly. It includes sensitive API keys. Make sure your `.gitignore` includes:

```gitignore
.env
```

You can remove the already committed `.env` from Git history using:

```bash
git rm --cached .env
echo ".env" >> .gitignore
git commit -m "Remove .env from version control"
git push
```

---

### 📜 **License**

This project is licensed under the [MIT License](LICENSE).

---

### 🙋‍♀️ **Author**

**Tasneem Ibrahim**
[GitHub Profile](https://github.com/Tasneem-Ibrahim)

Feel free to contribute, fork, or submit pull requests!

---

### ✅ **To-Do / Future Improvements**

* [ ] Add unit tests and GitHub Actions CI
* [ ] Support Claude and Mistral models
* [ ] Add CLI agent runner
* [ ] Package to PyPI
