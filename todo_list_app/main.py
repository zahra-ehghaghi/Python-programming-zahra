user_prompt = "Type add, show, edit, complete, exit:"


while True :
    user_action = input(user_prompt)
    match user_action.strip():
        case 'add':
            with open("todos.txt", 'r') as file:
                todos = file.readlines()
            todo = input("Enter a todo: ")+ "\n"
            todos.append(todo)
            with open("todos.txt", 'w') as file:
                file.writelines(todos)
        case 'show':
            with open("todos.txt", 'r') as file:
                todos = file.readlines()
            for index, item in enumerate(todos):
                print(f"{index+1}-{item[:len(item)-1:]}")
        case 'edit':
            todo_edit_number = int(input("Enter number of todo for edit: "))-1
            with open("todos.txt", 'r') as file:
                todos = file.readlines()

            if todo_edit_number >= todos.__len__() or todo_edit_number < 0:
                print("Hey, you entered  a rong number")
                continue
            todo_to_edit = todos[todo_edit_number].strip("\n")
            todo_edit = input("Enter value of todo for edit: ") +"\n"
            todos[todo_edit_number] = todo_edit
            with open("todos.txt", 'w') as file:
                file.writelines(todos)
            print(f"item is modified from {todo_to_edit}  to {todo_edit}")
        case 'complete':
            todo_delete_number = int(input("Enter number of todo for edit: ")) - 1
            with open("todos.txt", 'r') as file:
                todos = file.readlines()
            if todo_delete_number >= todos.__len__() or todo_delete_number < 0:
                print("Hey, you entered  a rong number")
                continue
            todo_to_remove= todos[todo_delete_number].strip("\n")
            todos.pop(todo_delete_number)
            with open("todos.txt", 'w') as file:
                file.writelines(todos)
            print(f"todo {todo_to_remove} is deleted")
        case 'exit':
            break
        case _:
            print("Hey, you entered  an unknown command")
print("Bye!!!")



