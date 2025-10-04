import os
from langsmith import traceable
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# --- Tool Run Type ---
@traceable(run_type="tool", name="StockDataFetcher")
def fetch_stock_price(ticker: str) -> float:
    """Simulates fetching the latest stock price for a given ticker."""
    # This function acts like an API call or tool execution
    if ticker == "GOOG":
        price = 150.25
    elif ticker == "MSFT":
        price = 420.00
    else:
        price = 100.00
    print(f"Tool executed: Fetched price for {ticker}: {price}")
    return price

# --- Chain Run Type ---
@traceable(run_type="chain", name="InvestmentChain")
def analyze_investment(ticker: str) -> str:
    """Traces a simple 'chain' that uses the 'tool' to get data."""

    # Call the 'tool' function. This call will be logged as a nested 'tool' run
    price = fetch_stock_price(ticker) 

    # Simple analysis (this is the 'chain' logic)
    if price > 200.0:
        analysis = f"{ticker} is a high-value stock at ${price:.2f}."
    else:
        analysis = f"{ticker} is a mid-range stock at ${price:.2f}."

    print(f"Chain executed: Analysis for {ticker}: {analysis}")
    return analysis

# Run the top-level 'chain'
result_goog = analyze_investment("GOOG")
result_msft = analyze_investment("MSFT")

print(f"\nFinal Result 1: {result_goog}")
print(f"Final Result 2: {result_msft}")

