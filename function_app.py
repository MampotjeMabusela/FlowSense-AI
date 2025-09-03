import logging
import azure.functions as func
import pandas as pd
from workflow_model import WorkflowClassifier
import torch

def main(req: func.HttpRequest) -> func.HttpResponse:
    file = req.files.get("log")
    df = pd.read_csv(file)
    
    model = WorkflowClassifier(input_size=5, hidden_size=64, output_size=3)
    model.load_state_dict(torch.load("workflow_model.pt"))
    model.eval()

    input_tensor = torch.tensor(df.iloc[0:1].values, dtype=torch.float32)
    prediction = model(input_tensor).argmax().item()
    return func.HttpResponse(f"Recommended Strategy: {prediction}", status_code=200)
