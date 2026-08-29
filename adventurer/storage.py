from adventurer.task import Task
from datetime import date, datetime
from dataclasses import asdict, dataclass

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


# def save(tasks: list[Task], path: str) -> None:
#
