from modules import  functions
import  PySimpleGUI as sg


label = sg.Text("Type in a to-do")
input_box= sg.InputText(tooltip="Enter todo")
button = sg.Button("Add")
window = sg.Window("My To-Do App",layout=[[label],[input_box,button]])

window.read()
window.close()