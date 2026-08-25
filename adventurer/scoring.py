from datetime import date
from typing import Optional

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
        return find_urgency(days_left)

def find_urgency(days: int) -> float:
    i = 0
    while days > URGENCY_ANCHORS[i][0]:
        i += 1
    anchor1 = URGENCY_ANCHORS[i - 1]
    anchor2 = URGENCY_ANCHORS[i]
    urgency_value = (anchor1[1] - anchor2[1]) / (anchor2[0] - anchor1[0]) * (anchor2[0] - days) + anchor2[1]
    return urgency_value



