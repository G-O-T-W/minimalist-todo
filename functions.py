FILEPATH = "todos.txt"


def read_todos(filepath=FILEPATH) -> list:
    """
        Read a list of to-dos from a text file and return
        it as a list.
    """
    with open(filepath, 'r') as local_file:
        list_of_todos = local_file.readlines()
    return list_of_todos


def write_todos(todos_arg, filepath=FILEPATH):
    """
        Write a list of to-dos into a text file.
    """
    with open(filepath, 'w') as file:
        file.writelines(todos_arg)


if __name__ == "__main__":
    print("modules.py is being executed directly!")
