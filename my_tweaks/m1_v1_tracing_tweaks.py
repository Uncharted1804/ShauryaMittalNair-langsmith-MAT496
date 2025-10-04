import os
from langsmith import traceable
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv() 

# Ensure tracing is enabled (should be set in .env)
os.environ["LANGCHAIN_TRACING_V2"] = "true" 

# Define a function to be traced
@traceable(run_type="chain", name="SumCalculator")
def calculate_list_sum(numbers: list):
    """Calculates the sum of all numbers in a list."""
    print(f"Input numbers: {numbers}")
    # Introduce a small delay to simulate a complex operation (optional)
    # import time; time.sleep(0.1) 
    total_sum = sum(numbers)
    print(f"Total sum: {total_sum}")
    return total_sum

# Run the function
my_numbers = [10, 25, 40, 5, 20]
result = calculate_list_sum(my_numbers)

