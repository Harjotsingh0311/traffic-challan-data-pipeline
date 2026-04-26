import pandas as pd
import os

RAW_PATH = "data/raw"
OUTPUT_PATH = "data/processed"

def load_data():

    files = os.listdir(RAW_PATH)

    dataframes = []

    for file in files:
        if file.endswith(".csv"):
            df = pd.read_csv(os.path.join(RAW_PATH, file))
            dataframes.append(df)

    data = pd.concat(dataframes, ignore_index=True)

    print("Total Records:", len(data))

    return data


if __name__ == "__main__":

    data = load_data()

    data.to_parquet(f"{OUTPUT_PATH}/combined_data.parquet")

    print("Data ingestion completed")