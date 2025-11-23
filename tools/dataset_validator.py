import pandas as pd
from observability.logger import logger
from observability.metrics import metrics

def validate_dataset(df: pd.DataFrame):
    logger.log("DatasetValidator: Validating dataset...")
    
    metrics.increment_rows(len(df))

    return {
        "rows": len(df),
        "columns": len(df.columns),
        "missing_values": df.isnull().sum().to_dict(),
        "dtypes": df.dtypes.astype(str).to_dict(),
    }
