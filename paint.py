from tkinter import *
import queue
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
    avd=messagebox.askquestion("Adventecia", "Si elimina eliminara el buffer ctr-y/z continuar?")
    if avd=="yes":
        eliminados = queue.Queue()
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
    
    x, y = event.x, event.y
    lienzo.create_rectangle(x - hancho.get(), y + hancho.get(), x + hancho.get(), y - hancho.get(), fill=col,
                            outline=col, tags=(col, "lapis",0, x - hancho.get(), y + hancho.get(), x + hancho.get(), y - hancho.get()))
    cord.clear()

def motion(event):
    
    x, y = event.x, event.y
    lienzo.create_rectangle(x - hancho.get(), y + hancho.get(), x + hancho.get(), y - hancho.get(), fill="white",
                            outline="white", tags=(col, "goma",0,x - hancho.get(), y + hancho.get(), x + hancho.get(), y - hancho.get(),))
    cord.clear()




def linea(event):
    x, y = event.x, event.y
    cord.append(x)
    cord.append(y)
    if len(cord) == 4 or len(cord) > 4:
        lienzo.create_line(cord[0], cord[1], cord[2], cord[3], fill=col, tags=(col, "linea", hancho.get() * 2,cord[0], cord[1], cord[2], cord[3]),
                            width=hancho.get() * 2)
        cord.clear()





def recta(event):
    x, y = event.x, event.y
    cord.append(x)
    cord.append(y)
    if len(cord) == 4 or len(cord) > 4:
        lienzo.create_rectangle(cord[0], cord[1], cord[2], cord[3], outline=col, width=hancho.get() * 2,
                                tags=(col, "rect", hancho.get() * 2, cord[0], cord[1], cord[2], cord[3] ))
        cord.clear()


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


eliminados = queue.LifoQueue()




def detraas(event):
    try:
        if lienzo.gettags(lienzo.find_all()[-1])[1]=="lapis":
            for i in range(10):   
                eliminados.put(lienzo.gettags(lienzo.find_all()[-1]))
                lienzo.delete(lienzo.find_all()[-1])
        else:
            eliminados.put(lienzo.gettags(lienzo.find_all()[-1]))
            lienzo.delete(lienzo.find_all()[-1])
    except IndexError:  # no more items to delete then return
        messagebox.showinfo("Info", "No es posible eliminar sin elementos")
        return

'''
tags=(col, "linea", hancho.get() * 2, cord)
lienzo.create_rectangle(cord[0], cord[1], cord[2], cord[3], outline=col, width=hancho.get() * 2,tags=(col, "rect", hancho.get() * 2, cord ))'''
def alante(event):
    item = eliminados.get()
    materia= item[1]
    if materia == "lapis":
        for i in range(10):
            print(item)
            lienzo.create_rectangle(item[3],item[4],item[5],item[6],outline=item[0],fill=item[0],width=item[2],tags=item)
            item = eliminados.get()
            materia= item[1]  
            if eliminados.empty():
                messagebox.showinfo("Info","No existen elemntos a reustarar")
                return
    else:
        if materia == "rect":
            if eliminados.empty():
                messagebox.showinfo("Info","No existen elemntos a reustarar")
                return
            lienzo.create_rectangle(item[3],item[4],item[5],item[6],outline=item[0],width=item[2],tags=item)
        elif materia == "linea":
            if eliminados.empty():
                messagebox.showinfo("Info","No existen elemntos a reustarar")
                return
            lienzo.create_line(item[3],item[4],item[5],item[6],fill=item[0],width=item[2],tags=item)
        
                
        


lienzo.bind('<Button-2>', getcolor)
lienzo.bind("<B3-Motion>", spray)
root.bind("<Control-z>", detraas)
root.bind("<Control-y>", alante)

root.mainloop()

