# noinspection PyProtectedMember
from adventurer.parser import _response_to_tasks

s = "oh my god, I really need to finish this hackathon project I made for myself... I want to finish it by tomorrow and it's the most important thing I could possibly be doing right now... I also need to finish cleaning my house, this is less important but I need to do it in a week. And also I have to make a doctor's appointment, this is very important as well."
tasks = _response_to_tasks('{"tasks": [{"text": "Finish hackathon project", "deadline": "2026-09-01", "importance": 3}, {"text": "Clean the house", "deadline": "2026-09-07", "importance": 1}, {"text": "Make doctor\'s appointment", "deadline": null, "importance": 3}]}')

def test_parse_number():
    assert len(tasks) == 3

def test_parse_deadlines():
    task3 = tasks[2]
    assert task3.deadline is None

def test_response_to_tasks_error():
    assert _response_to_tasks('hello') == []

