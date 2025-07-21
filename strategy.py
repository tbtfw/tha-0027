import pandas as pd
from typing import Literal

def strategy(data: pd.DataFrame) -> Literal["BUY", "SELL", None]:
    """Trading strategy implementation"""
    # TODO: Implement a simple moving average crossover strategy
    # Rules:
    # - BUY when 5-day SMA crosses above 20-day SMA
    # - SELL when 8-day EMA crosses below 18-day EMA
    #
    # Hint: Think about:
    # - What happens at the start of your data?
    # - How to handle price gaps?
    # - What about low volume days?
    return None