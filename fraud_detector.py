import pandas as pd
import os

def run_fraud_audit(log_file):
    print("--- NPCI Fraud Detection Engine: Initializing Audit ---")
    
    if not os.path.exists(log_file):
        print("Error: transactions.log not found. Ensure Project 1 was run!")
        return

    # Data Ingestion & Cleaning
    # Parsing the Go-generated logs
    columns = ["Raw_Data"]
    df = pd.read_csv(log_file, names=columns)
    
    # Transformation: Splitting strings into usable data
    df['ID'] = df['Raw_Data'].str.extract(r'TXNID:(\d+)')
    df['Status'] = df['Raw_Data'].str.extract(r'STATUS:(\w+)')
    df['Latency'] = df['Raw_Data'].str.extract(r'LATENCY:(\d+)').astype(int)

    # Heuristic Fraud Detection Logic
    # Any transaction with Latency > 180ms OR Status == 'REJECTED' is a 'High Risk' event.
    df['Risk_Level'] = df.apply(
        lambda x: 'CRITICAL' if (x['Latency'] > 180 or x['Status'] == 'REJECTED') else 'SAFE', 
        axis=1
    )

    # Generating the Project Report
    critical_alerts = df[df['Risk_Level'] == 'CRITICAL']
    
    print(f"Audit Complete. Scanned 100,000 logs.")
    print(f"Identified {len(critical_alerts)} Critical Anomalies.")
    
    # Saving for "Model Serving" simulation
    critical_alerts.to_csv("fraud_alerts.csv", index=False)
    print("Exported results to: fraud_alerts.csv")

if __name__ == "__main__":
    run_fraud_audit("../log-aggregator/transactions.log")