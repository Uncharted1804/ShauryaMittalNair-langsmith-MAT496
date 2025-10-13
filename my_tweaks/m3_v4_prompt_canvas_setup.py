import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import Runnable

load_dotenv()

# --- Define the LangChain Runnable for the Prompt Canvas ---
system_prompt = "You are a travel agent who specializes in unusual destinations. Be creative and concise."
prompt = ChatPromptTemplate.from_messages([
    ("system", system_prompt),
    ("user", "Suggest a 3-day itinerary for a trip to {location}.")
])
llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0.7)

# This is our chain, a LangChain "Runnable" object
chain: Runnable = prompt | llm | StrOutputParser()

# We give the chain a name for the run in LangSmith
chain = chain.with_config({"run_name": "MAT496-Prompt-Canvas-Demo"})

# --- Execute the Chain ---
print("Running the chain for Prompt Canvas setup...")
response = chain.invoke({"location": "the Moon"})
print(f"Response: {response}")

print("\nScript finished. Find the 'MAT496-Prompt-Canvas-Demo' run in LangSmith.")