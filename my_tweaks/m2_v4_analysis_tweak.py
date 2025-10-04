import os
from langsmith import Client
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain.evaluation import load_evaluator 

load_dotenv()
client = Client()

# --- Setup Constants ---
dataset_name = "MAT496-Code-Review-Queries"
evaluator = load_evaluator("exact_match")

# 1. Define the Final Optimized SUT (Assuming gpt-4o-mini performed better)
model_name = "gpt-4o-mini"

system_prompt = (
    "You are an expert Python code reviewer. Provide a highly accurate, concise, "
    "and single-sentence answer or the requested code snippet."
)
prompt = ChatPromptTemplate.from_messages([
    ("system", system_prompt),
    ("human", "{input}")
])

llm = ChatOpenAI(model=model_name, temperature=0.0) 
final_chain = prompt | llm | StrOutputParser()

# 2. Define Final Run Parameters with Metadata and Tags
final_project_name = "MAT496-Final-Submission-Analysis"

# Project-level metadata for easy overall filtering/tracking
final_project_metadata = {
    "model_version": model_name,
    "chain_type": "Optimized Code Reviewer",
    "date_submitted": "2024-10-05" # Change to actual date if needed
}

# Run-level tags (will apply to every single run in the project)
final_tags = ["Final-Submission-Run", "High-Quality-Model"]

print(f"\n--- Starting Final Submission Run: {model_name} ---")

# 3. Execute the Evaluation Run
run_results = client.run_on_dataset(
    dataset_name=dataset_name,
    llm_or_chain_factory=final_chain,
    project_name=final_project_name, 
    evaluators=[evaluator], 
    # --- THE KEY TWEAKS: Add metadata and tags ---
    project_metadata=final_project_metadata,
    tags=final_tags,

    verbose=True
)

print(f"Final Analysis Run completed. Project: {final_project_name}")
print("Check LangSmith UI and use filters/tags to analyze the results.")