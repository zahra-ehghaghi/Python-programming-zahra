user_prompt = "Type add, show, edit, complete, exit:"

while True :
    user_action = input(user_prompt).strip()
    if user_action.startswith("add"):
        with open("todos.txt", 'r') as file:
            todos = file.readlines()
        todo = user_action[4:] + "\n"
        todos.append(todo)
        with open("todos.txt", 'w') as file:
            file.writelines(todos)
    elif user_action.startswith("show"):
        with open("todos.txt", 'r') as file:
            todos = file.readlines()
        for index, item in enumerate(todos):
            print(f"{index+1}-{item[:len(item)-1:]}")
    elif user_action.startswith("edit"):
        try:
            todo_edit_number = int(user_action[5:])-1
            with open("todos.txt", 'r') as file:
                todos = file.readlines()
            todo_to_edit = todos[todo_edit_number].strip("\n")
            todo_edit = input("Enter value of todo for edit: ") +"\n"
            todos[todo_edit_number] = todo_edit
            with open("todos.txt", 'w') as file:
                file.writelines(todos)
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
            with open("todos.txt", 'r') as file:
                todos = file.readlines()
            todo_to_remove= todos[todo_delete_number].strip("\n")
            todos.pop(todo_delete_number)
            with open("todos.txt", 'w') as file:
                file.writelines(todos)
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



