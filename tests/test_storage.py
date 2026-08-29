from datetime import date, timedelta, datetime
from adventurer.task import Task
from adventurer.storage import task_to_dict, dict_to_task

task1 = Task('Code', None, 2)
task2 = Task('CodeAGAIN', date(2026, 8, 20), 3)

def test_task_dict_undated():
    assert dict_to_task(task_to_dict(task1)) == task1

def test_task_dict_dated():
    assert dict_to_task(task_to_dict(task2)) == task2
