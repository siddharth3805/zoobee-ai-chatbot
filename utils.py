# utils.py — Utility/helper functions

import json
import os
from datetime import datetime


def save_chat_history(history: list, filename: str = "chat_history.json"):
    """Save chat history to a JSON file."""
    data_dir = "data"
    os.makedirs(data_dir, exist_ok=True)
    filepath = os.path.join(data_dir, filename)
    with open(filepath, "w", encoding="utf-8") as f:
        json.dump(history, f, indent=2, ensure_ascii=False)
    return filepath


def get_timestamp() -> str:
    """Return current timestamp as string."""
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")