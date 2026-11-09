import pickle, pandas as pd

clf = pickle.load(open("models/model.pkl", "rb"))
print("model classes:", clf.classes_)
print("train labels:", pd.read_csv("data/processed/train_bow.csv").iloc[:, -1].unique())
print("test labels:", pd.read_csv("data/processed/test_bow.csv").iloc[:, -1].unique())