import tkinter
from tkinter import ttk

root = tkinter.Tk()
tab = ttk.Notebook(root)
class Tabs:
    def __init__(self,**kwargs):
        self.name=kwargs["name"]
        self.height=kwargs["height"]
        self.width=kwargs["width"]
        self.notebook=kwargs["notebook"]
        self.frame=tkinter.Frame(self.tabadded, width=200, height=200)
        self.tabadded=kwargs["tabadded"]



tab.pack(pady=15)
marco1 = tkinter.Frame(tab, width=200, height=200)
marco2 = tkinter.Frame(tab, width=200, height=200)
marco1.pack(expand=1, fill="both")
marco2.pack(expand=1, fill="both")
tab.add(marco1, text="saludar")
tab.add(marco2, text="despedir")

saludar = tkinter.Button(marco1, text="saludar", command=lambda: print("hey"))
despedir = tkinter.Button(marco2, text="despedir", command=lambda: print("dios"))
saludar.pack()
despedir.pack()
root.mainloop()
