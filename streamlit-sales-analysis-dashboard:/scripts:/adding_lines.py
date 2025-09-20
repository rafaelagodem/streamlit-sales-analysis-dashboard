from datetime import datetime 
import streamlit as st
import pandas as pd 

pathway_datasets = "datasets"

df_purchases = pd.read_csv(f"{pathway_datasets}/purchases.csv", sep= "," , decimal= ",")
df_stores = pd.read_csv (f"{pathway_datasets}/stores.csv" , sep= ";" , decimal= ",").drop(columns=["Unnamed: 0"], errors = "ignore")
df_products = pd.read_csv (f"{pathway_datasets}/products.csv" , sep= ";" , decimal= ",").drop(columns=["Unnamed: 0"])

df_stores["city/state"] = df_stores["city"] + '/'+ df_stores["state"]
stores_list = df_stores["city/state"].to_list()
selected_store = st.sidebar.selectbox("Select store", stores_list)

salesperson_list = df_stores.loc[df_stores["city/state"] == selected_store, "Salesperson"].iloc[0]
#st.write(salesperson_list)
salesperson_list = salesperson_list.strip("][").replace(" ' " , '').split(", ")
salesperson_selected = st.sidebar.selectbox("Select salesperson:" , salesperson_list)

products_list = df_products["name"].to_list()
selected_product = st.sidebar.selectbox("Select product", products_list)


customer_name = st.sidebar.text_input("Customer name")

gender_selected= st.sidebar.selectbox("Customer gender:" , ["Male" , "Female"])

payment_method_selected= st.sidebar.selectbox("Payment method" , ["credit card" , "debit card" , "bank transfer" , "cash"])

if st.sidebar.button("Add new purchase"):
    new_row = {
        "purchase_id": df_purchases["purchase_id"].max() + 1 if not df_purchases.empty else 1,
        "state": selected_store.split("/")[1],
        "city": selected_store.split("/")[0],
        "salesperson": salesperson_selected,
        "product": selected_product,
        "customer_name": customer_name,
        "client_gender": gender_selected.lower(),
        "payment_method": payment_method_selected,
        "date": datetime.now().isoformat(timespec="seconds")
    }

    df_purchases = pd.concat([df_purchases, pd.DataFrame([new_row])], ignore_index=True)
    df_purchases.to_csv(f"{pathway_datasets}/purchases.csv", sep=",", decimal=".", index=False)

    st.success("Purchase added ✅") 
    st.dataframe(df_purchases)
