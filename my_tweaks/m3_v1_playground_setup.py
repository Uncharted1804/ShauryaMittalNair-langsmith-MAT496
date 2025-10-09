import os
from langsmith import traceable
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

# Define the Simple Chain for Playground Setup
@traceable(run_type="chain", name="MAT496-Playground-Tweak-Chain")
def run_playground_chain(topic: str):
    """Creates and runs a simple chain whose components can be edited in the LangSmith Playground."""

    # 1. Prompt Definition: This is the part we want to experiment with in the UI
    system_prompt_template = (
        "You are a very brief, helpful, and slightly sarcastic assistant. "
        "Respond in one sentence."
    )

    prompt = ChatPromptTemplate.from_messages([
        ("system", system_prompt_template),
        ("user", "Explain {topic} in simple terms.")
    ])

    # 2. Model and Chain Setup
    llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0.7) 
    chain = prompt | llm | StrOutputParser()

    # 3. Execution (This logs the trace, making the chain editable in the UI)
    print(f"Running chain for topic: {topic}")
    response = chain.invoke({"topic": topic})
    print(f"Response: {response}")
    return response

# Execute the function to log the trace to LangSmith
run_playground_chain(topic="LangSmith Playground")