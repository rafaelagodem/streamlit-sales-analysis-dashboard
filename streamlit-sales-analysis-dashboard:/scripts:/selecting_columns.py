import streamlit as st 
import pandas as pd 

file_pathway = "datasets/purchases.csv"
df_purchases = pd.read_csv(file_pathway, sep = ";" , decimal = "," , index_col=0)

columns = list(df_purchases.columns)

selected_columns = st.sidebar.multiselect("select columns" , columns , columns)

col1, col2 = st.sidebar.columns(2)

col_filter = col1.selectbox("Select Column",
             [c for c in columns if c not in ["purchase_id"]])
value_filter = col2.selectbox("Selecione o valor" ,
                              list(df_purchases[col_filter].unique()))

st_filter = col1.button("Filter")
st_clean = col2.button ("Clean")

if st_filter:
    st.dataframe(df_purchases.loc[df_purchases[col_filter] == value_filter, selected_columns])
elif st_clean:
    st.dataframe(df_purchases[selected_columns])
else:
    st.dataframe(df_purchases[selected_columns])