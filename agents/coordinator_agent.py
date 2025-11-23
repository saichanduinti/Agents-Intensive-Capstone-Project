import time

from agents.cleaner_agent import CleanerAgent
from agents.analyzer_agent import AnalyzerAgent
from agents.reporter_agent import ReporterAgent

from observability.logger import logger
from observability.metrics import metrics
from observability.trancer import tracer

class CoordinatorAgent:

    name = "CoordinatorAgent"

    def __init__(self):
        self.cleaner = CleanerAgent()
        self.analyzer = AnalyzerAgent()
        self.reporter = ReporterAgent()

    def run(self, df):
        tracer.trace(self.name, "pipeline_start")
        logger.log("CoordinatorAgent: Starting full pipeline...")

        start_time = time.time()

        # 1️⃣ Cleaning phase
        cleaned = self.cleaner.run(df)

        # 2️⃣ Analysis phase
        stats = self.analyzer.run(cleaned)

        # 3️⃣ Final report generation
        report = self.reporter.run()

        # Observability
        metrics.pipeline_time = time.time() - start_time

        logger.log("CoordinatorAgent: Pipeline completed successfully.")
        logger.log(f"Total Pipeline Time: {metrics.pipeline_time:.2f} sec")

        tracer.trace(self.name, "pipeline_complete")

        return report
