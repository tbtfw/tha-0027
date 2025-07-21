from data import get_data
from strategy import strategy
import pandas as pd

def run_backtest(ticker: str, capital: int = 10_000) -> pd.DataFrame:
    """Run backtest and track trades"""
    data = get_data(ticker)
    trades = []
    position = 0
    cash = capital

    # TODO: Fix the backtesting loop
    # - Data should be processed one row at a time
    # - Each iteration should only see data up to that point
    # - Track position and cash properly
    # Hint: What happens with price gaps between days?

    for i in range(len(data)):
        current_data = data.iloc[:i+1]
        signal = strategy(current_data)
        
        if signal is not None:
            # TODO: Implement trading logic
            # - Update position and cash
            # - Record trade details
            # - Consider trading costs
            pass

    # TODO: Return DataFrame with:
    # - Entry/exit prices
    # - Position sizes
    # - P&L per trade
    return pd.DataFrame(trades)

def calculate_stats(trades: pd.DataFrame) -> None:
    """Calculate and display backtest statistics"""
    # TODO: Calculate key statistics
    # - Total P&L
    # - Win rate
    # - Average trade P&L
    # - Maximum drawdown
    pass

if __name__ == "__main__":
    import argparse
    
    parser = argparse.ArgumentParser(description="Backtest a trading strategy")
    parser.add_argument("ticker", type=str, help="Stock ticker")
    parser.add_argument("--capital", type=int, default=10_000, help="Starting capital")
    
    args = parser.parse_args()
    
    trades = run_backtest(args.ticker, args.capital)
    calculate_stats(trades)