import streamlit as st
from openai import OpenAI
import os

# Load your API key.
import streamlit as st
from openai import OpenAI

client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

SYSTEM_PROMPT = """
You are my Microsoft 365 & Copilot Trainer Coach.
Provide structured, practical training guidance.
"""

def ask_agent(message):
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": message}
        ],
        temperature=0.4,
    )
    return response.choices[0].message.content

# Streamlit UI
st.title("Copilot Trainer Studio")

task = st.text_area("Enter your trainer task:")

if st.button("Run"):
    reply = ask_agent(task)
    st.markdown(reply)
st.sidebar.title("Trainer Settings")

mode = st.sidebar.selectbox(
    "Choose training mode:",
    ["Beginner", "Intermediate", "Advanced"]
)
SYSTEM_PROMPT = f"""
You are my Microsoft 365 & Copilot Trainer Coach.

Training mode: {mode}

Beginner = gentle, step-by-step guidance.
Intermediate = practical, structured coaching.
Advanced = expert-level, fast, technical instruction.

Provide structured, practical training guidance.
"""
if "history" not in st.session_state:
    st.session_state.history = []
for chat in st.session_state.history:
    with st.chat_message(chat["role"]):
        st.write(chat["content"])
user_input = st.chat_input("Ask your trainer...")
if user_input:
    st.session_state.history.append({"role": "user", "content": user_input})
def ask_agent(history):
    messages = [{"role": "system", "content": SYSTEM_PROMPT}] + history

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=messages
    )

    return response.choices[0].message.content
assistant_reply = ask_agent(st.session_state.history)
st.session_state.history.append({"role": "assistant", "content": assistant_reply})
with st.chat_message("assistant"):
    st.write(assistant_reply)



