import pandas as pd
import os
from pathlib import Path

# Define the key columns with their positions and dtypes
headers_origination = {
    'credit_score': 'Int64',
    'first_payment_date': 'Int64',
    'first_time_homebuyer_flag': str,
    'maturity_date': 'Int64', 
    'metropolitan_statistical_area': str,
    'mortgage_insurance_percentage': 'Int64',
    'number_of_units': 'Int64',
    'occupancy_status': str,
    'original_cltv': 'float64',
    'original_dti_ratio': 'float64',
    'original_upb': 'float64',
    'original_ltv': 'float64',
    'original_interest_rate': 'float64',
    'channel': str,
    'ppm_flag': str,
    'amortization_type': str,
    'property_state': str,
    'property_type': str,
    'postal_code': str,
    'loan_sequence_number': str,
    'loan_purpose': str,
    'original_loan_term': 'Int64',
    'number_of_borrowers': 'Int64',
    'seller_name': str,
    'servicer_name': str,
    'super_conforming_flag': str,
    'pre_harp_loan_sequence_number': str,
    'program_indicator': str,
    'harp_indicator': str,
    'property_valuation_method': str,
    'interest_only_indicator': str,
    'mortgage_insurance_cancellation_indicator': str
}


def process_origination_files():
    # Create directories if they don't exist
    data_dir = Path('E:/mmar_project_data/data/raw')
    output_dir = Path('E:/mmar_project_data/data/origination')
    output_dir.mkdir(exist_ok=True, parents=True)
    
    # Get all origination files (those without 'time' in the name)
    origination_files = [f for f in data_dir.glob('*.txt') 
                        if 'time' not in f.name.lower()]
    
    # Prepare usecols and dtypes for pandas
    #usecols = [col['pos'] for col in key_origination_columns.values()]
    #names = list(key_origination_columns.keys())
    #dtype = {name: col['dtype'] for name, col in key_origination_columns.items()}
    
    

    for file_path in origination_files:
        print(f"Processing {file_path.name}")
        
        # Create output path
        output_path = output_dir / file_path.name.replace('.txt', '.parquet')
               
        # Read only the needed columns with specified dtypes
        df = pd.read_csv(
            file_path, 
            header=None,
            #usecols=usecols,
            names=list(headers_origination.keys()),
            dtype=headers_origination,
            sep='|'
        )
        print("Completed reading file")
        
        # Save to new location as parquet
        df.to_parquet(output_path, index=False)
        print(f"Saved processed file to {output_path}")

if __name__ == "__main__":
    process_origination_files() 