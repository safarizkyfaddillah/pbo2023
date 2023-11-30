import tkinter as tk
from tkinter import Entry,Button,END, filedialog, Text,LEFT,RIGHT, X

def openFile():
    tf = filedialog.askopenfilename(
    initialdir="C:/Users/MainFrame/Desktop/",
    title="Open Text file",
    filetypes=(("Text Files", "*.txt"),)
    )
    pathh.insert(END, tf)
    tf open(tf) # or tf = open(tf, 'r') =
    data = tf.read()
    txtarea.insert(END, data)
    tf.close()

WS = tk.Tk()
ws.title("PythonGuides")
ws.geometry("400x450")
ws['bg']='#fb0'
Extarea = Text (ws, width=40, height=20)
txtarea.pack(pady=20)

pathh = Entry(ws)
pathh.pack(side=LEFT, expand=True, fill=X, padx=20)

Button(
    WS,
    text="Open File",
    command=openFile
    ).pack(side=RIGHT, expand=True, fill=X, padx=20)

ws.mainloop()