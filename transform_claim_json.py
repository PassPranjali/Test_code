import pandas as pd
import json
import os

def transform_claim_to_json(input_csv, output_json):
    # Load CSV
    df = pd.read_csv(input_csv)

    # Validate and transform
    df['ClaimDate'] = pd.to_datetime(df['ClaimDate'], errors='coerce').dt.strftime("%Y-%m-%dT%H:%M:%S").fillna("1970-01-01")
    df['Amount'] = pd.to_numeric(df['Amount'], errors='coerce').fillna(0.0)

    # Convert 'ClaimDate' to string for JSON serialization - other way
    #df['ClaimDate'] = df['ClaimDate'].apply(lambda x: x.isoformat() if isinstance(x, pd.Timestamp) else x)

    # Select relevant columns
    selected_columns = ['ClaimID', 'ClaimDate', 'Amount']
    df = df[selected_columns]

    # Convert to JSON
    json_data = df.to_dict(orient='records')
    with open(output_json, 'w') as f:
        json.dump(json_data, f, indent=4)
    print(f"Transformed {input_csv} to {output_json}")

# Input and output paths
input_csv = "upload/claim.csv"
output_json = "upload/claim.json"

# Transform claim CSV to JSON
transform_claim_to_json(input_csv, output_json)
