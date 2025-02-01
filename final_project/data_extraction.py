import os
import zipfile
import glob

def extract_zip_files(directory='.', pattern='Q'):
    """
    Extract zip files in the specified directory and its subdirectories that match the pattern
    
    Args:
        directory (str): Root directory to search for zip files
        pattern (str): Pattern to match in zip file names
    """
    # Find all .zip files in directory and subdirectories
    zip_files = glob.glob(os.path.join(directory, '**/*.zip'), recursive=True)
    
    # Filter zip files to only those containing the pattern
    matching_zips = [f for f in zip_files if pattern in os.path.basename(f)]
    
    print(f"Found {len(matching_zips)} zip files containing '{pattern}'")
    
    # Extract each zip file
    for zip_path in matching_zips:
        try:
            # Get the directory containing the zip file
            extract_dir = os.path.dirname(zip_path)
            
            print(f"Extracting {zip_path} to {extract_dir}")
            
            # Extract the zip file
            with zipfile.ZipFile(zip_path, 'r') as zip_ref:
                zip_ref.extractall(extract_dir)
                
            print(f"Successfully extracted {zip_path}")
            
        except Exception as e:
            print(f"Error extracting {zip_path}: {str(e)}")

if __name__ == "__main__":
    # Get the current directory where the script is located
    current_dir = os.path.dirname(os.path.abspath(__file__))
    
    # Extract zip files containing 'Q'
    extract_zip_files(current_dir)
