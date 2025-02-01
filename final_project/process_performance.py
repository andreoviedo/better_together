import pandas as pd
import os
from pathlib import Path

# Define the key columns with their positions and dtypes
key_performance_columns = {
    'loan_sequence_number': {'pos': 0, 'dtype': str},
    'monthly_reporting_period': {'pos': 1, 'dtype': 'Int64'},  # nullable integer
    'current_actual_upb': {'pos': 2, 'dtype': 'Float64'},  # nullable float
    'current_loan_delinquency_status': {'pos': 3, 'dtype': str},
    'loan_age': {'pos': 4, 'dtype': 'Int64'},  # nullable integer
    'remaining_months_to_legal_maturity': {'pos': 5, 'dtype': 'Int64'},  # nullable integer
    'modification_flag': {'pos': 7, 'dtype': str},
    'current_interest_rate': {'pos': 10, 'dtype': 'Float64'}  # nullable float
}

def process_performance_files():
    # Create directories if they don't exist
    data_dir = Path('final_project/data/')
    output_dir = Path('final_project/data/performance')
    output_dir.mkdir(exist_ok=True, parents=True)
    
    # Get all performance files (those with 'time' in the name)
    performance_files = [f for f in data_dir.glob('*.txt') 
                        if 'time' in f.name.lower()]
    
    # Prepare usecols and dtypes for pandas
    usecols = [col['pos'] for col in key_performance_columns.values()]
    names = list(key_performance_columns.keys())
    dtype = {name: col['dtype'] for name, col in key_performance_columns.items()}
    
    for file_path in performance_files:
        print(f"Processing {file_path.name}")
        # Create output path (change extension to .parquet)
        output_path = output_dir / file_path.name.replace('.txt', '.parquet')
        
        # Skip if parquet file already exists
        if output_path.exists():
            print(f"Skipping {file_path.name} - parquet file already exists")
            continue
            
        # Read only the needed columns with specified dtypes
        df = pd.read_csv(
            file_path, 
            header=None,
            usecols=usecols,
            names=names,
            dtype=dtype,
            sep='|'
        )
        print("Completed reading file")
        
        # Save to new location as parquet
        df.to_parquet(output_path, index=False)
        print(f"Saved processed file to {output_path}")

if __name__ == "__main__":
    process_performance_files() 