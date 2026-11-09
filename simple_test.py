import pandas as pd
print(pd.read_csv("data/processed/test_bow.csv").iloc[:, -1].unique())