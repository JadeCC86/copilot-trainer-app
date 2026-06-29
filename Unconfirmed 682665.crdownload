import streamlit as st
from openai import OpenAI
import os

# Load your API key from env.txt
with open("env.txt", "r", encoding="utf-8") as f:
    for line in f:
        line = line.strip()
        if "=" in line:
            key, value = line.split("=", 1)
            os.environ[key] = value

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

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
