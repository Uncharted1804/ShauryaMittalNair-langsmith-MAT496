# ShauryaMittalNair-Langsmith-MAT496  
**Course Submission for MAT496**

This repository contains the required code and commit history for the **Intro to LangSmith** course submission.  


## Video-by-Video Learning and Tweaks

### Module 1, Video 1: Tracing Basics

- **Learned:**  
  Understood the fundamental process of setting up LangSmith environment variables (`LANGCHAIN_API_KEY`, `LANGCHAIN_PROJECT`, etc.) and how to use the `@traceable` decorator to automatically log any Python function's execution as a **Run** in LangSmith.

- **My Tweak:**  
  Instead of using the basic example from the tutorial, I applied the `@traceable` decorator to a function that **calculates the sum of a list of integers** (`SumCalculator`).  
  This successfully logged both the input list and the computed sum to my LangSmith project dashboard.

- **Source File:**  
  [`My_Tweaks/m1_v1_tracing_tweaks.py`](my_tweaks/m1_v1_tracing_tweaks.py)

  ## Module 1, Video 2: Types of Runs
- **Learned:** 
Understood the different run types (`llm`, `chain`, `tool`, `retriever`) used by LangSmith to categorize and visualize application steps. Learned how to manually assign a `run_type` using the `@traceable` decorator.

- **My Tweak:** Created a custom **`chain`** (`InvestmentChain`) that calls a custom **`tool`** (`StockDataFetcher`) and explicitly set both their `run_type` parameters to demonstrate nested tracing of different execution types.

-**Source File:** [my_tweaks/m1_v2_run_types_tweaks.py](my_tweaks/m1_v2_run_types_tweaks.py)

## Module 1, Video 3: Alternative Ways to Trace
- **Learned:** Understood how to use the `with client.run(...)` context manager for tracing. This allows explicit control over the start and end of a run, which is ideal for wrapping multi-step scripts or sections of code where decorators are not feasible.
- **My Tweak:** Implemented the context manager to trace a full **"Data Preprocessing Pipeline"** (`run_type="chain"`) that simulates fetching and cleaning data, logging the entire sequence as one run.
- **Source File:** [my_tweaks/m1_v3_alternate_ways_to_trace_tweak.py](my_tweaks/m1_v3_alternate_ways_to_trace_tweak.py)

---

## 🧠 Summary
Each lesson directory inside `my_tweaks/` includes:
- A customized code example building on the video’s concepts  
- Clear comments explaining what was modified  
- Verified LangSmith tracing results visible in the linked project

---

