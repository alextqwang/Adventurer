from datetime import date
from typing import Optional
from dataclasses import dataclass

@dataclass
class Task:
    text: str
    deadline: Optional[date]
    importance: int
    completed: bool = False
