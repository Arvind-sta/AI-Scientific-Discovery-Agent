from app.llm.llm_client import call_llm
from app.llm.prompts import REPORT_PROMPT

def generate_report(exploration, hypotheses, experiments, critique):
    user_prompt = f"""
Exploration:
{exploration}

Hypotheses:
{hypotheses}

Experiments:
{experiments}

Critique:
{critique}

Generate final insight report.
"""
    return call_llm(REPORT_PROMPT, user_prompt)
