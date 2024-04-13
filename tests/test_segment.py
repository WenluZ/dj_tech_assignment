import pytest
import pandas as pd
import sys
import os

# Setting path
current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)

import main


@pytest.fixture
def sample_data():
    # Sample data for testing
    data = [
        {
            "customer_id": 1,
            "name": "John Doe",
            "email": "john@example.com",
            "purchase_amount": 40.50,
        },
        {
            "customer_id": 2,
            "name": "Jane Smith",
            "email": "jane@example.com",
            "purchase_amount": 75.20,
        },
        {
            "customer_id": 3,
            "name": "Bob Johnson",
            "email": "bob@example.com",
            "purchase_amount": 200.00,
        },
        {
            "customer_id": 3,
            "name": "Bob Johnson",
            "email": "bob@example.com",
            "purchase_amount": 400.00,
        },
        {
            "customer_id": 2,
            "name": "Jane Smith",
            "email": "jane@example.com",
            "purchase_amount": 90.20,
        },
    ]
    return data


def test_calculate_segment():
    # Test for calculate_segment function
    assert main.calculate_segment(50) == "Low"
    assert main.calculate_segment(150) == "Medium"
    assert main.calculate_segment(600) == "High"


def test_process_data(sample_data):
    # Test for process_data function
    df = pd.DataFrame(sample_data)
    processed_df = main.process_data(sample_data)

    processed_df.head(20)

    # Check if processed_df is a DataFrame
    assert isinstance(processed_df, pd.DataFrame)

    # Check if the DataFrame has the expected columns
    assert all(
        col in processed_df.columns
        for col in ["customer_id", "name", "email", "total_purchase_amount", "segment"]
    )

    # Check if the segment is calculated correctly
    assert list(processed_df.loc[processed_df["customer_id"] == 1, "segment"]) == [
        "Low"
    ]
    assert list(processed_df.loc[processed_df["customer_id"] == 2, "segment"]) == [
        "Medium"
    ]
    assert list(processed_df.loc[processed_df["customer_id"] == 3, "segment"]) == [
        "High"
    ]
