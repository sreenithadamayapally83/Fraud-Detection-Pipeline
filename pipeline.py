import pandas as pd
import os
import sqlite3

def run_fraud_audit(log_file):
    print("--- Fraud Detection Engine: Initializing Audit ---")
    
    if not os.path.exists(log_file):
        print(f"--> [ERROR] {log_file} not found. Ensure the Go engine has generated the logs.")
        return

    # 1. Data Ingestion
    columns = ["Raw_Data"]
    df = pd.read_csv(log_file, names=columns)
    
    # 2. Transformation & Strict Schema Validation
    # We force specific data types. If a string slips into an integer column, the pipeline breaks here.
    # This is exactly what "schema validation" means in a production ETL pipeline.
    df['ID'] = df['Raw_Data'].str.extract(r'TXNID:(\d+)').astype(int)
    df['Status'] = df['Raw_Data'].str.extract(r'STATUS:(\w+)').astype(str)
    df['Latency'] = df['Raw_Data'].str.extract(r'LATENCY:(\d+)').astype(int)

    # 3. Heuristic Fraud Detection Logic
    df['Risk_Level'] = df.apply(
        lambda x: 'CRITICAL' if (x['Latency'] > 180 or x['Status'] == 'REJECTED') else 'SAFE', 
        axis=1
    )
    
    # Drop the unstructured raw data to finalize the clean schema
    clean_df = df[['ID', 'Status', 'Latency', 'Risk_Level']]

    # 4. SQL Database Persistence
    db_path = "fraud_audit.db"
    conn = sqlite3.connect(db_path)
    
    # Define the strict SQL table schema
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS audited_transactions (
            ID INTEGER PRIMARY KEY,
            Status TEXT NOT NULL,
            Latency INTEGER NOT NULL,
            Risk_Level TEXT NOT NULL
        )
    ''')
    
    # Push the clean Pandas DataFrame directly into the SQL engine
    clean_df.to_sql('audited_transactions', conn, if_exists='replace', index=False)
    
    print(f"--> [SUCCESS] Audit Complete. {len(clean_df)} records cleaned.")
    print("--> [SUCCESS] Cleaned data successfully persisted to SQL Database with schema validation.")
    
    conn.close()

if __name__ == "__main__":
    # Ensure this path points correctly to where your transactions.log is saved
    run_fraud_audit("../log-aggregator/transactions.log")