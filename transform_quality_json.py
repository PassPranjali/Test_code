import pandas as pd
import json
import os

def transform_quality_to_json(input_csv, output_json):
    # Load CSV
    df = pd.read_csv(input_csv)

    # Validate and transform
    df['InspectionDate'] = pd.to_datetime(df['InspectionDate'], errors='coerce').dt.strftime("%Y-%m-%dT%H:%M:%S").fillna("1970-01-01")
    df['Score'] = pd.to_numeric(df['Score'], errors='coerce').fillna(0.0)

    # Select relevant columns
    selected_columns = ['QualityID', 'InspectionDate', 'Score']
    df = df[selected_columns]

    # Convert to JSON
    json_data = df.to_dict(orient='records')
    with open(output_json, 'w') as f:
        json.dump(json_data, f, indent=4)
    print(f"Transformed {input_csv} to {output_json}")

# Input and output paths
input_csv = "upload/quality.csv"
output_json = "upload/quality.json"

# Transform quality CSV to JSON
transform_quality_to_json(input_csv, output_json)
