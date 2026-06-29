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
persona = st.sidebar.selectbox(
    "Trainer personality:",
    [
        "Friendly Coach",
        "Strict Instructor",
        "Corporate Trainer",
        "AI Expert",
        "Funny Mentor"
    ],
    key="trainer_persona"
)
SYSTEM_PROMPT = f"""
You are my Microsoft 365 & Copilot Trainer Coach.

Training mode: {mode}
Personality: {persona}

Personality behaviours:
- Friendly Coach: warm, encouraging, supportive, uses simple language.
- Strict Instructor: direct, no-nonsense, structured, expects precision.
- Corporate Trainer: professional, polished, business-focused.
- AI Expert: highly technical, fast-paced, deep explanations.
- Funny Mentor: humorous, light-hearted, uses jokes while teaching.

Adapt your tone, style, and explanations to match the selected personality.
Always provide structured, practical training guidance.
"""
import datetime

st.sidebar.subheader("Conversation History")

# Persona colour accents + gradients
persona_gradients = {
    "Friendly Coach": "linear-gradient(135deg, #A8E6CF, #4CAF50)",
    "Strict Instructor": "linear-gradient(135deg, #FFCDD2, #D32F2F)",
    "Corporate Trainer": "linear-gradient(135deg, #BBDEFB, #1976D2)",
    "AI Expert": "linear-gradient(135deg, #E1BEE7, #7B1FA2)",
    "Funny Mentor": "linear-gradient(135deg, #FFE0B2, #FF9800)"
}

accent_gradient = persona_gradients.get(persona, "linear-gradient(135deg, #D1C4E9, #7b61ff)")

# Inject CSS for premium animated styling
st.sidebar.markdown(
    f"""
    <style>
        .history-wrapper {{
            max-height: 380px;
            overflow-y: auto;
            padding-right: 8px;
            position: relative;
        }}

        .history-top-fade {{
            position: absolute;
            top: 0;
            left: 0;
            right: 0;
            height: 30px;
            background: linear-gradient(to top, transparent, #ffffff);
            z-index: 2;
        }}

        .history-bottom-fade {{
            position: absolute;
            bottom: 0;
            left: 0;
            right: 0;
            height: 40px;
            background: linear-gradient(to bottom, transparent, #ffffff);
            z-index: 2;
        }}

        .bubble {{
            padding: 12px 14px;
            margin-bottom: 12px;
            border-radius: 14px;
            box-shadow: 0px 2px 6px rgba(0,0,0,0.12);
            font-size: 13px;
            line-height: 1.5;
            animation: fadeIn 0.3s ease-in-out;
        }}

        .bubble-user {{
            background: #e8f3ff;
            border-left: 5px solid #1a73e8;
        }}

        .bubble-assistant {{
            background: #f4edff;
            border-left: 5px solid transparent;
            border-image: {accent_gradient} 1;
        }}

        .bubble-role {{
            font-weight: bold;
            margin-bottom: 6px;
            display: flex;
            align-items: center;
            gap: 6px;
        }}

        .avatar {{
            width: 20px;
            height: 20px;
            border-radius: 50%;
            background-size: cover;
            background-position: center;
        }}

        .timestamp {{
            font-size: 11px;
            color: #777;
            margin-top: 8px;
            text-align: right;
        }}

        @keyframes fadeIn {{
            from {{ opacity: 0; transform: translateY(4px); }}
            to {{ opacity: 1; transform: translateY(0); }}
        }}

        .clear-btn {{
            background-color: #f8f8f8;
            padding: 8px 12px;
            border-radius: 6px;
            border: 1px solid #ccc;
            text-align: center;
            cursor: pointer;
            transition: 0.2s;
        }}

        .clear-btn:hover {{
            background-color: #e6e6e6;
        }}
    </style>
    """,
    unsafe_allow_html=True
)

# Scrollable history container
st.sidebar.markdown('<div class="history-wrapper">', unsafe_allow_html=True)
st.sidebar.markdown('<div class="history-top-fade"></div>', unsafe_allow_html=True)

if "history" in st.session_state and len(st.session_state.history) > 0:
    for chat in st.session_state.history:
        role = chat["role"]
        content = chat["content"]
        timestamp = datetime.datetime.now().strftime("%H:%M")

        if role == "user":
            avatar = "background-image: url('https://i.imgur.com/4ZQZ4ZQ.png');"
            st.sidebar.markdown(
                f"""
                <div class="bubble bubble-user">
                    <div class="bubble-role">
                        <div class="avatar" style="{avatar}"></div>
                        🧑 You
                    </div>
                    {content}
                    <div class="timestamp">{timestamp}</div>
                </div>
                """,
                unsafe_allow_html=True
            )
        else:
            avatar = "background-image: url('https://i.imgur.com/8Km9tLL.png');"
            st.sidebar.markdown(
                f"""
                <div class="bubble bubble-assistant">
                    <div class="bubble-role">
                        <div class="avatar" style="{avatar}"></div>
                        🤖 Trainer
                    </div>
                    {content}
                    <div class="timestamp">{timestamp}</div>
                </div>
                """,
                unsafe_allow_html=True
            )
