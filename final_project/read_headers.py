import pandas as pd
import os

# Get the current directory where the script is located
current_dir = os.path.dirname(os.path.abspath(__file__))

# Path to the layout file
layout_path = os.path.join(current_dir, 'data', 'file_layout.xlsx')

try:
    # Read the Excel file
    layout_df = pd.read_excel(layout_path)
    
    # Skip the header row and get field names
    field_names = []
    for idx, row in layout_df.iterrows():
        if pd.notna(row['ORIGINATION DATA FILE']) and str(row['ORIGINATION DATA FILE']).isdigit():
            field_name = str(row['Unnamed: 1']).strip()
            if field_name:
                field_names.append(field_name)
    
    print("\nField names from layout file:")
    print("--------------------------")
    for i, name in enumerate(field_names, 1):
        print(f"{i}. {name}")
    
    print("\nTotal number of fields:", len(field_names))
    
    # Save as Python list format
    print("\nPython list format:")
    print("headers = [")
    for name in field_names:
        print(f"    '{name}',")
    print("]")
    
except Exception as e:
    print(f"Error reading layout file: {str(e)}") 