from app.llm.llm_client import call_llm
from app.llm.prompts import CRITIC_PROMPT

def critique_and_decide(hypotheses, experiment_results) -> dict:
    user_prompt = f"""
Hypotheses:
{hypotheses}

Experiment Results:
{experiment_results}

1. Are results valid?
2. Any bias or weak evidence?
3. Should we run another experiment? (YES or NO)
Return structured decision.
"""

    response = call_llm(CRITIC_PROMPT, user_prompt)

    decision = "YES" if "YES" in response.upper() else "NO"

    return {
        "analysis": response,
        "should_iterate": decision == "YES"
    }
