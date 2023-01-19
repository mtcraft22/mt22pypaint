from tkinter import *
from tkinter import colorchooser, messagebox

root = Tk()

material = "lapis"
col = "black"

hancho = Scale(from_=0, to=100, orient=HORIZONTAL)
hancho.grid(row=2, column=10, columnspan=8)
dis_linias = Scale(root, from_=1, to=30, orient=HORIZONTAL)
dis_linias.grid(row=6, column=10, columnspan=8)
lienzo = Canvas(root, width=600, height=400, bg="white")
lienzo.grid(padx=20, pady=20, row=1, columnspan=10, column=0, rowspan=10)
bor = Button(root, text="borrador", command=lambda: set_material("goma"))
bor.grid(row=1, column=10, columnspan=4)
las = Button(root, text="lapis", command=lambda: set_material("lapis"))
las.grid(row=1, column=14, columnspan=2)
lin = Button(root, text="linea", command=lambda: set_material("linea"))
lin.grid(row=1, column=16, columnspan=2)
rect = Button(root, text="rectangulo", command=lambda: set_material("rect"))
rect.grid(row=1, column=18, columnspan=4)
boton_eliminacion = Button(root, text="bora todo", command=lambda: des())
boton_eliminacion.grid(row=1, column=22, columnspan=4)
boton_FF6A00 = Button(root, bg="#70FF00", command=lambda: set_color("#FF6A00"), height=1, width=1)
boton_FF6A00.grid(row=3, column=10)
boton_black = Button(root, bg="black", command=lambda: set_color("black"), height=1, width=1)
boton_black.grid(row=3, column=11)
boton_F0F0F0 = Button(root, bg="#F0F0F0", command=lambda: set_color("#F0F0F0"), height=1, width=1)
boton_F0F0F0.grid(row=3, column=12)
boton_color = Button(root, bg="#F0F0F0", command=lambda: asck_color(), height=1, width=1)
boton_color.grid(row=4, column=12)


def asck_color():
    c2 = colorchooser.askcolor()[1]
    print(c2)
    set_color(c2)
    boton_color.config(bg=c2)


def set_color(c):
    print(c)
    global col
    col = c
    boton_color.config(bg=c)


cord = []


def des():
    avd = messagebox.askquestion("Adventecia", "Si elimina eliminara el buffer ctr-y/z continuar?")
    if avd == "yes":
        lineas_ancho.clear()
        rectangulos_width.clear()
        eliminados.clear()
        lienzo.delete("all")
    else:
        return


def set_material(m):
    global material
    material = m
    if material == "lapis":
        # lienzo.bind('<Button-1>', motion2)
        lienzo.bind('<B1-Motion>', motion2)
        las.config(bg="red")
        bor.config(bg="#F0F0F0")
        lin.config(bg="#F0F0F0")
        rect.config(bg="#F0F0F0")
    elif material == "goma":
        # lienzo.bind('<Button-1>', motion)
        lienzo.bind('<B1-Motion>', motion)
        bor.config(bg="red")
        las.config(bg="#F0F0F0")
        lin.config(bg="#F0F0F0")
        rect.config(bg="#F0F0F0")
    elif material == "linea":
        lienzo.bind('<Button-1>', linea)
        lienzo.bind('<B1-Motion>', clear)
        bor.config(bg="#F0F0F0")
        las.config(bg="#F0F0F0")
        lin.config(bg="red")
        rect.config(bg="#F0F0F0")
    elif material == "rect":
        lienzo.bind('<Button-1>', recta)
        lienzo.bind('<B1-Motion>', clear)
        bor.config(bg="#F0F0F0")
        las.config(bg="#F0F0F0")
        lin.config(bg="#F0F0F0")
        rect.config(bg="red")


def clear(event):
    cord.clear()


def motion2(event):
    cord.clear()
    x, y = event.x, event.y
    lienzo.create_rectangle(x - hancho.get(), y + hancho.get(), x + hancho.get(), y - hancho.get(), fill=col,
                            outline=col, tags=(col, "lapis"))


def motion(event):
    cord.clear()
    x, y = event.x, event.y
    lienzo.create_rectangle(x - hancho.get(), y + hancho.get(), x + hancho.get(), y - hancho.get(), fill="white",
                            outline="white", tags=(col, "goma"))


