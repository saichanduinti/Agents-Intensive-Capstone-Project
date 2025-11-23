import streamlit as st
import pandas as pd
from agents.coordinator_agent import CoordinatorAgent
from observability.logger import logger

st.set_page_config(page_title="DataFlow Automation Agent", layout="wide")

st.title("DataFlow Automation Agent")
st.write("Upload your dataset and let the multi-agent pipeline handle cleaning, analysis, and report generation.")

uploaded_file = st.file_uploader("Upload CSV dataset", type=["csv"])

if uploaded_file:
    df = pd.read_csv(uploaded_file)
    st.write("Dataset Preview:")
    st.dataframe(df.head())

    if st.button("Run DataFlow Pipeline"):
        coordinator = CoordinatorAgent()
        report = coordinator.run(df)

        st.success("Pipeline completed successfully!")
        st.subheader("Generated Report")
        st.text(report)
