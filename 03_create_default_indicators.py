import pandas as pd
from pathlib import Path
import numpy as np

def create_default_indicators(perf_df):
    """Create default indicators from performance data."""
    # Convert delinquency status to numeric, handling any non-numeric values
    perf_df['current_loan_delinquency_status'] = pd.to_numeric(
        perf_df['current_loan_delinquency_status'], 
        errors='coerce'
    )
    
    # Convert zero_balance_code to numeric, handling any non-numeric values
    perf_df['zero_balance_code'] = pd.to_numeric(
        perf_df['zero_balance_code'], 
        errors='coerce'
    )
    
    # Get worst delinquency status for each loan
    loan_status = perf_df.groupby('loan_sequence_number').agg({
        'current_loan_delinquency_status': 'max',  # worst status
        'monthly_reporting_period': ['min', 'max'],  # observation period
        'zero_balance_code': 'last'  # final disposition
    })
    
    # Flatten column names
    loan_status.columns = [
        'worst_delinquency_status',
        'first_observation',
        'last_observation',
        'final_zero_balance_code'
    ]
    
    # Define default (90+ days delinquent or foreclosure)
    loan_status['defaulted'] = (
        (loan_status['worst_delinquency_status'] >= 3) | 
        (loan_status['final_zero_balance_code'] == 3)  # foreclosure
    ).astype(int)
    
    # Calculate observation period in months
    loan_status['observation_period_months'] = (
        ((loan_status['last_observation'] // 100) * 12 + (loan_status['last_observation'] % 100)) - 
        ((loan_status['first_observation'] // 100) * 12 + (loan_status['first_observation'] % 100))
    )

    # Get first default month for each loan
    default_months = perf_df[
        (perf_df['current_loan_delinquency_status'] >= 3) |
        (perf_df['zero_balance_code'] == 3)
    ].groupby('loan_sequence_number')['monthly_reporting_period'].min()
    
    # Add default month to loan status
    loan_status['month_of_default'] = default_months
    
    # Flag if loan defaulted in first observation month
    loan_status['defaulted_at_start'] = (
        loan_status['month_of_default'] == loan_status['first_observation']
    ).fillna(False).astype(int)
    
    return loan_status

def process_performance_files():
    """Process each performance file individually and combine summaries."""
    data_dir = Path('E:/mmar_project_data/data/performance')
    output_dir = Path('E:/mmar_project_data/data/processed')
    output_dir.mkdir(exist_ok=True, parents=True)
    
    all_files = [f for f in data_dir.glob('*.parquet') if 'FULL' not in f.name]
    if not all_files:
        raise FileNotFoundError("No parquet files found in the performance directory")
    
    print(f"Found {len(all_files)} performance files to process")
    
    # Initialize list to store summaries
    all_summaries = []
    
    # Process each file individually
    for file_path in all_files:
        print(f"\nProcessing {file_path.name}")
        try:
            # Read performance file
            perf_df = pd.read_parquet(file_path)
            print(f"File shape: {perf_df.shape}")
            
            # Create summary for this file
            file_summary = create_default_indicators(perf_df)
            print(f"Processed {len(file_summary)} loans from {file_path.name}")
            
            # Add to list of summaries
            all_summaries.append(file_summary)
            
            # Clear memory
            del perf_df
            
        except Exception as e:
            print(f"Error processing {file_path.name}: {str(e)}")
            continue
    
    # Combine all summaries
    print("\nCombining all summaries...")
    combined_summary = pd.concat(all_summaries)
    
    # Group by loan_sequence_number to handle any overlaps between files
    #final_summary = combined_summary.groupby(level=0).agg({
    #    'worst_delinquency_status': 'max',
    #    'first_observation': 'min',
    #    'last_observation': 'max',
    #    'final_zero_balance_code': 'last',
    #    'defaulted': 'max',
    #    'observation_period_months': 'max'
    #})
    
    # Save results
    output_file = output_dir / 'loan_default_indicators.parquet'
    combined_summary.to_parquet(output_file)
    
    # Print summary statistics
    print("\nFinal Summary Statistics:")
    print(f"Total unique loans processed: {len(combined_summary)}")
    print(f"Default rate: {combined_summary['defaulted'].mean():.2%}")
    print("\nObservation period (months):")
    print(combined_summary['observation_period_months'].describe())
    
    return combined_summary

if __name__ == "__main__":
    process_performance_files() 