# Adventurer
Adventurer lets you dump every task in your head at once, then shows you only the next one, so you can start working instead of waiting for the next step.

## Status
Finished first version, very choppy but it works on streamlit. 

## How to run?
Clone and venv, pip install -r requirements.txt, install Ollama, ollama pull llama3.1:8b, streamlit run app.py

## How it works?
Just write out whatever's on your mind that you need to do. Describe it with as much detail as you want,
and Ollama will extract all the tasks with deadlines. It'll score it by how close the deadline is and 
how important you may have specified it to be, then it'll give you ONE task to complete -- whichever 
it thinks is the most important.

## OTHER THINGS BELOW
Probably could add quite a bit more, this is just a test so far.
