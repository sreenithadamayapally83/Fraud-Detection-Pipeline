"""
Unit Tests for Transaction Anomaly Detection Logic
Ensures the heuristic risk-scoring engine operates correctly.
"""
import pytest

# Extracting the core heuristic logic for isolated testing
def determine_risk(latency, status):
    if latency > 180 or status == 'REJECTED':
        return 'CRITICAL'
    return 'SAFE'

# Test 1: High latency should trigger a CRITICAL alert
def test_critical_latency():
    assert determine_risk(185, 'SUCCESS') == 'CRITICAL'

# Test 2: A REJECTED status should trigger a CRITICAL alert regardless of speed
def test_rejected_status():
    assert determine_risk(50, 'REJECTED') == 'CRITICAL'

# Test 3: Normal latency and SUCCESS status should be SAFE
def test_safe_transaction():
    assert determine_risk(100, 'SUCCESS') == 'SAFE'

# Test 4: Edge case exact threshold
def test_threshold_latency():
    assert determine_risk(180, 'SUCCESS') == 'SAFE'