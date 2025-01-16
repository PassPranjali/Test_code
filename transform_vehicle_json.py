import pandas as pd
import json
import os

def transform_vehicle_to_json(input_csv, output_json):
    # Load CSV
    df = pd.read_csv(input_csv)

    # Validate and transform
    df['RegistrationDate'] = pd.to_datetime(df['RegistrationDate'], errors='coerce').dt.strftime("%Y-%m-%dT%H:%M:%S").fillna("1970-01-01")
    df['Price'] = pd.to_numeric(df['Price'], errors='coerce').fillna(0.0)
    df['Device'] = df['Device'].fillna("Unknown")
    df['IssueDescription'] = df['IssueDescription'].fillna("No Description Provided")
    df['Status'] = df['Status'].fillna("Unknown Status")

    # Select relevant columns
    selected_columns = ['VehicleID', 'RegistrationDate', 'Price', 'Device', 'IssueDescription', 'Status']
    df = df[selected_columns]

    # Convert to JSON
    json_data = df.to_dict(orient='records')
    with open(output_json, 'w') as f:
        json.dump(json_data, f, indent=4)
    print(f"Transformed {input_csv} to {output_json}")

# Input and output paths
input_csv = "upload/vehicle.csv"
output_json = "upload/vehicle.json"

# Transform vehicle CSV to JSON
transform_vehicle_to_json(input_csv, output_json)
