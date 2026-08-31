from datetime import date, datetime
from adventurer.task import Task
from adventurer.storage import task_to_dict, dict_to_task, save, load

task1 = Task('Code', None, 2)
task2 = Task('CodeAGAIN', date(2026, 8, 20), 3)

def test_task_dict_undated():
    assert dict_to_task(task_to_dict(task1)) == task1

def test_task_dict_dated():
    assert dict_to_task(task_to_dict(task2)) == task2

def test_save_load(tmp_path):
    p = tmp_path / "test_tasks.json"
    save([task1, task2], p)
    assert load(p) == [task1, task2]

def test_file_not_found(tmp_path):
    assert load(tmp_path / "hello.json") == []
