from modules import  functions
import  PySimpleGUI as sg


label = sg.Text("Type in a to-do")
input_box= sg.InputText(tooltip="Enter todo", key="todo")
add_button = sg.Button("Add")
todo_listbox = sg.Listbox(values=functions.get_togos(), size=[45,10],enable_events=True,key="todos")
edit_button = sg.Button("Edit")
window = sg.Window("My To-Do App",
                   layout=[[label],[input_box,add_button],[todo_listbox,edit_button]],
                   font=("Helvetica",15))

while True:
    events, values =window.read()
    print (events)
    print (values)
    match events:
        case "Add":
            todos = functions.get_togos()
            new_todo = values['todo']+"\n"
            todos.append(new_todo)
            functions.write_todos(todos)
            window['todos'].update(values=todos)
        case "Edit":
            old_tod=values['todos'][0]
            new_todo = values['todo']+"\n"
            todos = functions.get_togos()
            index = todos.index(old_tod)
            todos[index] = new_todo
            window['todos'].update(values=todos)
        case 'todos':
            window['todo'].update(value=values['todos'][0])
        case sg.WIN_CLOSED:
            break

window.close()