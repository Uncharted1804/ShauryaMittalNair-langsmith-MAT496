import os
from langsmith import Client
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain.evaluation import load_evaluator # For ExactMatch scoring

load_dotenv()
client = Client()

# --- Setup Constants ---
dataset_name = "MAT496-Code-Review-Queries"
evaluator = load_evaluator("exact_match")

# 1. Define the Evaluation Function (to avoid repeating code)
def create_and_run_chain(model_name: str, temperature: float, project_tag: str):
    """Creates a chain and runs it on the dataset with evaluation."""
    print(f"\n--- Starting Experiment: {project_tag} ({model_name}) ---")

    # Define the SUT (System Under Test)
    system_prompt = (
        "You are an expert Python code reviewer. Provide a concise, single-sentence "
        "answer or the requested code snippet only, without any preamble or explanation."
    )
    prompt = ChatPromptTemplate.from_messages([
        ("system", system_prompt),
        ("human", "{input}")
    ])

    # Initialize the LLM with specified parameters
    llm = ChatOpenAI(model=model_name, temperature=temperature) 
    chain = prompt | llm | StrOutputParser()

    # Define the project name for this specific experiment run
    eval_project_name = f"MAT496-Code-Review-Experiment-{project_tag}"

    run_results = client.run_on_dataset(
        dataset_name=dataset_name,
        llm_or_chain_factory=chain,
        project_name=eval_project_name, 
        # Use the corrected parameter for evaluators
        evaluators=[evaluator], 
        verbose=True
    )
    print(f"Experiment '{project_tag}' completed. Project: {eval_project_name}")
    return run_results

# 2. Run Experiment 1: Baseline (gpt-3.5-turbo)
create_and_run_chain(
    model_name="gpt-3.5-turbo", 
    temperature=0.0, 
    project_tag="Baseline-GPT-3.5"
)

# 3. Run Experiment 2: Tweak (gpt-4o-mini is a good alternative for testing)
create_and_run_chain(
    model_name="gpt-4o-mini", 
    temperature=0.0, 
    project_tag="Experiment-GPT-4o-mini"
)

print("\nAll experiments complete. Check LangSmith UI under 'Projects' for comparison.")