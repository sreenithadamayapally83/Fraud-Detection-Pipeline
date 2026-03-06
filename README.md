# Real-Time Fraud Detection & Data Pipeline (Python)
## Overview
This project implements a high-speed data transformation and heuristic fraud detection pipeline. It is designed to ingest raw transaction telemetry—simulating the massive data throughput and identify critical anomalies in real-time.

As an ECE student, I focused on the intersection of Signal Processing logic and Data Science to build a system that prioritizes both accuracy and processing speed.

## Key Technical Achievements
End-to-End Data Pipeline: Successfully integrated with a Go-based high-concurrency engine to process and clean 100,000+ raw transaction records.

Advanced Data Transformation: Leveraged Pandas to parse unstructured log data, perform type conversion, and engineer a "Risk Scoring" feature.

Heuristic Fraud Detection: Developed logic to flag "Critical" anomalies based on system latency thresholds and transaction status codes, simulating real-world risk management.

## Features
Automated Data Cleaning: Removes noise and standardizes raw string data into a structured format for analysis.

Latency-Based Alerting: Specifically identifies transactions with high latency (>180ms), which often indicate system bottlenecks or fraudulent interference.

Scalable Reporting: Generates a professional fraud_alerts.csv report for downstream "Model Serving" or manual audit by risk teams.

## Tech Stack
Language: Python 3.x
Libraries: Pandas (Data Manipulation), OS (File Handling)
Concepts: Data Pipelines, Anomaly Detection, System Reliability

Libraries: Pandas (Data Manipulation), OS (File Handling)

Concepts: Data Pipelines, Anomaly Detection, System Reliability
