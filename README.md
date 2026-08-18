# Transaction Anomaly Detection & ETL Pipeline

An end-to-end Python/SQL ETL pipeline that ingests high-concurrency financial logs, performs schema validation, and detects anomalies using a heuristic risk-scoring engine. The pipeline persists clean data to SQLite and visualizes fraud trends via an interactive Streamlit dashboard.

*This project acts as the downstream data consumer for the [Log-Aggregator Go Engine](https://github.com/sreenithadamayapally83/LOG-AGGREGATOR).*

## Core Architecture
* **ETL Pipeline (`pipeline.py`):** Ingests raw `.log` files, enforces strict data types, drops unstructured noise, and engineers a heuristic `Risk_Level` feature based on latency (>180ms) and status codes.
* **SQL Persistence:** Bypasses basic CSV dumping by enforcing a SQL Data Definition Language (DDL) schema and persisting the cleaned records to a relational `SQLite` database.
* **Ops Dashboard (`app.py`):** An interactive Streamlit web application that queries the SQL database to visualize fraud distribution and provides one-click enterprise audit CSV downloads.
* **Automated Testing (`test_pipeline.py`):** Uses `pytest` to strictly validate the heuristic scoring logic against edge cases.
* **Containerization (`Dockerfile`):** Fully containerized deployment architecture for cross-environment consistency.

## How to Run

**1. Run the ETL Pipeline (Data Cleaning & SQL Persistence)**
```bash
python pipeline.py
Generates fraud_audit.db.

**2. Launch the Streamlit Dashboard**
```bash
pip install streamlit pandas
streamlit run app.py

**3. Run Unit Tests**
```bash
pip install pytest
pytest test_pipeline.py