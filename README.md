# AI Agent Architecture Demo

This project demonstrates a conceptual AI agent architecture using modular components designed for intelligent automation. It simulates how a language model-driven agent can analyze input, select tools, manage memory, and return structured outputs—applicable to enterprise automation use cases.

## 📦 Key Modules

- `AgentCore`: Handles prompt routing, tool selection, and output formatting
- `Toolset`: Basic tools like search, summarizer, math, etc.
- `Memory`: Session context management (short-term, long-term)
- `Planner`: Breaks down user goals into task plans
- `Orchestrator`: Manages agent loop and tool execution

## 🧠 Design Principles

- Composable functions and tools
- OpenAI-compatible language model interface
- YAML-based config and planning
- Architecture aligned with LangChain/LlamaIndex-style extensibility

## 🚀 Getting Started

1. Install Python dependencies:
```bash
pip install -r requirements.txt
```

2. Run the agent with a use case prompt:
```bash
python src/agent_main.py --usecase "Automate invoice data extraction and entry"
```

## 📊 Diagrams

See `/diagrams` for Mermaid + PNG architecture diagrams

## 👤 Author

Created by Sha Vadwalas – Director/Principal Enterprise Architect | AI/Automation | Cloud/Data Strategy  
[LinkedIn](https://www.linkedin.com/in/sha-v-0557a118/)

## 📜 License

MIT License – for demonstration and educational use.
