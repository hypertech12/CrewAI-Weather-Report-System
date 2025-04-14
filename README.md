# CrewAI Weather Report System

A multi-agent AI weather reporting tool built using Python and the CrewAI framework. This project integrates a local LLM via Ollama on macOS to deliver detailed, real-time weather forecasts without relying on external APIs.

## Features

- **Multi-Agent Architecture**  
  Utilizes role-specific agents:
  - **Weather Data Collector**: Gathers raw weather data.
  - **Meteorologist Expert**: Analyzes and interprets weather patterns.
  - **Local Weather Reporter**: Provides localized weather insights.

- **Local LLM Integration via Ollama**  
  Uses a local LLM (e.g., LLaMA 3 via Ollama) to generate natural language forecasts.

- **Developed in PyCharm**  
  The project is developed and maintained in PyCharm for efficient debugging and development.

## Getting Started

### Prerequisites

- **macOS** with Homebrew installed.
- **Ollama** installed on your system:
  
  ```bash
  brew install ollama
  ollama serve
  ollama pull llama3
