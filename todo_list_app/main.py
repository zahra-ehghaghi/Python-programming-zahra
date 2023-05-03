def get_togos(filepath="todos.txt"):
    """ Read a test file and return the list of  to-d items """
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write_todos(todos_arg, filepath="todos.txt"):
    """ write the to-do list of items in the text file"""
    with open(filepath, 'w') as file:
        file.writelines(todos_arg)


while True:
    user_prompt = "Type add, show, edit, complete, exit:"
    user_action = input(user_prompt).strip()
    if user_action.startswith("add"):
        todos = get_togos()
        todo = user_action[4:] + "\n"
        todos.append(todo)
        write_todos(todos)
    elif user_action.startswith("show"):
        todos = get_togos()
        for index, item in enumerate(todos):
            print(f"{index + 1}-{item[:len(item) - 1:]}")
    elif user_action.startswith("edit"):
        try:
            todo_edit_number = int(user_action[5:]) - 1
            todos = get_togos()
            todo_to_edit = todos[todo_edit_number].strip("\n")
            todo_edit = input("Enter value of todo for edit: ") + "\n"
            todos[todo_edit_number] = todo_edit
            write_todos(todos)
            print(f"item is modified from {todo_to_edit}  to {todo_edit}")
        except ValueError:
            print("Your command is not valid")
            continue
        except IndexError:
            print("There is no item  with that number. ")
            continue
    elif user_action.startswith("complete"):
        try:
            todo_delete_number = int(user_action[9:]) - 1
            todos = get_togos()
            todo_to_remove = todos[todo_delete_number].strip("\n")
            todos.pop(todo_delete_number)
            write_todos(todos)
            print(f"todo {todo_to_remove} is deleted")
        except ValueError:
            print("Your command is not valid")
            continue
        except IndexError:
            print("There is no item  with that number. ")
            continue
    elif user_action.startswith("exit"):
        break
    else:
        print("Hey, you entered  an unknown command")
print("Bye!!!")
