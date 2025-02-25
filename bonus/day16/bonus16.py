import FreeSimpleGUI as Gui

Gui.theme("DarkAmber")

label1 = Gui.Text("Select files to compress:")
input1 = Gui.Input()
choose_button1 = Gui.FilesBrowse("Choose Files", key="files")  # file_types=(("Text files", "*.txt")

label2 = Gui.Text("Select destination folder:")
input2 = Gui.Input()
choose_button2 = Gui.FolderBrowse("Choose Folder", key="folder")

compress_button = Gui.Button("Compress Files")

window = Gui.Window("File Compressor", layout=[
    [label1, input1, choose_button1],
    [label2, input2, choose_button2],
    [compress_button]
])

window.read()
window.close()
