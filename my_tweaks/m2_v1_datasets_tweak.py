import os
from langsmith import Client
from dotenv import load_dotenv

load_dotenv()
client = Client()

# 1. Define Unique Dataset Name
dataset_name = "MAT496-Code-Review-Queries"

# 2. Define Custom Examples (Input and Expected Output)
# The expected output is what an ideal LLM should return.
examples = [
    {
        "input": "Write a Python function to check if a string is a palindrome.",
        "expected_output": "def is_palindrome(s): return s == s[::-1]"
    },
    {
        "input": "Explain the difference between '==' and 'is' in Python.",
        "expected_output": "'==' checks value equality, 'is' checks object identity (memory location)."
    },
    {
        "input": "How do you handle exceptions in Python?",
        "expected_output": "Use 'try', 'except', and optional 'finally' blocks."
    }
]

# 3. Create the Dataset on LangSmith (will overwrite if it exists)
print(f"Creating dataset: {dataset_name}...")
dataset = client.create_dataset(
    dataset_name=dataset_name, 
    description="Dataset for testing LLM's ability to answer common code review questions.",
)
print(f"Dataset ID: {dataset.id}")

# 4. Upload all Examples to the Dataset
for example in examples:
    client.create_example(
        inputs={"input": example["input"]},
        outputs={"expected_output": example["expected_output"]},
        dataset_id=dataset.id,
    )

print(f"Successfully uploaded {len(examples)} examples to the dataset.")
