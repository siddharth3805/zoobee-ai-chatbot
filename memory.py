# memory.py — Manages in-memory conversation history

class ChatMemory:
    """Stores and manages conversation history as a list of message objects."""

    def __init__(self, system_prompt: str):
        self.history = [
            {"role": "system", "content": system_prompt}
        ]

    def add_user_message(self, content: str):
        self.history.append({"role": "user", "content": content})

    def add_assistant_message(self, content: str):
        self.history.append({"role": "assistant", "content": content})

    def get_history(self) -> list:
        return self.history

    def get_display_history(self) -> list:
        """Return history without the system prompt (for display in UI)."""
        return [msg for msg in self.history if msg["role"] != "system"]

    def clear(self):
        system = self.history[0]
        self.history = [system]

    def message_count(self) -> int:
        return len(self.history) - 1

    def trim_to_limit(self, max_messages: int = 20):
        """Keep only the last N messages to avoid token limit issues."""
        system = self.history[0]
        messages = self.history[1:]
        if len(messages) > max_messages:
            messages = messages[-max_messages:]
        self.history = [system] + messages