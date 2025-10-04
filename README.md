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
  [`My_Tweaks/m1_v1_tracing_tweak.py`](my_tweaks/m1_v1_tracing_tweak.py)

---

## 🧠 Summary
Each lesson directory inside `my_tweaks/` includes:
- A customized code example building on the video’s concepts  
- Clear comments explaining what was modified  
- Verified LangSmith tracing results visible in the linked project

---

