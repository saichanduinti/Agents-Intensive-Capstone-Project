from tools.dataset_validator import validate_dataset
from tools.data_cleaner_tool import clean_dataset
from memory.session_manager import session_manager
from memory.memory_bank import memory_bank
from observability.logger import logger
from observability.trancer import tracer

class CleanerAgent:

    name = "CleanerAgent"

    def run(self, df):
        tracer.trace(self.name, "start_cleaning")

        logger.log("CleanerAgent: Starting validation + cleaning pipeline...")

        validation = validate_dataset(df)
        cleaned_df = clean_dataset(df)

        session_manager.update("validation", validation)
        session_manager.update("cleaned_df", cleaned_df)

        memory_bank.store("cleaning_result", validation)

        tracer.trace(self.name, "completed_cleaning")

        return cleaned_df
