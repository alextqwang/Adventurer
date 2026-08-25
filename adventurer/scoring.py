from datetime import date
from typing import Optional

from adventurer.task import Task

# CONSTANTS
URGENCY_ANCHORS = [(0, 1.0), (2, 0.9), (3, 0.7), (7, 0.5), (8, 0.25), (14, 0.1), (30, 0.0)]

def urgency(deadline: Optional[date]) -> float:
    if not deadline:
        return 0.0
    days_left = (deadline - date.today()).days
    if days_left >= 30:
        return 0.0
    elif days_left <= 0:
        return 1.0
    else:
        return _find_urgency(days_left)

def _find_urgency(days: int) -> float:
    """ Assume 0 < days < 30, _find_urgency is a helper to calculate the correct
    urgency value using linear interpolation """
    i = 0
    while days > URGENCY_ANCHORS[i][0]:
        i += 1
    anchor1 = URGENCY_ANCHORS[i - 1]
    anchor2 = URGENCY_ANCHORS[i]
    urgency_value = (anchor1[1] - anchor2[1]) / (anchor2[0] - anchor1[0]) * (anchor2[0] - days) + anchor2[1]
    return urgency_value

def score(task: Task) -> float:
    task_urgency = urgency(task.deadline)
    return task.importance * (0.5 + task_urgency)


