#  penAI Agents SDK

A Python framework for building and running intelligent agents using OpenAI-compatible models (e.g., Gemini via OpenAI API wrappers).

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
git rm --cached .env # --cached removes it from the repository but keeps it locally.
echo ".env" >> .gitignore # This command appends the line .env to your .gitignore file.
git commit -m "Remove .env from version control"
git push
```

---

### **Author**

**Tasneem Ibrahim**
[GitHub Profile](https://github.com/Tasneem-Ibrahim)

