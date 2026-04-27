# 🚦 Traffic Challan Data Engineering Pipeline (India 2015–2026)

An **end-to-end Data Engineering pipeline** that processes **416M+ Indian traffic e-challan records** to generate analytical insights and visualize enforcement trends using an interactive dashboard.

This project demonstrates core **modern data engineering concepts** including:

* ETL pipeline design
* Data cleaning and preprocessing
* Data transformation and aggregation
* Data quality validation
* Exploratory data analysis
* Interactive analytics dashboards
* Containerized deployment using Docker
* Conceptual workflow orchestration using Apache Airflow

---

# 📊 Dashboard Preview

*(Add a screenshot of your dashboard inside the `assets` folder)*

```
assets/dashboard.png
```

Example:

![Dashboard](assets/dashboard.png)

---

# 📦 Dataset

Dataset: **Indian Traffic E-Challan Dataset (2015–2026)**

Total Records Processed:

**416,513,606 Challans**

Dataset Fields:

| Column          | Description           |
| --------------- | --------------------- |
| date            | Date of record        |
| totalchallan    | Total challans issued |
| disposedchallan | Resolved challans     |
| pendingchallan  | Pending challans      |
| pendingamount   | Pending fine amount   |
| disposedamount  | Amount recovered      |
| totalamount     | Total fine amount     |
| pendingcourt    | Pending court cases   |
| disposedcourt   | Resolved court cases  |
| totalcourt      | Total court cases     |

---

# 🏗 System Architecture

```
Raw Dataset (CSV)
        │
        ▼
Data Ingestion
(Python Scripts)
        │
        ▼
Data Cleaning
        │
        ▼
Data Transformation
(KPI Aggregation)
        │
        ▼
Data Quality Validation
        │
        ▼
Parquet Data Storage
        │
        ▼
Streamlit Dashboard
        │
        ▼
Docker Deployment
```

---

# 📂 Project Structure

```
traffic-challan-data-pipeline
│
├── dags
│   └── traffic_pipeline_dag.py
│
├── dashboard
│   └── app.py
│
├── scripts
│   ├── data_ingestion.py
│   ├── data_cleaning.py
│   ├── data_transform.py
│   └── data_quality.py
│
├── notebooks
│   └── eda.ipynb
│
├── data
│   ├── raw
│   └── processed
│
├── assets
│   └── dashboard.png
│
├── Dockerfile
├── requirements.txt
└── README.md
```

---

# ⚙️ Prerequisites

Install the following:

* Python **3.10+**
* pip
* Git
* Docker *(optional)*

---

# 📥 Clone the Repository

```
git clone https://github.com/<your-username>/traffic-challan-data-pipeline.git
cd traffic-challan-data-pipeline
```

---

# 📊 Dataset Setup

Download dataset from:

https://www.kaggle.com/datasets/bhanageviraj/indian-traffic-e-challan-daily-dataset-20152026

Place the dataset file inside:

```
data/raw/
```

Example:

```
data
 ├── raw
 │   └── challan_dataset.csv
 └── processed
```

---

# 🖥 Installation

Create virtual environment

```
python -m venv venv
```

Activate environment

### Windows

```
venv\Scripts\activate
```

### Mac/Linux

```
source venv/bin/activate
```

Install dependencies

```
pip install -r requirements.txt
```

---

# 🔄 Run the ETL Pipeline

### Step 1 – Data Ingestion

```
python scripts/data_ingestion.py
```

---

### Step 2 – Data Cleaning

```
python scripts/data_cleaning.py
```

---

### Step 3 – Data Transformation

```
python scripts/data_transform.py
```

This generates:

```
data/processed/clean_data.parquet
data/processed/yearly_kpi.csv
data/processed/monthly_kpi.csv
```

---

### Step 4 – Data Quality Validation

```
python scripts/data_quality.py
```

---

# 📊 Run the Dashboard

```
streamlit run dashboard/app.py
```

Open browser:

```
http://localhost:8501
```

Dashboard shows:

* Total challans issued
* Revenue collected
* Pending vs disposed challans
* Yearly enforcement trends
* Monthly challan distribution

---

# 🐳 Run Using Docker

Build Docker image:

```
docker build -t traffic-pipeline .
```

Run container:

```
docker run -p 8501:8501 traffic-pipeline
```

Open:

```
http://localhost:8501
```

---

# 📊 Exploratory Data Analysis

EDA notebook:

```
notebooks/eda.ipynb
```

Includes:

* Dataset inspection
* Trend visualization
* Monthly distribution analysis
* Pending vs disposed analysis

---

# 🔁 Workflow Orchestration

An example **Apache Airflow DAG** demonstrates pipeline orchestration.

Location:

```
dags/traffic_pipeline_dag.py
```

Pipeline tasks:

1. Data ingestion
2. Data cleaning
3. Data transformation
4. Data validation

---

# 📈 Key Insights

Analysis shows:

* Significant increase in traffic challans after **2019**
* Peak enforcement activity in **2025**
* Large backlog of unresolved challans
* Seasonal patterns in monthly enforcement

---

# 🧰 Technologies Used

| Technology       | Purpose                   |
| ---------------- | ------------------------- |
| Python           | Data pipeline development |
| Pandas           | Data processing           |
| Parquet          | Efficient data storage    |
| Streamlit        | Dashboard                 |
| Docker           | Containerized deployment  |
| Jupyter Notebook | EDA                       |
| Apache Airflow   | Workflow orchestration    |

---

# 🚀 Future Improvements

Possible extensions:

* Real-time streaming using Apache Kafka
* Distributed processing using Apache Spark
* Data warehouse integration (PostgreSQL / BigQuery)
* Cloud deployment using AWS or GCP

---

# 👨‍💻 Author

Harjot Singh
B.Tech Artificial Intelligence Machine Learning
Thapar Institute of Engineering and Technology

---
