import pandas as pd

df = pd.read_csv("simulation_results.csv")
df.to_excel("powerbi_export.xlsx", index=False)
