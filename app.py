"""
Streamlit Dashboard for Transaction Anomaly Detection
Queries the SQL database and visualizes fraud trends for Ops Teams.
"""
import streamlit as st
import pandas as pd
import sqlite3

# Connect to the SQL database we generated in Phase 1
@st.cache_data
def load_data():
    conn = sqlite3.connect("fraud_audit.db")
    df = pd.read_sql_query("SELECT * FROM audited_transactions", conn)
    conn.close()
    return df

# Configure the UI
st.set_page_config(page_title="Ops Dashboard: Fraud Detection", layout="wide")
st.title("Transaction Anomaly & Risk Dashboard")

try:
    df = load_data()
    
    # --- Top Level KPIs ---
    total_txns = len(df)
    critical_txns = len(df[df['Risk_Level'] == 'CRITICAL'])
    health_pct = ((total_txns - critical_txns) / total_txns) * 100 if total_txns > 0 else 0
    
    col1, col2, col3 = st.columns(3)
    col1.metric("Total Processed Logs", f"{total_txns:,}")
    col2.metric("Critical Anomalies Blocked", f"{critical_txns:,}")
    col3.metric("System Health", f"{health_pct:.2f}%")
    
    st.divider()

    # --- Visualizations ---
    st.subheader("Fraud Trend: Risk Level Distribution")
    # A simple interactive bar chart
    risk_counts = df['Risk_Level'].value_counts()
    st.bar_chart(risk_counts)
    
    st.divider()

    # --- Interactive Audit Report Download ---
    st.subheader("Ops Team Audit Log")
    st.write("Previewing top 100 critical transactions:")
    
    # Filter for criticals to show the ops team what went wrong
    critical_df = df[df['Risk_Level'] == 'CRITICAL']
    st.dataframe(critical_df.head(100), use_container_width=True)
    
    # The crucial "download audit reports" feature from your resume
    csv = df.to_csv(index=False).encode('utf-8')
    st.download_button(
        label="Download Full Audit CSV",
        data=csv,
        file_name='enterprise_audit_report.csv',
        mime='text/csv',
    )
    
except Exception as e:
    st.error(f"Database Error: {e}. Please ensure you run pipeline.py first to generate fraud_audit.db")