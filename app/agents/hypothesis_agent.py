from app.llm.llm_client import call_llm
from app.llm.prompts import HYPOTHESIS_PROMPT

def generate_hypotheses(exploration_result: dict) -> str:
    user_prompt = f"""
Dataset exploration results:
{exploration_result}

Generate 3 scientific hypotheses.
"""
    return call_llm(HYPOTHESIS_PROMPT, user_prompt)
