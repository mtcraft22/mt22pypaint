import tkinter
from tkinter import ttk


root= tkinter.Tk()

tab=ttk.Notebook(root)
tab.pack(pady=15)
marco1=tkinter.Frame(tab,width=200,height=200)
marco2=tkinter.Frame(tab,width=200,height=200)
marco1.pack(expand=1,fill="both")
marco2.pack(expand=1,fill="both")
tab.add(marco1,text="saludar")
tab.add(marco2,text="despedir")

saludar = tkinter.Button(marco1,text="saludat",command=lambda:print("hey"))
despedir = tkinter.Button(marco2,text="despedir",command=lambda:print("dios"))
saludar.pack()
despedir.pack()
root.mainloop()

