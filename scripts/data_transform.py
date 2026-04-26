import pandas as pd

INPUT = "data/processed/clean_data.parquet"


def create_kpis():

    # Load dataset
    df = pd.read_parquet(INPUT)

    # Convert date column to datetime
    df["date"] = pd.to_datetime(df["date"])

    # Extract year and month
    df["year"] = df["date"].dt.year
    df["month"] = df["date"].dt.month

    # ===== BASIC KPIs =====

    total_challans = df["totalchallan"].sum()
    total_amount = df["totalamount"].sum()
    pending_challans = df["pendingchallan"].sum()
    disposed_challans = df["disposedchallan"].sum()

    print("\nTOTAL CHALLANS:")
    print(total_challans)

    print("\nTOTAL AMOUNT COLLECTED:")
    print(total_amount)

    print("\nTOTAL PENDING CHALLANS:")
    print(pending_challans)

    print("\nTOTAL DISPOSED CHALLANS:")
    print(disposed_challans)

    # ===== YEARLY TREND =====

    yearly = df.groupby("year")["totalchallan"].sum().reset_index()

    print("\nYEARLY CHALLAN TREND:")
    print(yearly)

    # ===== MONTHLY TREND =====

    monthly = df.groupby("month")["totalchallan"].sum().reset_index()

    print("\nMONTHLY CHALLAN TREND:")
    print(monthly)

    # ===== COURT CASES =====

    court_cases = df[["pendingcourt", "disposedcourt", "totalcourt"]].sum()

    print("\nCOURT CASES:")
    print(court_cases)

    # ===== SAVE KPI FILES =====

    yearly.to_csv("data/processed/yearly_kpi.csv", index=False)
    monthly.to_csv("data/processed/monthly_kpi.csv", index=False)

    print("\nKPI files saved successfully!")


if __name__ == "__main__":
    create_kpis()