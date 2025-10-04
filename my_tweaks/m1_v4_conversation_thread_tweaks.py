import os
from langsmith import traceable
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# 1. Define a consistent Session ID for the entire conversation
CONVERSATION_ID = "Tweak-Session-496-001"

# Set the session ID as an environment variable (LangSmith uses this implicitly)
os.environ["LANGCHAIN_SESSION"] = CONVERSATION_ID

# Use a generic traceable function to simulate a chatbot response
@traceable(run_type="chain", name="ChatResponder")
def get_response(user_input: str, history: str) -> str:
    """Simulates a conversational AI response."""
    print(f"User Input: '{user_input}'")
    if "hello" in user_input.lower():
        response = "Hello! What can I analyze for you today?"
    elif "thanks" in user_input.lower():
        response = f"You're welcome! Conversation history was: {history[:30]}..."
    else:
        response = "I see. Let's trace that thought."
    return response

# --- Conversation Turn 1 ---
print("--- Turn 1 ---")
user_msg_1 = "Hello, I need to check something."
resp_1 = get_response(user_msg_1, "START")

# --- Conversation Turn 2 (Crucial for tracing) ---
print("\n--- Turn 2 ---")
user_msg_2 = "Thanks, that was very helpful!"

# The second run *must* be executed in the same environment (same process 
# or thread) where LANGCHAIN_SESSION is set to the same value 
# (CONVERSATION_ID) for LangSmith to link them automatically.
resp_2 = get_response(user_msg_2, resp_1) 

print(f"\nCompleted Conversation ID: {CONVERSATION_ID}")
