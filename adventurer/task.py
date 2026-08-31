from datetime import date, datetime
from typing import Optional
from dataclasses import dataclass, field

@dataclass
class Task:
    text: str
    deadline: Optional[date]
    importance: int
    completed: bool = False
    created_at: datetime = field(default_factory = datetime.now)
    snoozed_until: Optional[date] = None
