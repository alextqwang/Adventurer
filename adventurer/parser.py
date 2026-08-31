from datetime import date
from adventurer.task import Task
import ollama
import json

SYSTEM_PROMPT = f"""Extract every task from the user's message. The user may mention several tasks in one rambling message - return one object for each.

Return JSON in this exact shape:
{{"tasks": [{{"text": "...", "deadline": "...", "importance": 1}}]}}

Rules for each task:
- text: a short description of the task
- deadline: ISO format YYYY-MM-DD, or null if no deadline was mentioned
- importance: 1 (not very important), 2 (moderately important), or 3 (very important). Default to 1 if not mentioned.

Today's date is {date.today().isoformat()}.

Example input: "need to email my prof by friday, and at some point I should really clean the kitchen"
Example output: {{"tasks": [{{"text": "Email professor", "deadline": "2026-09-04", "importance": 2}}, {{"text": "Clean the kitchen", "deadline": null, "importance": 1}}]}}"""

def parse(user_input: str) -> list[Task]:
    response = ollama.chat(
        model="llama3.1:8b",
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": user_input}
        ],
        format = "json"
    )

    parsed_dicts = json.loads(response.message.content)["tasks"]
    
