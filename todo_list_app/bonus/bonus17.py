import PySimpleGUI as sg
from zip_creator import make_archive


label_source = sg.Text("Select files to compress: ")
text_source = sg.Input(tooltip="Source" )
button_source = sg.FilesBrowse("Choose",key="files")

label_dest = sg.Text("Select destination folder: ")
text_dest = sg.Input(tooltip="Destination",key="folder")
button_dest = sg.FolderBrowse("Choose")
button_compress = sg.Button("Compress")
label_msg = sg.Text("")
window = sg.Window("File Zipper",layout=[[label_source,text_source,button_source]
                                        ,[label_dest,text_dest,button_dest],
                                         [button_compress,label_msg]])

while True:

  event,values =  window.read()
  match event:
      case "Compress":
          if values["files"] == '':
              message = "Please select valid files"
          elif   values["folder"] == '':
              message = "Please select valid destination"
          else:
              filepaths = values["files"].split(";")
              dest_dir =  values["folder"]
              try:
                make_archive(filepaths,dest_dir)
                message = "Files Compresses successfully"
              except FileNotFoundError:
                  message ="Value must be valid"
          label_msg.update(value=message)
      case sg.WIN_CLOSED:
          break
window.close()
