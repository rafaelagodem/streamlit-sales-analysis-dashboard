import pandas as pd
import streamlit as st
from pathlib import Path
from datetime import timedelta

datasets_path = Path("datasets")

df_purchases = pd.read_csv(
    datasets_path / "purchases.csv",
    sep=",",
    decimal=".",
    parse_dates=["date"]
)

df_stores = pd.read_csv(datasets_path / "stores.csv", sep=";", decimal=",")
df_products = pd.read_csv(datasets_path / "products.csv", sep=";", decimal=",")

for df in (df_purchases, df_stores, df_products):
    if "Unnamed: 0" in df.columns:
        df.drop(columns=["Unnamed: 0"], inplace=True)

if "name" in df_products.columns:
    df_products.rename(columns={"name": "product"}, inplace=True)

df_purchases = df_purchases.set_index("date")
df_purchases.index = pd.to_datetime(df_purchases.index, errors="coerce")
df_purchases = df_purchases[~df_purchases.index.isna()]

data_default = df_purchases.index.max().date()
df_purchases["commission"] = df_purchases["price"] * 0.05

with st.sidebar.form("filters"):
    start_date = st.date_input("Start date", data_default - timedelta(days=6))
    final_date = st.date_input("Final date", data_default)
    submitted = st.form_submit_button("Search")

if not submitted:
    st.info("Set the dates and click **Search**.")
    st.stop()

if start_date > final_date:
    st.error("Start date must be on or before Final date.")
    st.stop()

start_ts = pd.Timestamp(start_date)
end_ts = pd.Timestamp(final_date) + timedelta(days=1)
df_purchases_filter = df_purchases[(df_purchases.index >= start_ts) & (df_purchases.index < end_ts)]

if df_purchases_filter.empty:
    st.info("No purchases in the selected period.")
    st.stop()

st.markdown("# Summary Metrics")
col1, col2 = st.columns(2)

sales_value = df_purchases_filter["price"].sum()
col1.metric("Total Sales Value", f"${sales_value:,.2f}")
col2.metric("Total Orders", df_purchases_filter["price"].count())

st.divider()

vc_store = df_purchases_filter["city"].value_counts()
if not vc_store.empty:
    main_store = vc_store.index[0]
    st.markdown(f"# Main Store: {main_store}")
    col21, col22 = st.columns(2)

    value_purchases_store = df_purchases_filter[df_purchases_filter["city"] == main_store]["price"].sum()
    col21.metric("Total purchase value", f"${value_purchases_store:,.2f}")
    quantity_store_purchases = df_purchases_filter[df_purchases_filter["city"] == main_store]["price"].count()
    col22.metric("Total number of purchases during the period", quantity_store_purchases)

st.divider()

vc_seller = df_purchases_filter["salesperson"].value_counts()
if not vc_seller.empty:
    main_seller = vc_seller.index[0]
    st.markdown(f"# Main seller: {main_seller}")

    seller_purchase_value = df_purchases_filter[df_purchases_filter["salesperson"] == main_seller]["price"].sum()
    seller_comission_value = df_purchases_filter[df_purchases_filter["salesperson"] == main_seller]["commission"].sum()

    col31, col32 = st.columns(2)
    col31.metric("Total purchase value in the period", f"${seller_purchase_value:,.2f}")
    col32.metric("Total commission in the period", f"${seller_comission_value:,.2f}")
