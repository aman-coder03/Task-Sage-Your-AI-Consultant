import streamlit as st
import os
from dotenv import load_dotenv
from groq import Groq

# Load API key from .env
load_dotenv()
API_KEY = os.getenv("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")
client = Groq(api_key=API_KEY)

def analyze_task(task):
    prompt = f"""
    You are Task Sage – Your AI Consultant. For the task below:
    Task: {task}

    1. Assign a priority: High, Medium, Low.
    2. Suggest an ideal deadline (like '2 days', '1 week', 'Today').
    3. Give a "Focus Score" between 1-100 (higher = more urgent).
    4. Offer a witty, motivational tip (max 1 line).

    Respond strictly in this JSON format:
    {{
        "priority": "...",
        "deadline": "...",
        "focus_score": ...,
        "tip": "..."
    }}
    """

    # ✅ Correct Model: llama3-8b-8192
    response = client.chat.completions.create(
        messages=[{"role": "user", "content": prompt}],
        model="llama3-8b-8192"  # Use the supported model
    )

    return response.choices[0].message.content

# Streamlit UI
st.title("🧙‍♂️ Task Sage – Your AI Consultant")
task_input = st.text_area("Enter your task here:", "")

if st.button("Analyze Task"):
    if task_input.strip() == "":
        st.warning("Please enter a task!")
    else:
        with st.spinner("Analyzing your task..."):
            result = analyze_task(task_input)
            st.json(result)
