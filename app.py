# app.py — Main Streamlit web interface

import streamlit as st
from chatbot import ChatBot
from memory import ChatMemory
from prompts import SYSTEM_PROMPT, WELCOME_MESSAGE
from utils import save_chat_history

# ─── Page Configuration ─────────────────────────────────────────────
st.set_page_config(
    page_title="Zoobee — AI Chatbot with Memory",
    page_icon="🐝",
    layout="centered",
)

# ─── Initialize Session State ────────────────────────────────────────
def init_session():
    if "memory" not in st.session_state:
        st.session_state.memory = ChatMemory(SYSTEM_PROMPT)

    if "chatbot" not in st.session_state:
        try:
            st.session_state.chatbot = ChatBot()
        except ValueError as e:
            st.error(f"❌ {e}")
            st.stop()


# ─── Sidebar ─────────────────────────────────────────────────────────
with st.sidebar:
    st.title("⚙️ Settings")

    if "memory" in st.session_state:
        msg_count = st.session_state.memory.message_count()
        st.metric("💬 Messages in Memory", msg_count)

    st.divider()

    if st.button("🗑️ Clear Conversation", use_container_width=True):
        if "memory" in st.session_state:
            st.session_state.memory.clear()
        st.rerun()

    if st.button("💾 Save Chat History", use_container_width=True):
        if "memory" in st.session_state:
            history = st.session_state.memory.get_history()
            filepath = save_chat_history(history)
            st.success(f"Saved to {filepath}")

    st.divider()
    st.caption("🔒 Powered by Groq (Llama 3.3)")
    st.caption("Built for Innovexa Catalyst")


# ─── Main App ────────────────────────────────────────────────────────
st.title("🐝 Zoobee")
st.caption("Your AI chatbot that remembers our entire conversation!")

init_session()

# Display chat history
history = st.session_state.memory.get_display_history()

if not history:
    with st.chat_message("assistant"):
        st.write(WELCOME_MESSAGE)
else:
    for msg in history:
        with st.chat_message(msg["role"]):
            st.write(msg["content"])

# ─── Chat Input ──────────────────────────────────────────────────────
user_input = st.chat_input("Type your message here...")

if user_input:
    with st.chat_message("user"):
        st.write(user_input)

    st.session_state.memory.add_user_message(user_input)
    st.session_state.memory.trim_to_limit(max_messages=20)

    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            response = st.session_state.chatbot.get_response(
                st.session_state.memory.get_history()
            )
        st.write(response)

    st.session_state.memory.add_assistant_message(response)