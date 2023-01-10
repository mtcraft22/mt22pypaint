import tkinter
import customtkinter


customtkinter.set_appearance_mode("Dark")
customtkinter.set_default_color_theme("test")


class Paint(customtkinter.CTk):
    WIDTH = 1000
    HEIGHT = 900

    def __init__(self):
        super().__init__()
        # make canvas and canvasframe
        self.title("PyPaint")
        self.geometry(f"{Paint.WIDTH}x{Paint.HEIGHT}")
        self.protocol("WM_DELETE_WINDOW", self.on_closing)
        self.cavasframe = customtkinter.CTkFrame(master=self, corner_radius=10, width=1000, height=900)
        self.cavasframe.grid(row=1, column=0, pady=20, padx=20, rowspan=3)
        self.lienzo = tkinter.Canvas(self.cavasframe, width=900, height=800, bg="#ffffff", border=-50)
        self.lienzo.grid(padx=20, pady=20)
        # load button picture

        # make buton palete frame
        self.buttonframe_top = customtkinter.CTkFrame(master=self, corner_radius=10, width=400, height=200)
        self.buttonframe_top.grid(row=1, column=1, pady=20, padx=20, sticky="s")
        self.buttonframe_midle = customtkinter.CTkFrame(master=self, corner_radius=10, width=400, height=200)
        self.buttonframe_midle.grid(row=2, column=1, pady=20, padx=20)
        self.buttonframe_bottom = customtkinter.CTkFrame(master=self, corner_radius=10, width=400, height=200)
        self.buttonframe_bottom.grid(row=3, column=1, pady=20, padx=20, sticky="n")
        # make palete_buton labels
        Heramientas = customtkinter.CTkLabel(master=self.buttonframe_top, text="Heramientas")
        Heramientas.grid(row=0, column=0)
        Colores = customtkinter.CTkLabel(master=self.buttonframe_midle, text="Paleta", width=45)
        Colores.grid(row=0, column=0, columnspan=3, padx=1)
        # make palete butons

        # first row
        ffffff = customtkinter.CTkButton(bg_color="#ffffff", fg_color="#ffffff", hover_color="#ffffff", text="",
                                         master=self.buttonframe_midle, width=30, corner_radius=10,
                                         command=lambda: self.set_selbut(ffffff))
        ffffff.grid(row=1, column=0, padx=5, pady=5)
        ffff99 = customtkinter.CTkButton(bg_color="#ffff99", fg_color="#ffff99", hover_color="#ffff99", text="",
                                         master=self.buttonframe_midle, width=30, corner_radius=10,
                                         command=lambda: self.set_selbut(ffff99))
        ffff99.grid(row=1, column=1, padx=5, pady=5)
        ffff33 = customtkinter.CTkButton(bg_color="#ffff33", fg_color="#ffff33", hover_color="#ffff33", text="",
                                         master=self.buttonframe_midle, width=30, corner_radius=10,
                                         command=lambda: self.set_selbut(ffff33))
        ffff33.grid(row=1, column=2, padx=5, pady=5)
        ffff00 = customtkinter.CTkButton(bg_color="#ffff00", fg_color="#ffff00", hover_color="#ffff00", text="",
                                         master=self.buttonframe_midle, width=30, corner_radius=10,
                                         command=lambda: self.set_selbut(ffff00))
        ffff00.grid(row=1, column=3, padx=5, pady=5)
        ffee33 = customtkinter.CTkButton(bg_color="#ffee33", fg_color="#ffee33", hover_color="#ffee33", text="",
                                         master=self.buttonframe_midle, width=30, corner_radius=10,
                                         command=lambda: self.set_selbut(ffee33))
        ffee33.grid(row=1, column=4, padx=5, pady=5)
        ffdd33 = customtkinter.CTkButton(bg_color="#ffdd33", fg_color="#ffdd33", hover_color="#ffdd33", text="",
                                         master=self.buttonframe_midle, width=30, corner_radius=10,
                                         command=lambda: self.set_selbut(ffdd33))
        ffdd33.grid(row=1, column=5, padx=5, pady=5)
        ffcc00 = customtkinter.CTkButton(bg_color="#ffcc00", fg_color="#ffcc00", hover_color="#ffcc00", text="",
                                         master=self.buttonframe_midle, width=30, corner_radius=10,
                                         command=lambda: self.set_selbut(ffcc00))
        ffcc00.grid(row=1, column=6, padx=5, pady=5)

        # second row

        # third row
        self.cccc00 = customtkinter.CTkButton(bg_color="#cccc00", fg_color="#cccc00", hover_color="#cccc00", text="",
                                              master=self.buttonframe_midle, width=30, corner_radius=10,
                                              command=lambda: self.set_selbut(self.cccc00))
        self.cccc00.grid(row=3, column=3, padx=5, pady=5)
        # list of color butons
        self.colorbuttons = [ffffff, ffff99, ffff00, ffcc00, ffff33, ffdd33, ffee33, self.cccc00]
        # make buttons
        borador = customtkinter.CTkButton(text="Goma", master=self.buttonframe_top)
        borador.grid(row=1, column=0, padx=5, pady=5)
        lapis = customtkinter.CTkButton(text="Goma", master=self.buttonframe_top)
        lapis.grid(row=1, column=1, padx=5, pady=5)
        linea = customtkinter.CTkButton(text="Goma", master=self.buttonframe_top)
        linea.grid(row=2, column=0, padx=5, pady=5)
        rect = customtkinter.CTkButton(text="Goma", master=self.buttonframe_top)
        rect.grid(row=2, column=1, padx=5, pady=5)
        b_to = customtkinter.CTkButton(text="Goma", master=self.buttonframe_top)
        b_to.grid(row=3, column=0, padx=5, pady=5)
        # make slide bars and slide bars labels
        grueso_label = customtkinter.CTkLabel(self.buttonframe_bottom, text="Grueso de linia: ")
        grueso_label.grid(row=1, column=0, padx=5, pady=5)
        grueso_slider = customtkinter.CTkSlider(self.buttonframe_bottom, from_=0, to=100, orient=tkinter.HORIZONTAL)
        grueso_slider.set(0)
        grueso_slider.grid(row=2, column=0, padx=5, pady=5)
        separacion_label = customtkinter.CTkLabel(self.buttonframe_bottom, text="Separación de linia: ")
        separacion_label.grid(row=3, column=0, padx=35, pady=5)
        separacion_slider = customtkinter.CTkSlider(self.buttonframe_bottom, from_=0, to=100, orient=tkinter.HORIZONTAL)
        separacion_slider.set(0)
        separacion_slider.grid(row=4, column=0, padx=35, pady=5)

    def set_selbut(self, but):
        for i in self.colorbuttons:
            if i == but:
                print(i.bg_color)
                i.config(borderwidth=2, bg="black")
            else:
                i.config(borderwidth=0, bg="black")

    def on_closing(self, event=0):
        self.destroy()


paint = Paint()
paint.title("Pypaint")
paint.mainloop()
