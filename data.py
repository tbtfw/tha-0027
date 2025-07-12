import pandas as pd
from pathlib import Path

def load_data(ticker:str) -> pd.DataFrame:
  # TODO: Refer to the following documentation and load data for 
  # https://www.alphavantage.co/documentation/#daily
  pass

def cleanup_data(data: pd.DataFrame) -> pd.DataFrame:
  # TODO: Perform necessary cleanup on the data
  # such as removing NaN values, renaming columns, etc.
  pass

def parse_data(data: pd.DataFrame) -> pd.DataFrame:
  # TODOD: parse data to the format datetime, open, high, low, close, volume
  pass


def get_data(ticker: str) -> pd.DataFrame:
  # TODO: Chain above methods in appropriate order
  pass