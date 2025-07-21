import pandas as pd
import requests
from pathlib import Path
from typing import Dict


def load_data(ticker: str) -> pd.DataFrame:
    """Get stock data from Alpha Vantage"""
    # TODO: Load daily stock data from Alpha Vantage API
    # Hint: Look at the rate limits and error responses
    # Data should have columns: date, open, high, low, close, volume
    return pd.DataFrame()


def cleanup_data(data: pd.DataFrame) -> pd.DataFrame:
    """Clean the data for analysis"""
    # TODO: Clean the data
    # - Fix column names to be lowercase
    # - Convert date strings to datetime
    # - Handle any missing values
    # - Remove duplicates if any
    # Hint: What happens with dividend dates?
    return data


def clear_data(data: pd.DataFrame) -> pd.DataFrame:
    """Remove unnecessary columns from the data"""
    # Clear Close Prices
    # adjust close price by mean of open


def parse_data(data: pd.DataFrame) -> pd.DataFrame:
    """Format data for backtesting"""
    # TODO: Parse data into usable format
    # - Set index to datetime
    # - Ensure OHLCV columns exist
    # - Data sorted by date
    # - All columns as proper numeric types
    # Hint: Watch out for adjusted vs unadjusted prices
    return data


def get_data(ticker: str) -> pd.DataFrame:
    """Main function to load and process data"""
    try:
        # TODO: Implement the full data pipeline
        # - Load raw data
        # - Clean it up
        # - Parse into final format
        # Hint: What could go wrong at each step?
        clear_data()
        return pd.DataFrame()
    except Exception as e:
        # TODO: Add proper error handling
        raise
