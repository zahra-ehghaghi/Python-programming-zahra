from modules import  functions
import PySimpleGUI as sg
import time



sg.theme("DarkPurple4")
label = sg.Text("Type in a to-do")
clock = sg.Text('',key="clock")
input_box= sg.InputText(tooltip="Enter todo", key="todo")
add_button = sg.Button("Add",size=10)
todo_listbox = sg.Listbox(values=functions.get_togos(), size=[45,10],enable_events=True,key="todos")
edit_button = sg.Button("Edit")
complete_button = sg.Button("Complete")
exit_button = sg.Button("Exit")
window = sg.Window("My To-Do App",
                   layout=[ [clock],
                            [label],
                           [input_box,add_button],
                           [todo_listbox,edit_button,complete_button],
                           [exit_button]],
                   font=("Helvetica",15))

while True:
    events, values =window.read(timeout=1000)
    window['clock'].update(value=time.strftime("%b %m %Y %H:%M:%S"))
    match events:
        case "Add":
            todos = functions.get_togos()
            new_todo = values['todo']+"\n"
            todos.append(new_todo)
            functions.write_todos(todos)
            window['todos'].update(values=todos)
        case "Edit":
            try:
                old_tod=values['todos'][0]
                new_todo = values['todo']+"\n"
                todos = functions.get_togos()
                index = todos.index(old_tod)
                todos[index] = new_todo
                functions.write_todos(todos)
                window['todos'].update(values=todos)
            except IndexError:
                sg.popup("Please select an item first",font=("Helvetica",15))
        case "Complete":
            try:
                to_remove_tod = values['todos'][0]
                todos = functions.get_togos()
                todos.remove(to_remove_tod)
                functions.write_todos(todos)
                window['todos'].update(values=todos)
                window['todo'].update('')
            except IndexError:
               sg.popup("Please select an item first", font=("Helvetica", 15))

        case 'Exit':
            break
        case 'todos':
            window['todo'].update(value=values['todos'][0][:len(values['todos'][0])-1])
        case sg.WIN_CLOSED:
            break

window.close()