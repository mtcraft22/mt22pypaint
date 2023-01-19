import tkinter
from tkinter import ttk


class Newpaint:
    def __init__(self):
        # root definition
        self.root = tkinter.Tk()
        # gui widgets definition
        self.canvas = tkinter.Canvas(width=800, height=600, bg="white")
        self.rectcreation = tkinter.Button(text="Rectangulo", command=lambda: self.set_matterial("rect"))
        self.circlecreation = tkinter.Button(text="Circulo", command=lambda: self.set_matterial("circ"))
        # show and config the widgets
        self.__show()
        #binding mouse events to canvas actions
        self.canvas.bind("<1>", self.origin)  # store the pos of the mouse when has right-clicket
        self.canvas.bind("<ButtonRelease-1>", self.destination)  # remove a intem tags to make this fixed
        self.canvas.bind("<B1-Motion>", self.draw_rect)  # draw rect while right-mousee button is presed
        # pen properties
        self.material = "lapis"
        # mouse buffer
        self.cords = []

    def set_matterial(self, m):
        self.material = m

    def __show(self):
        self.canvas.grid(row=1, column=0, pady=20, padx=20)
        self.rectcreation.grid(row=1, column=1)
        self.circlecreation.grid(row=1, column=2)

    def draw_rect(self, event):
        self.canvas.delete("rectprod")
        match self.material:
            case "circ":
                self.canvas.create_arc(self.cords[0][0], self.cords[0][1], event.x, event.y, width=10,
                                        tags="rectprod", fill="red")
            case "rect":
                self.canvas.create_rectangle(self.cords[0][0], self.cords[0][1], event.x, event.y, width=10,
                                             tags="rectprod", outline="red")
            case _:
                pass

    def origin(self, event):
        self.cords.clear()
        self.cords.append((event.x, event.y))

    def destination(self, event):
        a = self.canvas.find_withtag("rectprod")
        self.canvas.dtag(a, "rectprod")


newpaint = Newpaint()
newpaint.root.mainloop()
