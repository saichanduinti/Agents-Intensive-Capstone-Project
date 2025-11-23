import json
from datetime import datetime
from agents.base_llm import call_gemini
from memory.session_manager import session_manager
from memory.memory_bank import memory_bank
from observability.logger import logger
from observability.trancer import tracer

class ReporterAgent:

    name = "ReporterAgent"

    def run(self):
        tracer.trace(self.name, "start_reporting")

        logger.log("ReporterAgent: Generating final data report using Gemini...")

        validation = session_manager.get("validation")
        stats = session_manager.get("statistics")

        # Get current date
        current_date = datetime.today().strftime("%B %d, %Y")  # e.g., November 15, 2025

        prompt = f"""
        You are a data reporting agent. 
        Create a clear, professional report summarizing the dataset.

        ### Date
        {current_date}

        ### Dataset Validation
        {json.dumps(validation, indent=2)}

        ### Statistical Summary
        {json.dumps(stats["summary"], indent=2)}

        Provide:
        - High-level observations
        - Data quality evaluation
        - Key insights from the statistics
        - Recommended next analysis steps
        """

        report = call_gemini(prompt)

        session_manager.update("final_report", report)
        memory_bank.store("report", report)

        tracer.trace(self.name, "completed_reporting")

        return report
