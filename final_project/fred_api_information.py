import requests
import os
from dotenv import load_dotenv

def get_fred_data(series_id):
    """
    Retrieves economic data from the FRED API in JSON format
    
    Args:
        series_id (str): The FRED series ID to retrieve
        
    Returns:
        dict: JSON response from the FRED API containing the requested data
    """
    # Load API key from environment variables
    load_dotenv()
    api_key = os.getenv('FRED_API_KEY')
    
    # Construct the API URL
    base_url = "https://api.stlouisfed.org/fred/series/observations"
    params = {
        'series_id': series_id,
        'api_key': api_key,
        'file_type': 'json'
    }
    
    # Make the API request
    response = requests.get(base_url, params=params)
    
    # Check if request was successful
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"Failed to retrieve data: {response.status_code}")


get_fred_data('FEDFUNDS')