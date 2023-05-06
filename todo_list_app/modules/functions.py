FILEPATH = "todos.txt"

def get_togos(filepath=FILEPATH):
    """ Read a test file and return the list of  to-d items """
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write_todos(todos_arg, filepath=FILEPATH):
    """ write the to-do list of items in the text file"""
    with open(filepath, 'w') as file:
        file.writelines(todos_arg)
