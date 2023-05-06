import PySimpleGUI as sg


label_source = sg.Text("Select files to compress: ")
text_source = sg.Input(tooltip="Source")
button_source = sg.FilesBrowse("Choose")

label_dest = sg.Text("Select destination folder: ")
text_dest = sg.Input(tooltip="Destination")
button_dest = sg.FolderBrowse("Choose")
button_compress = sg.Button("Compress")
window = sg.Window("File Zipper",layout=[[label_source,text_source,button_source]
                                        ,[label_dest,text_dest,button_dest],
                                         [button_compress]])
window.read()
window.close()
