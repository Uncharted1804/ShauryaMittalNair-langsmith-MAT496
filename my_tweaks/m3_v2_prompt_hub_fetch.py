import os
from dotenv import load_dotenv
from langsmith import Client
from langchain import hub
from langchain.prompts.chat import ChatPromptTemplate
from langchain_openai import ChatOpenAI

# Load keys and set up the client
load_dotenv()
client = Client()

# --- Part 1: Pull a Public Prompt ---
print("--- Pulling a public RAG prompt from the Hub ---")
try:
    # Grab a popular RAG prompt to start with
    pulled_prompt = hub.pull("prompt1")
    print("Successfully pulled 'prompt1'.")
    print("Template snippet:", pulled_prompt.messages[0].prompt.template[:100] + "...")
except Exception as e:
    print(f"Failed to pull prompt: {e}")

# --- Part 2: My Tweak - Create and Push a Custom Prompt ---
print("\n--- Creating and Pushing my own prompt ---")

# My custom prompt for a pirate-themed assistant
my_prompt_template_str = """You are a helpful and friendly pirate assistant. Answer the user's question based on the provided context.

Context: {context}
Question: {question}
Answer (in a pirate voice):"""

my_prompt = ChatPromptTemplate.from_template(my_prompt_template_str)
my_prompt_name = "pirate-rag-prompt"

try:
    # FIX: Pass the prompt template using the 'object' keyword argument
    client.push_prompt(my_prompt_name, object=my_prompt)
    print(f"Successfully pushed '{my_prompt_name}' to the Prompt Hub!")
    print("It should be available in the LangSmith UI now.")
except Exception as e:
    print(f"Failed to push prompt: {e}")