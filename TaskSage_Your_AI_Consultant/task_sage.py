import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

API_KEY = os.getenv("YOUR_GROQ_API_KEY")
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

    response = client.chat.completions.create(
    messages=[{"role": "user", "content": prompt}],
    model="llama3-8b-8192"  # Use the supported model
)


    return response.choices[0].message.content

def main():
    print("🧙‍♂️ Task Sage – Your AI Consultant")
    while True:
        task = input("Enter a task (or type 'exit' to quit): ")
        if task.lower() == 'exit':
            break
        result = analyze_task(task)
        print("Result:", result)
        print("-" * 50)

if __name__ == "__main__":
    main()
