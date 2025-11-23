from tools.statistics_tool import generate_statistics
from memory.session_manager import session_manager
from memory.memory_bank import memory_bank
from observability.logger import logger
from observability.trancer import tracer

class AnalyzerAgent:

    name = "AnalyzerAgent"

    def run(self, df):
        tracer.trace(self.name, "start_analysis")

        logger.log("AnalyzerAgent: Running statistical analysis...")

        stats = generate_statistics(df)

        session_manager.update("statistics", stats)
        memory_bank.store("statistics", stats)

        tracer.trace(self.name, "completed_analysis")

        return stats
