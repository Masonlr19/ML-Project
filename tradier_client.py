import requests
import os

TRADIER_API_KEY = os.getenv("TRADIER_API_KEY")  # Set this in your environment
BASE_URL = "https://api.tradier.com/v1/markets"

headers = {
    "Authorization": f"Bearer {TRADIER_API_KEY}",
    "Accept": "application/json"
}

def get_historical_data(symbol, interval='daily', start_date='2024-01-01', end_date='2024-12-31'):
    params = {
        "symbol": symbol,
        "interval": interval,
        "start": start_date,
        "end": end_date
    }
    response = requests.get(f"{BASE_URL}/history", headers=headers, params=params)
    response.raise_for_status()
    return response.json()
