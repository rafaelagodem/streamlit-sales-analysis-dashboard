import streamlit as st
import pandas as pd

purchases_pathway = "datasets/purchases.csv"

df_purchases = pd.read_csv(purchases_pathway , sep=";" , decimal= ",")

st.dataframe(df_purchases) 