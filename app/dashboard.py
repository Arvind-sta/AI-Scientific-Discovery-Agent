import json
import streamlit as st
from pathlib import Path

st.set_page_config(page_title="AI Discovery Agent", layout="wide")

st.title("🧠 AI Scientific Discovery Agent")

memory_file = Path("agent_memory.json")

if not memory_file.exists():
    st.warning("No agent memory found. Run the agent first.")
else:
    memory = json.loads(memory_file.read_text())

    for entry in memory["history"]:
        with st.expander(f"{entry['stage']} | {entry['timestamp']}"):
            st.json(entry)
