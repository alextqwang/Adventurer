from adventurer.scoring import urgency, score, sort_tasks
from datetime import date, timedelta
from adventurer.task import Task


def test_urgency_no_deadline():
    assert urgency(None) == 0

def test_urgency_overdue():
    assert urgency(date.today() + timedelta(days = -1)) == 1

def test_urgency_today():
    assert urgency(date.today()) == 1

def test_urgency_week():
    assert urgency(date.today() + timedelta(days = 7)) == 0.5

def test_urgency_year():
    assert urgency(date.today() + timedelta(days = 365)) == 0

task1 = Task('Code', None, 2)
task2 = Task('Code', date.today() + timedelta(days = 8), 1)
task3 = Task('Code', date.today() + timedelta(days = 8), 1)
task4 = Task('Code', date.today() + timedelta(days = 7), 1)

def test_score():
    assert score(task1) == 1

def test_score_ordering():
    assert score(task1) > score(task2)

def test_sort_tasks():
    assert sort_tasks([task1, task2, task3, task4]) == [task4, task1, task2, task3]
