import modules.functions as f
import FreeSimpleGUI as Gui

# layout elements
label = Gui.Text("Type in a To-Do:")
input_box = Gui.InputText(tooltip="Enter todo")
add_button = Gui.Button("Add")

# layout: is a sequence of rows, columns, and elements
window = Gui.Window("My TO-DO App", layout=[[label], [input_box, add_button]])
window.read()  # display the window
window.close()  # close the window
