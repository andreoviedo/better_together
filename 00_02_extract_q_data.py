import zipfile
import os
from pathlib import Path

def extract_q_files():
    # Define paths
    base_dir = Path('E:/mmar_project_data/data')
    q_data_dir = base_dir / 'q_data'
    raw_dir = base_dir / 'raw'
    
    # Create raw directory if it doesn't exist
    raw_dir.mkdir(exist_ok=True)
    
    # Get all zip files in q_data directory
    zip_files = list(q_data_dir.glob('*.zip'))
    
    for zip_path in zip_files:
        print(f"Processing {zip_path.name}")
        
        # Skip if already extracted (checking if any file with same stem exists)
        if any(raw_dir.glob(zip_path.stem + '*')):
            print(f"Skipping {zip_path.name} - files already extracted")
            continue
            
        try:
            # Extract zip file to raw directory
            with zipfile.ZipFile(zip_path, 'r') as zip_ref:
                zip_ref.extractall(raw_dir)
            print(f"Successfully extracted {zip_path.name}")
        except Exception as e:
            print(f"Error extracting {zip_path.name}: {str(e)}")

if __name__ == "__main__":
    extract_q_files() 