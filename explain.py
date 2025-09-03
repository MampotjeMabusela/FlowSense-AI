import shap
import torch
import pandas as pd
from workflow_model import WorkflowClassifier

df = pd.read_csv("sample_log.csv")
model = WorkflowClassifier(input_size=5, hidden_size=64, output_size=3)
model.load_state_dict(torch.load("workflow_model.pt"))
model.eval()

explainer = shap.Explainer(model, torch.tensor(df.values, dtype=torch.float32))
shap_values = explainer(torch.tensor(df.values, dtype=torch.float32))

shap.plots.waterfall(shap_values[0])
