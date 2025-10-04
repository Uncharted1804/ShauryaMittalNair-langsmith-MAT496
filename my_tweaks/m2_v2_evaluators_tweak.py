import os
from langsmith import Client
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

# 1. Import the necessary evaluator loading function
from langchain.evaluation import load_evaluator 

load_dotenv()
client = Client()

# --- Define the System Under Test (SUT) ---
# This is the Chain that will be tested against the dataset.
system_prompt = (
    "You are an expert Python code reviewer. Provide a concise, single-sentence "
    "answer or the requested code snippet only, without any preamble or explanation."
)

prompt = ChatPromptTemplate.from_messages([
    ("system", system_prompt),
    ("human", "{input}")
])

# Initialize the LLM (Ensure OPENAI_API_KEY is set in .env)
llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0.0) 

# Create the chain: Prompt | LLM | Output Parser
code_reviewer_chain = prompt | llm | StrOutputParser()

# 2. Define the Evaluator
# Load a simple evaluator that checks for an exact match between LLM output and expected_output
exact_match_evaluator = load_evaluator("exact_match")

# 3. Define the Run Parameters
# This MUST match the dataset name created in M2 V1
dataset_name = "MAT496-Code-Review-Queries"

# Use a distinct project name for the evaluation run
eval_project_name = "MAT496-Code-Review-Exact-Match-Eval"

print(f"Running CodeReviewerChain with Exact Match Evaluator on dataset '{dataset_name}'...")

# 4. Execute the Evaluation Run with the Corrected Evaluator Parameter
run_results = client.run_on_dataset(
    dataset_name=dataset_name,
    llm_or_chain_factory=code_reviewer_chain,
    project_name=eval_project_name, 
    
    # --- CORRECTED TWEAK: Pass the evaluator list using the 'evaluators' keyword ---
    evaluators=[exact_match_evaluator], 
    
    verbose=True 
)

print(f"\nEvaluation run finished. Project created: '{eval_project_name}'.")
print("Check LangSmith UI under 'Projects' -> 'MAT496-Code-Review-Exact-Match-Eval' for evaluation scores.")