lineas_ancho = {}


def linea(event):
    x, y = event.x, event.y
    cord.append(x)
    cord.append(y)
    if len(cord) == 4 or len(cord) > 4:
        b = lienzo.create_line(cord[0], cord[1], cord[2], cord[3], fill=col, tags=(col, "linea"),
                               width=hancho.get() * 2, )
        lineas_ancho[lienzo.getint(b)] = hancho.get() * 2
        cord.clear()


rectangulos_width = {}


def recta(event):
    x, y = event.x, event.y
    cord.append(x)
    cord.append(y)
    if len(cord) == 4 or len(cord) > 4:
        a = lienzo.create_rectangle(cord[0], cord[1], cord[2], cord[3], outline=col, width=hancho.get() * 2,
                                    tags=(col, "rect"))
        cord.clear()
        rectangulos_width[lienzo.getint(a)] = hancho.get() * 2


def spray(event):
    x, y = event.x, event.y
    dis = (hancho.get() * 2) + dis_linias.get()
    lienzo.create_rectangle(x - hancho.get(), y + hancho.get(), x + hancho.get(), y - hancho.get(), fill=col,
                            outline=col, tags=col)
    lienzo.create_rectangle(x - hancho.get() + dis, y + hancho.get() - dis, x + hancho.get() + dis,
                            y - hancho.get() - dis, fill=col, outline=col, tags=col)


def getcolor(event):
    for item_id in lienzo.find_all():
        tag = lienzo.gettags(item_id)[0]
        lienzo.tag_bind(tag, '<Button-2>', lambda _, i=tag: set_color(i))


eliminados = []


def detraas(event):
    try:
        if lienzo.gettags(lienzo.find_all()[-1])[1] == "lapis":
            for i in range(10):
                lienzo.delete(lienzo.find_all()[-1])
                eliminados.append((lienzo.gettags(lienzo.find_all()[-1])[1], lienzo.coords(lienzo.find_all()[-1]),
                                   lienzo.gettags(lienzo.find_all()[-1])[0], lienzo.find_all()[-1]))
        else:
            lienzo.delete(lienzo.find_all()[-1])
            eliminados.append((lienzo.gettags(lienzo.find_all()[-1])[1], lienzo.coords(lienzo.find_all()[-1]),
                               lienzo.gettags(lienzo.find_all()[-1])[0], lienzo.find_all()[-1]))
    except IndexError:  # no more items to delete then return
        messagebox.showinfo("Info", f"No es posible eliminar sin elementos, elementos eliminados")
        return


def alante(event):
    try:
        if lienzo.gettags(lienzo.find_all()[-1])[0] == "lapis":
            contador = 0

            materia = eliminados[-1][0]
            while materia == "lapis" and contador < 10:
                lienzo.create_rectangle(eliminados[-1][1], fill=eliminados[-1][2], outline=eliminados[-1][2],
                                        tags=(eliminados[-1][2], materia))
                eliminados.pop(-1)
                contador += 1
                print(materia)
        else:
            materia = eliminados[-1][0]
            if materia == "rect":
                lienzo.create_rectangle(eliminados[-1][1], outline=eliminados[-1][2],
                                        width=str(rectangulos_width[eliminados[-1][3]]),
                                        tags=(eliminados[-1][2], materia))

                print(materia)
                print(materia, " ", rectangulos_width, " ", rectangulos_width[eliminados[-1][3]])
                eliminados.pop(-1)
            elif materia == "linea":
                lienzo.create_line(eliminados[-1][1], fill=eliminados[-1][2], tags=(eliminados[-1][2], materia),
                                   width=str(lineas_ancho[eliminados[-1][3]]))
                print(materia, " ", lineas_ancho, " ", lineas_ancho[eliminados[-1][3]])
                eliminados.pop(-1)
            print(materia)
    except IndexError:
        messagebox.showinfo("Info", f"No es posible reustarar sin elementos, elementos eliminados")
        return


lienzo.bind('<Button-2>', getcolor)
lienzo.bind("<B3-Motion>", spray)
root.bind("<Control-z>", detraas)
root.bind("<Control-y>", alante)
root.mainloop()
