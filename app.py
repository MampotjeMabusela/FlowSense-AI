import streamlit as st
import torch
import pandas as pd
from workflow_model import WorkflowClassifier

st.title("FlowSense AI — Workflow Automation Advisor")

uploaded_file = st.file_uploader("Upload system log (CSV)", type="csv")
if uploaded_file:
    df = pd.read_csv(uploaded_file)
    st.write("Preview:", df.head())

    # Simulate automation ROI
    st.subheader("Simulated ROI")
    efficiency_gain = df["task_duration"].mean() * 0.25
    st.metric("Estimated Time Saved", f"{efficiency_gain:.2f} mins/task")

    # Predict automation category
    model = WorkflowClassifier(input_size=5, hidden_size=64, output_size=3)
    model.load_state_dict(torch.load("workflow_model.pt"))
    model.eval()

    input_tensor = torch.tensor(df.iloc[0:1].values, dtype=torch.float32)
    prediction = model(input_tensor).argmax().item()
    categories = ["Manual", "Semi-Automated", "Fully Automated"]
    st.success(f"Recommended Strategy: {categories[prediction]}")
