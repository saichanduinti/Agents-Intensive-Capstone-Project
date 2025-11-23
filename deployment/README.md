# DataFlow Automation Agent
## Environment Setup

Create a `.env` file in the root folder:


## Overview
This project is a **multi-agent AI system** designed for automating data workflows:
- **CleanerAgent**: Validates and cleans datasets.
- **AnalyzerAgent**: Generates statistics and correlation insights.
- **ReporterAgent**: Uses Google Gemini API to produce a professional natural language report.
- **CoordinatorAgent**: Orchestrates the full pipeline.

## Features Implemented
- **Multi-Agent System**: Sequential & coordinated agent workflow.
- **Tools Integration**: Data cleaning, validation, statistics generation.
- **Sessions & Memory**: SessionManager for state, MemoryBank for long-term storage.
- **Observability**: Logging, tracing, metrics.
- **LLM Integration**: Google Gemini API for report generation.
- **Deployment**: Streamlit app for interactive use.

## Installation

```bash
git clone <repo-url>
cd dataflow-agent/deployment
python -m venv venv
source venv/bin/activate  # macOS/Linux
venv\Scripts\activate     # Windows
pip install -r requirements.txt
