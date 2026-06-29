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
