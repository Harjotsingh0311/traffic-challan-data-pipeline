import streamlit as st
import pandas as pd
import os

st.set_page_config(page_title="Traffic Challan Dashboard", layout="wide")

st.title("🚦 India Traffic Challan Analytics (2015–2026)")

# Get project root directory
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Data paths
yearly_path = os.path.join(BASE_DIR, "data", "processed", "yearly_kpi.csv")
monthly_path = os.path.join(BASE_DIR, "data", "processed", "monthly_kpi.csv")
clean_path = os.path.join(BASE_DIR, "data", "processed", "clean_data.parquet")

# Load data
yearly = pd.read_csv(yearly_path)
monthly = pd.read_csv(monthly_path)
df = pd.read_parquet(clean_path)

# KPI values
total_challans = df["totalchallan"].sum()
total_amount = df["totalamount"].sum()
pending = df["pendingchallan"].sum()
disposed = df["disposedchallan"].sum()

# KPI cards
col1, col2, col3, col4 = st.columns(4)

col1.metric("Total Challans", f"{total_challans:,}")
col2.metric("Total Amount Collected", f"₹{total_amount:,}")
col3.metric("Pending Challans", f"{pending:,}")
col4.metric("Disposed Challans", f"{disposed:,}")

st.divider()

# Charts
st.subheader("Yearly Challan Trend")
st.line_chart(yearly.set_index("year"))

st.subheader("Monthly Challan Trend")
st.bar_chart(monthly.set_index("month"))

year = st.selectbox("Select Year", yearly["year"])

filtered = yearly[yearly["year"] == year]

st.line_chart(filtered.set_index("year"))