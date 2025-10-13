import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import Runnable

load_dotenv()

# --- Define the LangChain Runnable Object Directly ---

system_prompt = "You are a food critic. Describe the user's item in a single, negative sentence."
prompt = ChatPromptTemplate.from_messages([
    ("system", system_prompt),
    ("user", "What is your opinion on {item}?")
])
llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0.8)

# This is our chain, which is a LangChain "Runnable" object
chain: Runnable = prompt | llm | StrOutputParser()

# We give the chain a name that LangSmith will use for the run.
chain = chain.with_config({"run_name": "MAT496-Lifecycle-Chain-Direct"})

# --- Execute the Chain Directly ---
print("Running the chain directly...")
response = chain.invoke({"item": "cold fries"})
print(f"Response: {response}")

print("\nScript finished.")