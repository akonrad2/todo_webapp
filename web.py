import streamlit as st
import functionsDict
# http://localhost:8501

try:
    todos = functionsDict.get_todos()
except FileNotFoundError:
    with open("todos.txt", 'w') as f:
        pass
    todos = {}

def add_todo():
    this_todo = st.session_state["new_todo"] + "\n"
    todos[this_todo] = 1
    functionsDict.write_todos(todos.keys())

st.title("My To-Do List")
st.subheader("(for a more organized procrastination experience)")
st.write("Click boxes next to completed items to remove them.")

checkDupl = {}
deleteItem= {}
for key in todos.keys():
    if key in checkDupl:
        continue
    else:
        checkDupl[key] = 1
        checkbox=st.checkbox(key, key=key)
        if checkbox:
            #deleteItem[key] = 1
            todos.pop(key)
            functionsDict.write_todos(todos.keys())
            del st.session_state[key]
            st.experimental_rerun()

st.text_input(label="",
              placeholder="Add or edit a to-do...",
              on_change=add_todo,
              key="new_todo")
