import PySimpleGUI as sg

def convertor(feet,inches):
    return feet * 0.3048 + inches * 0.0254


label_feet = sg.Text("Enter feet: ")
text_feet = sg.InputText(tooltip="Enter feet",key="feet")


label_inch = sg.Text("Enter inches: ")
text_inch = sg.Input(tooltip="Enter inches ",key="inches")

button_compress = sg.Button("Convert")
label_meter = sg.Text("",key="meters",text_color="red" , font=('Arial',12))
window = sg.Window("Convertor",layout=[[label_feet,text_feet]
                                        ,[label_inch,text_inch],
                                         [button_compress,label_meter]])
while True:
    event,values = window.read()
    print(event)
    print(values)
    match event:
     case "Convert":
         try:
            feet = float(values['feet'])
            inches = float(values['inches'])
            meters = convertor(feet,inches)
            messge = f"The value of meters is: {meters}"
         except ValueError:
             messge = "Enter valid number for feet and inches"
         window['meters'].update(value=messge)
     case sg.WIN_CLOSED:
         break




window.close()
