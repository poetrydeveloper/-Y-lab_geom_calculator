from tkinter import *
from tkinter import ttk
from tkinter.ttk import Combobox
from calc.calculator import Calculator
from PIL import Image, ImageTk


class Window:
    def __init__(self, width=600, height=500, title="Калькулятор", resizable=(False, False), icon="resources/icon.ico"):
        self.image = None
        self.answer = None
        self.entries = None
        self.calc = None
        self.root = Tk()
        self.root.title(title)
        self.root.geometry(f"{width}x{height}+200+200")
        self.root.resizable(resizable[0], resizable[1])
        if icon:
            self.root.iconbitmap(icon)

        self.root['background'] = '#856ff8'
        self.figures = Combobox(self.root, width=15, height=1, values=('square', "circle", "triangle",))

    def run(self):
        self.draw_widgets()
        self.root.mainloop()

    def draw_widgets(self):
        Label(self.root, width=15, height=1, text="Choose a geometry:").place(relx=0.1, rely=0.05)
        self.figures.current(0)
        self.figures.place(relx=0.1, rely=0.1)
        Button(self.root, width=15, height=1, text="Enter", command=self.get_figure).place(relx=0.1, rely=0.2)

    def get_figure(self):
        figure = self.figures.get()
        Label(self.root, width=25, height=1, text=f"Geometry: {figure}").place(relx=0.1, rely=0.27)
        self.image = PhotoImage(file=f"resources/{figure}.png")
        Label(self.root, image=self.image,).place(relx=0.6, rely=0.05)
        # self.label_image.image = self.image

        self.create(figure)

    def create(self, figure):
        self.calc = Calculator(figure)
        props = self.calc.get_figure_info()
        self.draw_fields(props)

    def draw_fields(self, props):
        self.entries = []
        step = 0.1
        Label(self.root, width=15, height=1, text=f"Fill in these fields:").place(relx=0.1, rely=0.4)
        for prop in props:
            Label(self.root, width=15, height=1, text=f"{prop}").place(relx=0.1, rely=(0.4 + step))
            entry = ttk.Entry(self.root, width=15, )
            entry.place(relx=0.5, rely=(0.4 + step))
            self.entries.append(entry)
            step += 0.1

        ttk.Button(text="ok", command=self.button_action).place(relx=0.174, rely=0.75)

    def button_action(self):
        calc_args = list(map(lambda x: x.get(), self.entries))
        if self.calc:
            self.answer = self.calc.insert_param(calc_args)
            Label(self.root, width=15, height=3, text=self.answer).place(relx=0.5, rely=0.75)