else:
    st.sidebar.write("No messages yet.")

st.sidebar.markdown('<div class="history-bottom-fade"></div>', unsafe_allow_html=True)
st.sidebar.markdown('</div>', unsafe_allow_html=True)

# Clear history button
if st.sidebar.button("🗑️ Clear chat history"):
    st.session_state.history = []
first_name = st.sidebar.text_input("Your first name:", key="user_first_name")
if first_name:
    st.session_state.first_name = first_name
    st.sidebar.subheader("Copilot Prompt Builder")

goal = st.sidebar.selectbox(
    "What do you want Copilot to do?",
    [
        "Summarise text",
        "Rewrite text",
        "Draft an email",
        "Create a PowerPoint outline",
        "Analyse a document",
        "Explain something simply"
    ],
    key="prompt_goal"
)

tone = st.sidebar.selectbox(
    "Choose tone:",
    ["Professional", "Friendly", "Direct", "Formal", "Casual"],
    key="prompt_tone"
)

output_format = st.sidebar.selectbox(
    "Output format:",
    ["Paragraph", "Bullet points", "Step-by-step", "Short summary"],
    key="prompt_format"
)

extra_details = st.sidebar.text_area(
    "Add extra details (optional):",
    key="prompt_extra"
)

if st.sidebar.button("Generate Copilot Prompt"):
    built_prompt = (
        f"Goal: {goal}\n"
        f"Tone: {tone}\n"
        f"Format: {output_format}\n"
        f"Details: {extra_details if extra_details else 'None'}"
    )

    st.sidebar.markdown("### Your Copilot Prompt")
    st.sidebar.code(built_prompt)
st.sidebar.subheader("Trainer Tips")

tips = [
    "Use @ to reference files directly in Copilot.",
    "Ask Copilot to rewrite text in different tones.",
    "Use Copilot in Teams to summarise meetings instantly.",
    "Ask Copilot to extract action items from long text.",
    "Use Copilot in Word to generate outlines before writing.",
    "Ask Copilot to explain complex topics in simple language."
]

for tip in tips:
    st.sidebar.markdown(f"- {tip}")
    st.sidebar.subheader("Copilot Prompt Library")

prompt_library = {
    "Summarise a document": "Summarise the following content and highlight key points, decisions, and action items.",
    "Rewrite professionally": "Rewrite this text in a professional, concise tone suitable for business communication.",
    "Rewrite casually": "Rewrite this text in a friendly, conversational tone.",
    "Draft an email": "Draft a clear, structured email based on the following details.",
    "Create a PowerPoint outline": "Create a PowerPoint outline with slide titles and bullet points for this topic.",
    "Extract action items": "Extract all action items, deadlines, and responsibilities from the following text.",
    "Explain simply": "Explain this topic in simple, beginner-friendly language.",
    "Analyse text": "Analyse this text and provide insights, risks, opportunities, and recommendations.",
    "Turn notes into a summary": "Convert these rough notes into a clean, structured summary.",
    "Turn notes into a plan": "Convert these notes into a step-by-step plan with clear actions."
}

for label, prompt in prompt_library.items():
    if st.sidebar.button(label):
        st.session_state.history.append({"role": "user", "content": prompt})
        import datetime

st.sidebar.subheader("✨ Prompt of the Day")

daily_prompts = [
    "Summarise this text and highlight key decisions and action items.",
    "Rewrite this message in a professional, concise tone.",
    "Create a PowerPoint outline with slide titles and bullet points for this topic.",
    "Extract all action items, deadlines, and responsibilities from the following text.",
    "Explain this concept in simple language suitable for a beginner.",
    "Turn these rough notes into a structured summary.",
    "Analyse this text and provide insights, risks, and recommendations.",
    "Rewrite this text in a friendly, conversational tone.",
    "Draft a clear, structured email based on the following details.",
    "Convert these notes into a step-by-step plan with clear actions."
]

# Pick prompt based on day of year
day_index = datetime.datetime.now().timetuple().tm_yday % len(daily_prompts)
prompt_of_the_day = daily_prompts[day_index]

st.sidebar.markdown(f"**{prompt_of_the_day}**")

# Button to send it into the chat
if st.sidebar.button("Use Prompt of the Day"):
    st.session_state.history.append({"role": "user", "content": prompt_of_the_day})



user_name = st.session_state.get("first_name", "friend")
