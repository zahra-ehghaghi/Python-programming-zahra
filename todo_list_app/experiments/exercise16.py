import PySimpleGUI as sg


label_feet = sg.Text("Enter feet: ")
text_feet = sg.InputText(tooltip="Enter feet")


label_inch = sg.Text("Enter inches: ")
text_inch = sg.Input(tooltip="Enter inches ")

button_compress = sg.Button("Convert")
window = sg.Window("Convertor",layout=[[label_feet,text_feet]
                                        ,[label_inch,text_inch],
                                         [button_compress]])
window.read()
window.close()
