import os
from tkinter import Tk, Label, Button, Entry, Text, END

def execute_command():
    command_to_execute = os.popen(entry.get()).read()
    txt.delete('1.0','end')
    txt.insert(END, command_to_execute)

window = Tk()
window.title('Run CMD')
window.geometry("600x400")
window.iconbitmap('app.ico')
window.resizable(False, False)

lbl = Label(window, text="Command:")
entry = Entry(window, width=40)
btn = Button(window, text="Execute", command=execute_command)
txt = Text(window , bg='grey')

lbl.place(x=1,y=5)
entry.place(x=70,y=5)
btn.place(x=320,y=2)
txt.place(y=50)

window.mainloop()