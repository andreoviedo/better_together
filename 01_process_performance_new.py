import pandas as pd
import os
from pathlib import Path

# Define key columns we want to keep
key_performance_columns = [
    'loan_sequence_number',                  
    'monthly_reporting_period',              
    'current_loan_delinquency_status',       
    'current_actual_upb',                    
    'loan_age',                             
    'current_interest_rate',                 
    'modification_flag',                     
    'zero_balance_code'                      
]


def process_performance_files():
    # Create directories if they don't exist
    data_dir = Path('E:/mmar_project_data/data/raw')
    output_dir = Path('E:/mmar_project_data/data/performance')
    output_dir.mkdir(exist_ok=True, parents=True)
    
    # Get all performance files (those with 'time' in the name)
    performance_files = [f for f in data_dir.glob('*.txt') 
                        if 'time' in f.name.lower()]
    
    for file_path in performance_files:
        print(f"Processing {file_path.name}")
        
        # Create output path
        output_path = output_dir / file_path.name.replace('.txt', '.parquet')
        
        # Skip if parquet file already exists
        if output_path.exists():
            print(f"Skipping {file_path.name} - parquet file already exists")
            continue
        
        try:
            # Read the file with explicit dtypes for all columns
            perf_df = pd.read_csv(file_path, 
                         usecols=[0, 1, 3, 8, 9],  # 0-based indexing
                         names=['loan_sequence_number',
                               'monthly_reporting_period',
                               'current_loan_delinquency_status',
                               'zero_balance_code',
                               'zero_balance_effective_date'],
                            dtype={
                                'loan_sequence_number': str,
                                'monthly_reporting_period': 'Int64',
                                'current_loan_delinquency_status': str,
                                'zero_balance_code': str,
                                'zero_balance_effective_date': 'Int64'
                            },
                            sep='|')
            # Save to parquet
            perf_df.to_parquet(output_path, index=False)
            print(f"Saved processed file to {output_path}")
            
        except Exception as e:
            print(f"Error processing {file_path.name}: {str(e)}")

if __name__ == "__main__":
    process_performance_files()