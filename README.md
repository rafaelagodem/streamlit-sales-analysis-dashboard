# 📊 Streamlit Sales Analysis Dashboard

An interactive dashboard for sales analytics built with **Streamlit** and **Pandas**, using **self-generated datasets** to simulate retail transactions, stores, and products.

---

## 🚀 Features
- Pivot table generation with dynamic indices and columns
- KPIs: total sales, total orders, commissions
- Store-level and salesperson-level analysis
- Custom datasets created to simulate realistic sales scenarios

---

## 📂 Repository Structure

```
streamlit-sales-analysis-dashboard/
│
├── datasets/                 # CSV and Excel files with synthetic sales data
│   ├── purchases.csv
│   ├── stores.csv
│   └── products.csv
│
├── scripts/                  # Python scripts for analysis and dashboard
│   ├── pivot_table.py        # Interactive pivot tables (indices/columns)
│   ├── data_volume.py        # Summary metrics (total sales, orders, commissions)
│   ├── view_tables.py        # Explore and visualize raw tables
│   ├── gera_dataset.py       # Script to generate synthetic datasets
│   ├── adding_lines.py       # Utility script for adding rows
│   └── selecting_columns.py  # Utility script for selecting/filtering columns
│
└── README.md                 # Project documentation
```

## 🛠️ Technologies
- Python 3  
- Pandas  
- Streamlit

## ⚙️ Installation & How to Run

1. Clone this repository:
```bash
git clone https://github.com/rafaelagodem/streamlit-sales-analysis-dashboard.git
cd streamlit-sales-analysis-dashboard
```

2. Install dependencies:
```bash
pip install pandas streamlit
```

3. Run one of the Streamlit apps:

**a) Pivot Tables Dashboard**
```bash
streamlit run scripts/pivot_table.py
```

**b) Summary Metrics Dashboard**
```bash
streamlit run scripts/data_volume.py
```

4. Open the local URL provided by Streamlit (something like `http://localhost:8501`) to explore the dashboard.

## 📸 Screenshots

### Pivot Tables Dashboard
Example of the interactive pivot table view:
<img width="1254" height="711" alt="Screenshot 2025-09-20 at 15 04 51" src="https://github.com/user-attachments/assets/cd6f0179-beb7-4c76-9f39-16fbd548090c" />


### Summary Metrics Dashboard
Example of the KPIs and aggregated metrics view:
![Summary Metrics Dashboard](images/data_volume_example.png)


  
🎯 Purpose
This project demonstrates my ability to:
Generate synthetic datasets
Perform data cleaning and manipulation with Pandas
Build interactive dashboards with Streamlit
