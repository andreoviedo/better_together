import pandas as pd
from pathlib import Path

def merge_loan_data():
    """Merge origination and performance indicator data."""
    # Set up paths
    data_dir = Path('E:/mmar_project_data/data/processed')
    orig_file = data_dir / 'combined_origination.parquet'
    perf_file = data_dir / 'loan_default_indicators.parquet'
    
    # Check if files exist
    if not orig_file.exists():
        raise FileNotFoundError("Combined origination file not found")
    if not perf_file.exists():
        raise FileNotFoundError("Loan default indicators file not found")
    
    print("Loading files...")
    
    # Load origination data
    print("Reading origination data...")
    orig_df = pd.read_parquet(orig_file)
    print(f"Origination shape: {orig_df.shape}")
    
    # Load performance indicators
    print("\nReading performance indicators...")
    perf_df = pd.read_parquet(perf_file)
    print(f"Performance indicators shape: {perf_df.shape}")
    
    # Merge the datasets
    print("\nMerging datasets...")
    merged_df = pd.merge(
        orig_df,
        perf_df,
        on='loan_sequence_number',
        how='inner',
        validate='1:1'
    )
    
    print(f"\nMerged shape: {merged_df.shape}")
    print(f"Merge retention rate: {len(merged_df) / len(orig_df):.2%} of origination records")
    
    # Save merged dataset
    output_file = data_dir / 'merged_loan_data.parquet'
    merged_df.to_parquet(output_file)
    print(f"\nSaved merged data to {output_file}")
    
    # Print summary statistics
    print("\nSummary Statistics:")
    print(f"Total loans: {len(merged_df)}")
    print(f"Default rate: {merged_df['defaulted'].mean():.2%}")
    print("\nObservation period (months):")
    print(merged_df['observation_period_months'].describe())
    
    return merged_df

if __name__ == "__main__":
    merge_loan_data() 