import pandas as pd

INPUT = "data/processed/combined_data.parquet"

OUTPUT = "data/processed/clean_data.parquet"


def clean_data():

    df = pd.read_parquet(INPUT)

    df.drop_duplicates(inplace=True)

    df.fillna(0, inplace=True)

    df.columns = df.columns.str.lower().str.replace(" ", "_")

    return df


if __name__ == "__main__":

    df = clean_data()

    df.to_parquet(OUTPUT)

    print("Data cleaned")