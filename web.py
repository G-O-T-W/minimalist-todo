import streamlit as st
import functions

todos = functions.read_todos()


def add_todo():
    """
    This function adds a new todo item to
    the list and writes the updated list
    to the file
    """
    new_todo = st.session_state["new-todo"].title() + "\n"

    todos.append(new_todo)
    functions.write_todos(todos)

    # To blank the input_text field after adding todo in list
    st.session_state["new-todo"] = ""


st.title("Minimalist Todo")
st.subheader("A minimalistic to-do app for the minimalist in you")

st.text_input(label="", placeholder="Enter a todo...",
              key="new-todo", on_change=add_todo,
              help="Please add the todo you want on the list",
              label_visibility="collapsed")

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        # to delete todo from session_state dictionary
        del st.session_state[todo]
        st.rerun()



