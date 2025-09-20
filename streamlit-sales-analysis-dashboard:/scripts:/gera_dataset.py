#Creating a Dataset

import random 
from datetime import datetime, timedelta
from pathlib import Path
import names
import pandas as pd
 
folder_datasets = Path(__file__).parent / "datasets"
folder_datasets.mkdir(parents=True, exist_ok=True)

STORES = [
    {"state": "Colorado" , "city" : "Denver" , "Salesperson" : ["John Miller", "James Wilson"]},
    {"state": "New York" , "city" : "New York" , "Salesperson" : ["Emilly Johnson", "Michael Brown"]},
    {"state": "Florida" , "city" : "Orlando" , "Salesperson" : ["Sarah Davis", "Olivia Taylor"]},
    {"state": "Texas" , "city" : "Austin" , "Salesperson" : ["Daniel Dean", "Jessica Moore"]},
    {"state": "Washington" , "city" : "Olympia" , "Salesperson" : ["Matthew Clark", "Ashley Harris"]},
    ]

PRODUCTS = [
    {"name" : "MacBook" , "id" : "0" ,  "price": 1299},
    {"name" : "iPad" , "id" : "1" ,  "price": 499.00},
    {"name" : "Apple Watch" , "id" : "2" ,  "price": 399},
    {"name" : "iPhone" , "id" : "3" ,  "price": 999},
    {"name" : "AirPods" , "id" : "4" ,  "price": 199},
]

PAYMENT_METHODS = [
"credit card" , "debit card", "bank transfer" , "cash"
]

CLIENTS_GENDER = ["male" , "female"]

purchases = []

for _ in range(2000):
    store = random.choice(STORES)
    seller = random.choice(store["Salesperson"])
    product = random.choice(PRODUCTS)
    purchase_time = datetime.now() - timedelta(
        days=random.randint(1, 365),
        hours = random.randint(-5, 5),
        minutes = random.randint(-30, 30)
    )
    client_gender = random.choice(CLIENTS_GENDER)
    customer_name = names.get_full_name(client_gender)
    payment_method = random.choice(PAYMENT_METHODS)

    purchases.append ({
        "date" : purchase_time , 
        "order_number" : 0 , 
        "store" : store["city"] , 
        "salesperson" : seller , 
        "products" : product["name"] , 
        "customer_name" : customer_name , 
        "client_gender" : client_gender , 
        "payment_method" : payment_method
        })

df_purchases = pd.DataFrame(purchases).set_index("date").sort_index()
df_purchases["purchase_id"] = [ i for i in range(len(df_purchases))]

df_stores = pd.DataFrame(STORES)
df_products = pd.DataFrame(PRODUCTS)

print(df_stores)
print(df_products)
print(df_purchases)

#Exporting Dataframes 

df_purchases.to_csv(folder_datasets / "purchases.csv" , decimal = "," , sep= ";" )
df_stores.to_csv(folder_datasets / "stores.csv" , decimal = "," , sep= ";" )
df_products.to_csv(folder_datasets / "products.csv" , decimal = "," , sep= ";" )

df_purchases.to_excel(folder_datasets / "purchases.xlsx" )
df_stores.to_excel(folder_datasets / "stores.xlsx" )
df_products.to_excel(folder_datasets / "products.xlsx" )