import json
from datetime import datetime
from pathlib import Path

MEMORY_FILE = Path("agent_memory.json")

def load_memory() -> dict:
    if MEMORY_FILE.exists():
        return json.loads(MEMORY_FILE.read_text())
    return {"history": []}

def save_memory(entry: dict):
    memory = load_memory()
    memory["history"].append({
        "timestamp": datetime.utcnow().isoformat(),
        **entry
    })
    MEMORY_FILE.write_text(json.dumps(memory, indent=2))
