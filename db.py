from flask import Flask, request, jsonify
import requests
import mysql.connector
import json
import os

app = Flask(__name__)

# =======================
# CONFIG
# =======================

# 🔐 Set your OpenRouter API key as environment variable
# export OPENROUTER_API_KEY="your_key_here"
OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")

OPENROUTER_URL = "https://openrouter.ai/api/v1/chat/completions"

DB_CONFIG = {
    "host": "localhost",
    "user": "root",            # change if needed
    "password": "password",    # change if needed
    "database": "email_tasks_db"
}

# =======================
# DB CONNECTION
# =======================

def get_db_connection():
    return mysql.connector.connect(**DB_CONFIG)

# =======================
# HOME
# =======================

@app.route("/", methods=["GET"])
def home():
    return "Flask server with MySQL is running successfully 🚀"

# =======================
# LLM EMAIL ANALYSIS
# =======================

def analyze_email_with_llm(subject, body):
    prompt = f"""
Analyze the following email and convert it into a well-structured task.

Email Subject: {subject}
Email Body: {body}

Return STRICT JSON only with:
- title
- description
- priority (low / medium / high)
"""

    headers = {
        "Authorization": f"Bearer {OPENROUTER_API_KEY}",
        "Content-Type": "application/json"
    }

    payload = {
        "model": "openai/gpt-3.5-turbo",
        "messages": [
            {"role": "user", "content": prompt}
        ],
        "temperature": 0.2
    }

    response = requests.post(OPENROUTER_URL, headers=headers, json=payload)
    content = response.json()["choices"][0]["message"]["content"]

    return json.loads(content)

# =======================
# API 1: EMAIL WEBHOOK
# =======================

@app.route("/webhook/email", methods=["POST"])
def receive_email():
    data = request.get_json()
    subject = data.get("subject", "No Subject")
    body = data.get("body", "")

    task = analyze_email_with_llm(subject, body)

    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        INSERT INTO tasks (title, description, priority, status)
        VALUES (%s, %s, %s, %s)
        """,
        (
            task["title"],
            task["description"],
            task["priority"],
            "pending"
        )
    )

    conn.commit()
    cursor.close()
    conn.close()

    return jsonify({
        "message": "Email analyzed and task saved to database",
        "task": task
    })

# =======================
# API 2: GET ALL TASKS
# =======================

@app.route("/tasks", methods=["GET"])
def get_tasks():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)

    cursor.execute("SELECT * FROM tasks")
    tasks = cursor.fetchall()

    cursor.close()
    conn.close()

    return jsonify(tasks)

# =======================
# RUN
# =======================

if __name__ == "__main__":
    app.run(debug=True)
