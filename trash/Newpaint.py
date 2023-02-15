import tkinter, random
from tkinter import ttk


class Newpaint:
    def __init__(self):
        # root definition
        self.root = tkinter.Tk()
        # widget vars
        self.idlistvar = tkinter.StringVar()
        # gui widgets definition
        self.canvas = tkinter.Canvas(width=800, height=600, bg="white")
        self.rectcreation = tkinter.Button(text="Rectangulo", command=lambda: self.set_matterial("rect"))
        self.circlecreation = tkinter.Button(text="Circulo", command=lambda: self.set_matterial("circ"))
        self.trianglecre = tkinter.Button(text="triangle", command=lambda: self.set_matterial("triangle"))
        self.trianglecre2 = tkinter.Button(text="triangle", command=lambda: self.set_matterial("triangle2"))
        self.idlist = tkinter.Listbox(listvariable=self.idlistvar)
        # show and config the widgets
        self.__show()
        # binding mouse events to canvas actions
        self.canvas.bind("<1>", self.origin)  # store the pos of the mouse when has right-clicket
        self.canvas.bind("<ButtonRelease-1>", self.destination)  # remove a intem tags to make this fixed
        self.canvas.bind("<B1-Motion>", self.draw_rect)  # draw rect while right-mousee button is presed
        self.canvas.bind("<B3-Motion>", self.move)
        # pen properties
        self.material = "lapis"
        # mouse buffer
        self.cords = []

    def set_matterial(self, m):
        self.material = m

    def __show(self):
        self.canvas.grid(row=1, column=0, pady=20, padx=20, rowspan=10)
        self.rectcreation.grid(row=1, column=1)
        self.circlecreation.grid(row=1, column=2)
        self.trianglecre.grid(row=2, column=1)
        self.trianglecre2.grid(row=2, column=2)
        self.idlist.grid(row=3, column=2)

    def draw_rect(self, event):
        self.canvas.delete("rectprod")
        match self.material:

            case "circ":
                circle = self.canvas.create_oval(self.cords[0][0], self.cords[0][1], event.x, event.y, width=10,
                                                 tags=("rectprod",f"Circulo: w:{abs(self.cords[0][0]-event.x)} h: {abs(self.cords[0][1]-event.y)}"), fill="red")

            case "rect":
                re = self.canvas.create_rectangle(self.cords[0][0], self.cords[0][1], event.x, event.y, width=10,
                                                  tags=("rectprod",f"Rect: w:{abs(self.cords[0][0]-event.x)} h: {abs(self.cords[0][1]-event.y)}"), outline="red")

            case "triangle":
                prex = self.cords[0][0]
                prey = self.cords[0][1]
                pol = self.canvas.create_polygon(prex, event.y, event.x, prey, event.x, event.y, tags=("rectprod",f"T_Rect: w:{abs(self.cords[0][0]-event.x)} h: {abs(self.cords[0][1]-event.y)}"),
                                                 outline="red", fill=random.choice(("red", "brown", "blue", "orange")),
                                                 width=5)

            case "triangle2":
                prex = self.cords[0][0]
                prey = self.cords[0][1]

                tri = self.canvas.create_polygon(prex, event.y, event.x, event.y, prex - ((prex - event.x) / 2), prey,
                                                 tags=("rectprod",f"T_Equi: w:{abs(self.cords[0][0]-event.x)} h: {abs(self.cords[0][1]-event.y)}"), outline="red",
                                                 fill=random.choice(("red", "brown", "blue", "orange")), width=5)


            case _:
                pass

    def origin(self, event):
        self.cords.clear()
        self.cords.append((event.x, event.y))

    def destination(self, event):
        a = self.canvas.find_withtag("rectprod")
        self.canvas.dtag(a, "rectprod")
        try:
            if not(a[0]==None):
                self.idlist.insert(tkinter.END, self.canvas.gettags(a)[0])
        except IndexError:
            return
    def move(self,event=0):
        print(self.idlist.get("active"))
        b=self.canvas.find_withtag(self.idlist.get("active"))
        print(b)
        self.canvas.moveto(int(b[0]),event.x,event.y)
        
newpaint = Newpaint()
newpaint.root.mainloop()
