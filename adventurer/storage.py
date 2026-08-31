from adventurer.task import Task
from datetime import date, datetime
from dataclasses import asdict, dataclass
import json
from pathlib import Path

def task_to_dict(task: Task) -> dict:
    task_dict = asdict(task)
    task_dict['deadline'] = task.deadline.isoformat() if task.deadline is not None else None
    task_dict['created_at'] = task.created_at.isoformat()
    return task_dict

def dict_to_task(d: dict) -> Task:
    """Precondition: d is already formatted"""
    text = d["text"]
    deadline = date.fromisoformat(d["deadline"]) if d["deadline"] is not None else None
    importance = d["importance"]
    completed = d["completed"]
    created_at = datetime.fromisoformat(d["created_at"])
    return Task(text, deadline, importance, completed, created_at)

def save(tasks: list[Task], path: str | Path) -> None:
    readable_tasks = [task_to_dict(task) for task in tasks]
    with open(path, "w") as file:
        json.dump(readable_tasks, file, indent = 2)

def load(path: str | Path) -> list[Task]:
    try:
        with open(path, "r") as file:
            data = json.load(file)
        task_list = [dict_to_task(d) for d in data]
        return task_list
    except FileNotFoundError:
        return []
