import streamlit as st
from adventurer.parser import parse
from adventurer.scoring import sort_tasks
from datetime import date, timedelta
from adventurer.storage import save, load

TASKS_PATH = "tasks.json"

if "tasks" not in st.session_state:
    st.session_state["tasks"] = load(TASKS_PATH)

def add_tasks():
    dump = st.session_state["dump"]
    if not dump:
        return
    with st.spinner("Thinking..."):
        tasks = parse(dump)
    st.session_state["tasks"].extend(tasks)
    save(st.session_state["tasks"], TASKS_PATH)
    st.session_state["dump"] = ""

st.title("Adventurer")
st.text_area("Brain Dump Here!", key = "dump")

st.button("Add Tasks", on_click=add_tasks)

st.session_state["tasks"] = sort_tasks(st.session_state["tasks"])
current_session = [task for task in st.session_state["tasks"] if task.snoozed_until is None or task.snoozed_until <= date.today()]

if current_session:
    current_task = current_session[0]
    st.subheader(current_task.text)
    if current_task.deadline is not None:
        st.write(f"Deadline: {current_task.deadline}")
    else:
        st.write("No Deadline")
    if st.button("Done!"):
        st.session_state["tasks"].remove(current_task)
        save(st.session_state["tasks"], TASKS_PATH)
        st.rerun()
    if st.button("Not Now..."):
        current_task.snoozed_until = date.today() + timedelta(days = 1)
        save(st.session_state["tasks"], TASKS_PATH)
        st.rerun()
else:
    st.write("No more tasks!")


