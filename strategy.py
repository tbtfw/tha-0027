import pandas as pd
from .data import get_data
from typing import Literal


def strategy(data: pd.DataFrame) -> Literal["BUY", "SELL", None]:
  # TODO: You must implement your strategy here
  # The strategy should return "BUY" if you want to buy,
  # "SELL" if you want to sell, or None if you don't want to do anything
  
  # Strategy 
  # BUY if SMA_5 crosses above SMA_20
  # SELL if EMA_8 crosses below EMA_18
  pass