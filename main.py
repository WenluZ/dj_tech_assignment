import json
import os
import pandas as pd
import sys


# Define a function to calculate segment
def calculate_segment(total_purchase_amount):
    if total_purchase_amount < 100:
        return "Low"
    elif 100 <= total_purchase_amount <= 500:
        return "Medium"
    else:
        return "High"


def process_data(data):
    try:
        df = pd.DataFrame(data)
    except ValueError:
        print("Error: Data could not be converted to DataFrame.")
        sys.exit(1)

    # Group by customer_id and calculate total purchase amount
    grouped_df = (
        df.groupby(["customer_id", "name", "email"])["purchase_amount"]
        .sum()
        .reset_index()
    )
    grouped_df.head(20)

    # Rename column
    grouped_df.rename(
        columns={"purchase_amount": "total_purchase_amount"}, inplace=True
    )

    # Apply the function to calculate segment
    grouped_df["segment"] = grouped_df["total_purchase_amount"].apply(calculate_segment)

    return grouped_df


def export_to_csv(processed_df, filename):
    # Export the final data to a CSV file
    try:
        processed_df.to_csv(f"output/{filename}", index=False)
        print("Data exported successfully to CustSeg.csv")
    except Exception as e:
        print(f"Error occurred while exporting data: {e}")


def main():
    # Check whether the input data exists
    input_data_exists = os.path.exists("data/CustData.json")
    print(f"input_data_exists: {input_data_exists}")

    if not input_data_exists:
        from src import data_generator

        cust_data = data_generator.generate_customer_data(5000)
        data_generator.write_to_json(cust_data, "data/CustData.json")
        print("CustData successfully generated.")

    try:
        with open("data/CustData.json", "r") as f:
            data = json.load(f)
    except Exception as e:
        raise ValueError(f"Error: Error occurred while reading json file : {e}")

    # Process the data
    processed_df = process_data(data)

    # Export to CSV
    export_to_csv(processed_df, "CustSeg.csv")


if __name__ == "__main__":
    main()
