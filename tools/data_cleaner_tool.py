import pandas as pd
import numpy as np
from observability.logger import logger

def clean_dataset(df: pd.DataFrame):
    logger.log("DataCleaner: Cleaning dataset...")

    cleaned = df.copy()

    # Numeric columns → fill NA with median
    num_cols = cleaned.select_dtypes(include=[np.number]).columns
    cleaned[num_cols] = cleaned[num_cols].fillna(cleaned[num_cols].median())

    # Categorical columns → fill NA with mode
    cat_cols = cleaned.select_dtypes(include=['object']).columns
    for col in cat_cols:
        cleaned[col] = cleaned[col].fillna(cleaned[col].mode().iloc[0])

    return cleaned
