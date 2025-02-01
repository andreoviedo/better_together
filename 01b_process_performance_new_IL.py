import pandas as pd
import os
from pathlib import Path

# Define key columns we want to keep
headers_performance = {
    'loan_sequence_number': str,  # Alpha Numeric - PYYQnXXXXXX
    'monthly_reporting_period': 'Int64',  # Date
    'current_actual_upb': float,  # Numeric - 12,2
    'current_loan_delinquency_status': str,  # Alpha Numeric
    'loan_age': 'Int64',  # Numeric
    'remaining_months_to_legal_maturity': 'Int64',  # Numeric
    'defect_settlement_date': 'Int64',  # Date
    'modification_flag': str,  # Alpha
    'zero_balance_code': str,  # Numeric
    'zero_balance_effective_date': 'Int64',  # Date
    'current_interest_rate': float,  # Numeric - 8,3
    'current_deferred_upb': float,  # Numeric
    'due_date_of_last_paid_installment': 'Int64',  # Date
    'mi_recoveries': float,  # Numeric - 12,2
    'net_sales_proceeds': float,  # Alpha-Numeric
    'non_mi_recoveries': float,  # Numeric - 12,2
    'expenses': float,  # Numeric - 12,2
    'legal_costs': float,  # Numeric - 12,2
    'maintenance_and_preservation_costs': float,  # Numeric - 12,2
    'taxes_and_insurance': float,  # Numeric - 12,2
    'miscellaneous_expenses': float,  # Numeric - 12,2
    'actual_loss_calculation': float,  # Numeric - 12,2
    'modification_cost': float,  # Alpha
    'step_modification_flag': str,  # Alpha
    'deferred_payment_plan': str,  # Numeric
    'estimated_loan_to_value': float,  # Numeric - 12,2
    'zero_balance_removal_upb': float,  # Alpha
    'delinquent_accrued_interest': float,  # Alpha
    'delinquency_due_to_disaster': str,  # Numeric - 12,2
    'borrower_assistance_program_code': str,  # Numeric - 12,2
    'current_month_modification_cost': float,  # Numeric - 12,2
    'interest_bearing_upb': float  # Numeric - 12,2
}


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
        output_path = output_dir / file_path.name.replace('.txt', '_FULL.parquet')
        
        # Skip if parquet file already exists
        if output_path.exists():
            print(f"Skipping {file_path.name} - parquet file already exists")
            continue
        
        try:
            # Read the file with explicit dtypes for all columns
            perf_df = pd.read_csv(file_path, 
                         #usecols=[0, 1, 3, 8, 9],  # 0-based indexing
                         names=list(headers_performance.keys()),
                         dtype=headers_performance,
                         sep='|')
            # Save to parquet

            perf_df.to_parquet(output_path, index=False)
            print(f"Saved processed file to {output_path}")
            
        except Exception as e:
            print(f"Error processing {file_path.name}: {str(e)}")

if __name__ == "__main__":
    process_performance_files()