# 🧠 AI Scientific Discovery Agent

## 1. Project Overview

The **AI Scientific Discovery Agent** is an autonomous, multi-agent AI system designed to perform **scientific discovery on structured datasets** without requiring predefined analytical questions.

Instead of asking:
> “What do you want to analyze?”

The system autonomously:
- Explores the dataset
- Discovers patterns
- Generates scientific hypotheses
- Designs and executes statistical experiments
- Critiques its own findings
- Stores reasoning history (memory)
- Produces a structured, human-readable scientific report

This project demonstrates **Agentic AI**, **autonomous reasoning**, and **production-grade AI system design**.

---

## 2. Problem Statement

Traditional data analysis systems:
- Require human-defined questions
- Depend heavily on manual exploration
- Do not reason about *why* results may be wrong
- Do not self-evaluate or iterate

Real scientific reasoning, however, involves:
- Hypothesis formation
- Experimental validation
- Critical evaluation
- Iterative refinement

This project bridges that gap by building an **AI system that reasons like a scientist**.

---

## 3. Core Objectives

The system is designed to:

1. Discover insights **without human questions**
2. Generate **testable, falsifiable hypotheses**
3. Validate hypotheses using **statistical methods**
4. Critically evaluate its own conclusions
5. Iterate autonomously when evidence is weak
6. Produce reports understandable by humans
7. Maintain traceable reasoning history

---

## 4. High-Level Architecture

┌────────────────────┐
│ Raw Dataset │
└─────────┬──────────┘
↓
┌────────────────────┐
│ Exploration Agent │
│ - Structure │
│ - Distributions │
│ - Correlations │
└─────────┬──────────┘
↓
┌────────────────────┐
│ Hypothesis Agent │
│ - Scientific logic │
│ - Measurable ideas │
└─────────┬──────────┘
↓
┌────────────────────┐
│ Experiment Agent │
│ - Statistical test │
│ - Significance │
└─────────┬──────────┘
↓
┌────────────────────┐
│ Critic Agent │
│ - Bias detection │
│ - Validity checks │
│ - Iterate decision │
└─────────┬──────────┘
↓
┌────────────────────┐
│ Memory System │
│ - Reasoning logs │
│ - Iteration trace │
└─────────┬──────────┘
↓
┌────────────────────┐
│ Report Agent │
│ - Human language │
│ - Insights │
│ - Recommendations │
└────────────────────┘

---

## 5. Agent Responsibilities (DEEP EXPLANATION)

### 5.1 Exploration Agent

**Purpose:**  
Understand the dataset *before* asking any questions.

**Responsibilities:**
- Identify dataset size and structure
- Detect missing values
- Compute descriptive statistics
- Detect strongest numerical correlations
- Surface unexpected relationships

**Why this matters:**  
Human analysts often miss patterns because they search for answers too early.

---

### 5.2 Hypothesis Generation Agent

**Purpose:**  
Convert observed patterns into **scientific hypotheses**.

**Properties of generated hypotheses:**
- Measurable
- Falsifiable
- Testable using available data

**Example:**
> “Employees with longer tenure tend to have higher salaries.”

This agent uses **LLM reasoning**, not rules.

---

### 5.3 Experiment Agent

**Purpose:**  
Objectively validate hypotheses using statistics.

**Current capabilities:**
- Pearson correlation testing
- p-value significance testing
- Effect size interpretation

**Why statistics are essential:**  
LLMs reason — statistics validate.

---

### 5.4 Critic & Decision Agent

**Purpose:**  
Act as a skeptical reviewer.

**Responsibilities:**
- Detect spurious correlations
- Identify possible confounding variables
- Evaluate sample size adequacy
- Decide whether evidence is sufficient
- Trigger additional iterations if needed

This agent prevents **false confidence**.

---

### 5.5 Memory System

**Purpose:**  
Persist agent reasoning across steps.

**What is stored:**
- Exploration outputs
- Hypotheses
- Experiment results
- Critic evaluations
- Iteration decisions

**Why memory matters:**  
Stateless systems cannot reflect or improve.

---

### 5.6 Report Generation Agent

**Purpose:**  
Translate technical reasoning into **human-readable insights**.

**Outputs:**
- Executive summary
- Key findings
- Hypotheses and validation
- Limitations
- Recommendations

This mirrors **real research reports**.

---

## 6. Technology Stack (WHY EACH TOOL IS USED)

| Component | Technology | Reason |
|---------|-----------|-------|
| Language | Python | Industry standard for ML |
| Data | Pandas, NumPy | Efficient data manipulation |
| Statistics | SciPy | Reliable scientific testing |
| LLM | OpenAI API | Advanced reasoning |
| Architecture | Modular Agents | Clean separation of concerns |
| Memory | JSON | Transparent and auditable |
| Dashboard | Streamlit | Fast introspection |
| Env Mgmt | Virtualenv | Dependency isolation |

---

## 7. Project Structure (Detailed)

app/
│
├── main.py
│ └── Orchestrates agent execution & iteration
│
├── config.py
│ └── Environment configuration
│
├── agents/
│ ├── explorer_agent.py
│ ├── hypothesis_agent.py
│ ├── experiment_agent.py
│ ├── critic_agent.py
│ └── report_agent.py
│
├── core/
│ ├── dataset_loader.py
│ ├── statistics.py
│ └── memory.py
│
├── llm/
│ ├── llm_client.py
│ └── prompts.py
│
└── dashboard.py

---

## 8. Installation & Setup (FULL) 

### Step 1: Clone Repository
```bash
git clone https://github.com/<your-username>/ai-scientific-discovery-agent.git
cd ai-scientific-discovery-agent

### Step 2: Create Virtual Environment
python -m venv venv
venv\Scripts\activate

###Step 3: Install Dependencies
pip install -r requirements.txt

###Step 4: Configure Environment
OPENAI_API_KEY=your_api_key

### 9. Running the System
python -m app.main

## 9. Execution Flow

1. Dataset is loaded into the system  
2. Exploration agent analyzes dataset structure, distributions, and correlations  
3. Hypothesis generation agent creates scientific, testable hypotheses  
4. Experiment agent executes statistical validation using appropriate tests  
5. Critic agent evaluates result validity, bias, and evidence strength  
6. Iteration decision is made (continue analysis or stop)  
7. Agent memory is updated with reasoning and decisions  
8. Final scientific report is produced  

---

## 10. Dashboard Usage

Run the dashboard using the following command:

```bash
streamlit run app/dashboard.py



