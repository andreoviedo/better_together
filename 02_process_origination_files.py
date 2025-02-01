import pandas as pd
from pathlib import Path

def process_origination_files():
    """Combine all origination files into a single file."""
    # Create directories if they don't exist
    data_dir = Path('E:/mmar_project_data/data/origination')
    output_dir = Path('E:/mmar_project_data/data/processed')
    output_dir.mkdir(exist_ok=True, parents=True)
    
    # Get all origination parquet files
    orig_files = list(data_dir.glob('*.parquet'))
    
    if not orig_files:
        raise FileNotFoundError("No origination parquet files found in the origination directory")
    
    print(f"Found {len(orig_files)} origination files to process")
    
    # Initialize list to store DataFrames
    all_dfs = []
    
    # Process each file individually
    for file_path in orig_files:
        print(f"\nProcessing {file_path.name}")
        try:
            # Read origination file
            df = pd.read_parquet(file_path)
            print(f"File shape: {df.shape}")
            
            # Add to list
            all_dfs.append(df)
            
        except Exception as e:
            print(f"Error processing {file_path.name}: {str(e)}")
            continue
    
    # Combine all files
    print("\nCombining all files...")
    combined_df = pd.concat(all_dfs, ignore_index=True)
    print(f"Combined shape: {combined_df.shape}")
    
    # Save combined file
    output_file = output_dir / 'combined_origination.parquet'
    combined_df.to_parquet(output_file)
    print(f"\nSaved combined file to {output_file}")
    
    return combined_df

if __name__ == "__main__":
    process_origination_files() 