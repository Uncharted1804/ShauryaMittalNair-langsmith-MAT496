import os
import time
from langsmith import Client
from dotenv import load_dotenv

# --- Load environment variables and initialize client ---
load_dotenv()

def print_debug_env():
    """Check if LangSmith environment variables are correctly loaded."""
    print("\n🔍 LangSmith Environment Debug:")
    api_key = os.getenv("LANGCHAIN_API_KEY")
    endpoint = os.getenv("LANGCHAIN_ENDPOINT")
    tracing = os.getenv("LANGCHAIN_TRACING_V2")

    if not api_key:
        print(" LANGCHAIN_API_KEY is missing or empty.")
    elif not api_key.startswith("ls__"):
        print("LANGCHAIN_API_KEY format looks invalid (should start with 'ls__').")
    else:
        print("API key detected.")

    print(f"Endpoint: {endpoint or 'Missing'}")
    print(f"Tracing Enabled: {tracing or ' Missing'}\n")

print_debug_env()
client = Client()

# --- Simulation Functions ---
def fetch_data(source):
    """Simulates fetching data."""
    time.sleep(0.1)
    print(f"  > Fetched data from {source}")
    return [f"Raw data from {source}", "ERROR_DATA", "CLEAN_DATA"]

def clean_data(data_list):
    """Simulates cleaning bad data points."""
    time.sleep(0.1)
    cleaned = [d for d in data_list if "ERROR" not in d]
    print(f"  > Cleaned {len(data_list) - len(cleaned)} bad entries.")
    return cleaned

# --- Helper to detect new LangSmith API ---
def has_context_run(client_obj):
    """Check if 'client.run' method exists (newer versions)."""
    return hasattr(client_obj, "run") and callable(getattr(client_obj, "run"))

# --- Main Execution ---
try:
    if has_context_run(client):
        
        with client.run(
            run_type="chain",
            name="DataPreprocessingPipeline",
            inputs={"start_source": "Internal DB"}
        ) as run:
            raw_data = fetch_data("Internal DB")
            final_data = clean_data(raw_data)
            run.end(outputs={"final_count": len(final_data), "sample_data": final_data[0]})

    else:
     
        run = client.create_run(
            name="DataPreprocessingPipeline",
            run_type="chain",
            inputs={"start_source": "Internal DB"}
        )

        if run is None:
            print("Failed to create run. Check your LangSmith API key and endpoint in the .env file.")
        else:
            raw_data = fetch_data("Internal DB")
            final_data = clean_data(raw_data)
            client.update_run(run.id, outputs={"final_count": len(final_data), "sample_data": final_data[0]})
            client.update_run(run.id, end_time=time.time())

    print("\n Data pipeline completed and trace logged to LangSmith.")

except Exception as e:
    print(f"\nAn unexpected error occurred: {e}")
