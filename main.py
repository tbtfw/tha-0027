from .data import get_data
from .strategy import strategy

def runner(ticker: str, capital: int = 10_000) -> None:
  data = get_data(ticker)
  
  # TODO: Fix this, you need to provide data for each row one by one
  # On first iteration, data should be the first row
  # On second iteration, data should be the first two rows
  # and so on...
  # TODO: This is a sample code, you need to fix it
  for i in data.itterrows():
    signal = strategy(data[i:])
    
    if signal is not None:
      # TODO: Implement logic to buy or sell based on the signal
      # TODO: You must also store individual trades in a list / dataframe
      pass
  
  
  # TODO: Calculate stats, like PnL, total trades, profitable trades, loss trades, etc.
  # TODO: Visualise stats on a candlestick chart with trades marked.
  
  
  if __name__ == "__main__":
    import argparse
    
    parser = argparse.ArgumentParser(description="Run trading strategy on historical data.")
    parser.add_argument("ticker", type=str, help="Stock ticker symbol")
    parser.add_argument("--capital", type=int, default=10_000, help="Initial capital for trading")
    
    args = parser.parse_args()
    
    runner(args.ticker, args.capital)