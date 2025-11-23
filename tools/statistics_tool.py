import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from observability.logger import logger

def generate_statistics(df: pd.DataFrame):
    logger.log("StatisticsTool: Generating statistics...")

    summary = df.describe(include='all').to_dict()
    corr = df.corr(numeric_only=True)

    # Save heatmap
    plt.figure(figsize=(8, 6))
    sns.heatmap(corr, annot=True, cmap="coolwarm")
    plt.title("Correlation Heatmap")
    plt.tight_layout()
    plt.savefig("correlation_heatmap.png")
    plt.close()

    return {
        "summary": summary,
        "correlation_image": "correlation_heatmap.png"
    }
