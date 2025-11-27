# AgentFlow Examples

Official examples for the [AgentFlow](https://github.com/ia-nova-labs/agentflow) framework.

## 📦 Installation

First, install AgentFlow:

```bash
pip install agentflow-ai==1.0.5
```

## ⚙️ Prerequisites

Most examples require [Ollama](https://ollama.ai) running locally:

```bash
# Install Ollama (see https://ollama.ai)
# Then pull a model:
ollama pull qwen2.5-coder:1.5b
```

**Note**: These examples use `qwen2.5-coder:1.5b` as the default model. You can easily adapt them to use any other LLM by changing the model parameter:

```python
# Current (Qwen)
agent = Agent(model="qwen2.5-coder:1.5b")

# Or use any other Ollama model
agent = Agent(model="llama3.1:8b")
agent = Agent(model="mistral")

# Or use OpenAI/Mistral APIs
from agentflow import OpenAI, Mistral
agent = Agent(model=OpenAI(model="gpt-4o"))
agent = Agent(model=Mistral(model="mistral-large-latest"))
```


### Basic Usage

- **[example_basic.py](example_basic.py)** - Basic agent usage, conversation history, and error handling
- **[example_async.py](example_async.py)** - Async/await patterns and concurrent execution

### Features

- **[example_tools.py](example_tools.py)** - Tool decorator and multi-step reasoning
- **[example_memory.py](example_memory.py)** - Persistent memory with FileMemory
- **[example_models.py](example_models.py)** - Using Ollama, OpenAI, and Mistral

### Advanced

- **[example_robust_loop.py](example_robust_loop.py)** - Debug mode, loop detection, and timeouts
- **[example_testing.py](example_testing.py)** - MockModel and AgentTestClient for offline testing
- **[example_mcp.py](example_mcp.py)** - MCP integration with filesystem and Git servers

## 🚀 Running Examples

```bash
# Clone this repo
git clone https://github.com/ia-nova-labs/agentflow-examples
cd agentflow-examples

# Run an example
python example_basic.py
```

## 📚 Documentation

See the main [AgentFlow documentation](https://github.com/ia-nova-labs/agentflow-docs) for comprehensive guides.

## 🔗 Links

- [AgentFlow](https://github.com/ia-nova-labs/agentflow) - Main framework
- [Documentation](https://github.com/ia-nova-labs/agentflow-docs) - Comprehensive guides
- [Examples](https://github.com/ia-nova-labs/agentflow-examples) - This repo

## 📄 License

MIT License - see [LICENSE](LICENSE)
