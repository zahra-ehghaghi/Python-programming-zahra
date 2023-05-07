import PySimpleGUI as sg
from zip_extractor import extract_archive

sg.theme("Black")

archive_lable = sg.Text("Select Archive: ")
archive_text = sg.InputText(key="archiveFile")
archive_button = sg.FileBrowse("Choose")

dest_lable = sg.Text("Select Destination: ")
dest_text = sg.InputText(key="dest_dir")
dest_button= sg.FolderBrowse("Choose")

unzip_button = sg.Button("Extract",key="Extract")
exit_button = sg.Button("Exit", key="Exit")
message_label = sg.Text(key="message_label",text_color="red")

window = sg.Window("Archive Extractor",layout=[[archive_lable,archive_text,archive_button],
                                               [dest_lable,dest_text,dest_button],
                                               [unzip_button,exit_button,message_label]])
while True:
    event, values = window.read()
    match event:
        case "Extract":
            try:
                archiveFile = values['archiveFile']
                dest_dir= values['dest_dir']
                extract_archive(archiveFile,dest_dir)
                message = "File Extracted Successfully"
            except :
                message = "Error!!! Choose Valid data"
            window['message_label'].update(value=message)

        case "Exit":
            break
        case sg.WIN_CLOSED:
            break
window.close()

