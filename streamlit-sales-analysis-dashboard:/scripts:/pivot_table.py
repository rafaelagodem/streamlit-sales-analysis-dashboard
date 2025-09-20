import pandas as pd
import streamlit as st
from pathlib import Path
from datetime import timedelta

PERC_COMMISSION = 0.05
COLUMNS_ANALYSIS = ["city", "salesperson", "product", "client_gender", "payment_method"]
COLUMNS_NUMERICAL = ["price", "commission"]
AGGREGATION_FUNCTIONS = {"soma": "sum", "contagem": "count"}

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
df_purchases["commission"] = df_purchases["price"] * PERC_COMMISSION

dynamic_index = st.sidebar.multiselect("Select indices", COLUMNS_ANALYSIS)
filtered_columns = [c for c in COLUMNS_ANALYSIS if c not in dynamic_index]
dynamic_column = st.sidebar.multiselect("Select columns", filtered_columns)
value_analysis = st.sidebar.selectbox("Select value", COLUMNS_NUMERICAL)
metric_analysis = st.sidebar.selectbox("Select metric", list(AGGREGATION_FUNCTIONS.keys()))

dynamic_purchases = pd.DataFrame()

if len(dynamic_index) == 0 or len(dynamic_column) == 0:
    st.info("Select at least one option in **indices** and **columns** in the sidebar.")
    st.stop()

metric = AGGREGATION_FUNCTIONS[metric_analysis]

dynamic_purchases = pd.pivot_table(
    df_purchases,
    index=dynamic_index,
    columns=dynamic_column,
    values=value_analysis,
    aggfunc=metric
)

if dynamic_purchases.empty:
    st.info("Sem dados para as combinações escolhidas.")
    st.stop()

dynamic_purchases["GRAND_TOTAL"] = dynamic_purchases.sum(axis=1, numeric_only=True)
grand_total_col = dynamic_purchases.sum(axis=0, numeric_only=True)
dynamic_purchases.loc["GRAND_TOTAL"] = grand_total_col

st.dataframe(dynamic_purchases)
