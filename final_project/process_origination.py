import pandas as pd
import os
from pathlib import Path

# Define the headers for origination files
headers_origination = [
    'credit_score', 'first_payment_date', 'first_time_homebuyer', 'maturity_date',
    'msa', 'mortgage_insurance_percentage', 'number_of_units', 'occupancy_status',
    'original_CLTV', 'original_DTI', 'original_UPB', 'original_LTV',
    'original_interest_rate', 'channel', 'prepayment_penalty_mortgage',
    'product_type', 'property_state', 'property_type', 'postal_code',
    'loan_sequence_number', 'loan_purpose', 'original_loan_term',
    'number_of_borrowers', 'seller_name', 'servicer_name', 'super_conforming_flag'
]

# Define the key columns we want to keep
key_origination_columns = [
    'credit_score', 'first_payment_date', 'original_UPB', 'original_LTV', 'original_DTI',
    'original_interest_rate', 'property_state', 'property_type',
    'loan_sequence_number', 'loan_purpose', 'original_loan_term'
]

def process_origination_files():
    # Create directories if they don't exist
    data_dir = Path('final_project/data/')  # Specify full path to raw data folder
    print(f"Looking for files in: {data_dir}")
    output_dir = Path('final_project/data/origination')  # Create output dir under processed folder
    output_dir.mkdir(exist_ok=True)  # Create origination subfolder
    print(f"Saving processed files to: {output_dir}")
    # Get all origination files (those without 'time' in the name)
    origination_files = [f for f in data_dir.glob('*.txt') 
                        if 'time' not in f.name.lower()]
    
    print(origination_files)
    
    for file_path in origination_files:
        print(f"Processing {file_path.name}")
        
        # Read the file without headers, using pipe as delimiter
        df = pd.read_csv(file_path, header=None, names=headers_origination, sep='|')
        
        # Keep only the key columns
        df_filtered = df[key_origination_columns]
        
        # Create output path
        output_path = output_dir / file_path.name
        
        # Save to new location
        df_filtered.to_csv(output_path, index=False)
        print(f"Saved processed file to {output_path}")

if __name__ == "__main__":
    process_origination_files() 