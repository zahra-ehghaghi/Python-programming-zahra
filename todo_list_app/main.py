user_prompt = "Type add, show, edit, complete, exit:"

while True :
    user_action = input(user_prompt)
    if 'add' in user_action:
        with open("todos.txt", 'r') as file:
            todos = file.readlines()
        todo = user_action[4:] + "\n"
        todos.append(todo)
        with open("todos.txt", 'w') as file:
            file.writelines(todos)
    elif 'show' in user_action:
        with open("todos.txt", 'r') as file:
            todos = file.readlines()
        for index, item in enumerate(todos):
            print(f"{index+1}-{item[:len(item)-1:]}")
    elif 'edit' in user_action:
        todo_edit_number = int(user_action[5:])-1
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
    elif 'complete' in user_action:
        todo_delete_number = int(user_action[9:]) - 1
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
    elif 'exit' in user_action:
        break
    else:
         print("Hey, you entered  an unknown command")
print("Bye!!!")



