import streamlit as st
from adventurer.parser import parse
from adventurer.scoring import sort_tasks

if "tasks" not in st.session_state:
    st.session_state["tasks"] = []

st.title("Adventurer")
dump = st.text_area("Brain Dump Here!")

if st.button("Add Tasks") and dump:
    with st.spinner("Thinking..."):
        tasks = parse(dump)
    st.session_state["tasks"].extend(tasks)

st.session_state["tasks"] = sort_tasks(st.session_state["tasks"])

i = 0
st.write(st.session_state["tasks"][i])

if st.button("Done!"):
    st.session_state["tasks"] = st.session_state["tasks"][1:]

if st.button("Not Now!"):
    i += 1
    st.write(st.session_state["tasks"][i])
