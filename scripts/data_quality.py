import pandas as pd

df = pd.read_parquet("data/processed/clean_data.parquet")

assert df["totalchallan"].isnull().sum() == 0

print("Data quality check passed")