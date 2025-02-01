import zipfile
import os
from pathlib import Path

def unzip_files():
    # Define paths
    data_dir = Path('E:/mmar_project_data/data')
    output_dir = data_dir / 'q_data'
    
    # Create output directory if it doesn't exist
    output_dir.mkdir(exist_ok=True)
    
    # Get all zip files in the directory
    zip_files = list(data_dir.glob('*.zip'))
    
    for zip_path in zip_files:
        print(f"Extracting {zip_path.name}")
        
        # Skip if already extracted
        if any(output_dir.glob(zip_path.stem + '*')):
            print(f"Skipping {zip_path.name} - files already extracted")
            continue
            
        try:
            with zipfile.ZipFile(zip_path, 'r') as zip_ref:
                zip_ref.extractall(output_dir)
            print(f"Successfully extracted {zip_path.name}")
        except Exception as e:
            print(f"Error extracting {zip_path.name}: {str(e)}")

if __name__ == "__main__":
    unzip_files() 