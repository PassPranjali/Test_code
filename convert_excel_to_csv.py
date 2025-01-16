import pandas as pd
import os

def convert_excel_to_csv(input_file, output_folder):
    # Read the Excel file
    excel_data = pd.ExcelFile(input_file)

    # Ensure the output folder exists
    os.makedirs(output_folder, exist_ok=True)

    # Process each sheet
    for sheet_name in excel_data.sheet_names:
        # Read the sheet into a DataFrame
        df = excel_data.parse(sheet_name)

        # Save as CSV
        output_csv = os.path.join(output_folder, f"{sheet_name.lower()}.csv")
        df.to_csv(output_csv, index=False)
        print(f"Converted {sheet_name} to {output_csv}")

# Input and output paths
input_file = "input/data.xlsx"
output_folder = "upload"

# Convert Excel sheets to CSV
convert_excel_to_csv(input_file, output_folder)
