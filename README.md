# 🚦 Traffic Challan Data Engineering Pipeline (India 2015–2026)

An end-to-end **Data Engineering project** that processes **416M+ Indian traffic e-challan records** to build a scalable ETL pipeline, perform analytics, and visualize enforcement trends using an interactive dashboard.

This project demonstrates the **core concepts of modern data engineering**, including data ingestion, transformation, validation, orchestration, data modeling, analytics, and containerized deployment.

---

# 📊 Project Overview

Traffic enforcement generates massive datasets that contain valuable insights about road safety, policy enforcement, and administrative efficiency.

This project builds a **complete data pipeline** to process historical e-challan data and generate analytical insights.

The pipeline:

1. Ingests raw enforcement data
2. Cleans and validates records
3. Generates KPI aggregations
4. Stores processed datasets
5. Visualizes insights through a dashboard
6. Demonstrates orchestration using Airflow DAGs
7. Deploys the dashboard using Docker containers

---

# 📦 Dataset

Dataset Source:

Indian Traffic E-Challan Dataset (2015-2026)

Total Records Processed:

**416,513,606 challans**

Dataset Fields:

| Column          | Description                   |
| --------------- | ----------------------------- |
| date            | Daily enforcement record date |
| totalchallan    | Total challans issued         |
| disposedchallan | Challans resolved             |
| pendingchallan  | Challans pending              |
| pendingamount   | Total pending fine amount     |
| disposedamount  | Amount recovered              |
| totalamount     | Total fine amount             |
| pendingcourt    | Cases pending in court        |
| disposedcourt   | Cases resolved in court       |
| totalcourt      | Total court cases             |

---

# 🏗 System Architecture

The project follows a simplified **Modern Data Engineering Architecture**.

```
Raw Dataset (CSV)
        │
        ▼
Data Ingestion
(Python Scripts)
        │
        ▼
Data Cleaning & Validation
        │
        ▼
Data Transformation
(KPI Aggregations)
        │
        ▼
Parquet Data Lake
        │
        ▼
Analytics Layer
(Streamlit Dashboard)
        │
        ▼
Docker Deployment
```

Optional orchestration is demonstrated through **Apache Airflow DAGs**.

---

# ⚙️ Project Structure

```
TRAFFIC_DATA_PIPELINE
│
├── dags
│   └── traffic_pipeline_dag.py
│
├── dashboard
│   └── app.py
│
├── data
│   ├── raw
│   └── processed
│
├── logs
│
├── notebooks
│   └── eda.ipynb
│
├── pipelines
│
├── scripts
│   ├── data_ingestion.py
│   ├── data_cleaning.py
│   ├── data_transform.py
│   └── data_quality.py
│
├── Dockerfile
├── requirements.txt
└── README.md
```

---

# 🔄 ETL Pipeline

The project implements a standard **ETL workflow**.

### Extract

Raw challan data is ingested from the dataset source.

Script:

```
scripts/data_ingestion.py
```

Responsibilities:

* Load raw dataset
* Convert file formats
* Store raw records

---

### Transform

Data is cleaned and standardized.

Script:

```
scripts/data_cleaning.py
```

Operations performed:

* Handling missing values
* Standardizing column names
* Removing duplicates
* Converting date formats

---

### Data Quality Validation

Script:

```
scripts/data_quality.py
```

Validation checks:

* Null value checks
* Schema validation
* Data integrity checks

---

### Aggregation & KPI Generation

Script:

```
scripts/data_transform.py
```

Key KPIs generated:

* Total challans issued
* Total fines collected
* Pending vs disposed challans
* Yearly enforcement trends
* Monthly enforcement patterns

Output files:

```
yearly_kpi.csv
monthly_kpi.csv
clean_data.parquet
```

---

# 📈 Exploratory Data Analysis

EDA was conducted using Jupyter notebooks.

Location:

```
notebooks/eda.ipynb
```

Analysis includes:

* Dataset inspection
* Yearly challan trends
* Monthly challan distribution
* Pending vs resolved challans
* Data visualization

---

# 📊 Dashboard

An interactive dashboard built using **Streamlit** provides insights into enforcement patterns.

Location:

```
dashboard/app.py
```

Features:

* KPI summary cards
* Yearly challan trends
* Monthly challan distribution
* Pending vs resolved statistics

Dashboard preview:

Key insights include:

* Rapid growth in challan issuance after 2019
* Peak enforcement in 2025
* Significant backlog of unresolved challans

---

# 🔁 Workflow Orchestration

The pipeline includes an example **Apache Airflow DAG** to demonstrate orchestration of ETL tasks.

Location:

```
dags/traffic_pipeline_dag.py
```

Workflow tasks:

1. Data ingestion
2. Data cleaning
3. Data transformation
4. Data validation

Even though Airflow is not executed on Windows environments, the DAG demonstrates how the pipeline would run in a production system.

---

# 🐳 Docker Deployment

The dashboard is containerized using Docker.

Dockerfile defines:

* Python runtime
* Dependency installation
* Dashboard launch

Run the container:

```
docker build -t traffic-pipeline .
docker run -p 8501:8501 traffic-pipeline
```

Access dashboard:

```
http://localhost:8501
```

---

# 📊 Key Findings

Analysis of the dataset reveals several trends:

### Growth in Enforcement

Traffic challans increased significantly after 2019 due to digital enforcement systems and stricter traffic policies.

### High Pending Cases

A large proportion of challans remain unresolved, indicating administrative backlog.

### Seasonal Patterns

Monthly analysis suggests variation in enforcement intensity across the year.

---

# 🧠 Data Modeling

Conceptual star schema for analytics:

```
Fact Table
Traffic_Challan_Facts
    totalchallan
    disposedchallan
    pendingchallan
    totalamount
    date_key

Dimension Tables
Date_Dimension
State_Dimension
Violation_Dimension
```

This structure allows efficient OLAP-style analysis.

---

# 🧰 Technologies Used

| Technology       | Purpose                             |
| ---------------- | ----------------------------------- |
| Python           | Data pipeline implementation        |
| Pandas           | Data processing                     |
| Parquet          | Efficient columnar storage          |
| Streamlit        | Analytics dashboard                 |
| Docker           | Containerized deployment            |
| Jupyter Notebook | Exploratory data analysis           |
| Apache Airflow   | Workflow orchestration (conceptual) |

---

# 🎯 Learning Outcomes

This project demonstrates the following **data engineering concepts**:

* ETL pipeline design
* Data transformation workflows
* Data quality validation
* Batch data processing
* Data modeling concepts
* Analytics dashboards
* Containerized deployment
* Workflow orchestration

---

# 🚀 Future Improvements

Possible extensions include:

* Real-time streaming using Apache Kafka
* Distributed processing with Apache Spark
* Data warehouse integration (PostgreSQL / BigQuery)
* Cloud deployment using AWS or GCP
* Automated monitoring and alerting

---

# 📚 Academic Relevance

This project aligns with course topics including:

* Data engineering foundations
* Data modeling
* ETL pipeline design
* Workflow orchestration
* Big data concepts
* Data governance
* DevOps practices for data platforms

---

# 👨‍💻 Author

Harjot Singh
B.Tech Artificial Intelligence Machine Learning
Thapar Institute of Engineering and Technology

---
