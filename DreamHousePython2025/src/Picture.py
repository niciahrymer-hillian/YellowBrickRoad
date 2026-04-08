import tkinter as tk
from tkinter import ttk
from Square import Square
from Triangle import Triangle
from Circle import Circle


class Picture:
    def __init__(self, root=None):
        self.root = root
        self.root.title("House Drawing Application")
        self.root.geometry("800x600")

        # Create main frame
        main_frame = ttk.Frame(root)
        main_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        # Create canvas for drawing
        self.canvas = tk.Canvas(main_frame, width=600, height=400, bg='lightblue')
        self.canvas.pack(side=tk.LEFT, padx=(0, 10))

        self.wall = None
        self.window = None
        self.roof = None
        self.sun = None

        self.draw()

    def draw(self):
        self.roof = Triangle(canvas=self.canvas, height=100, width=75, color="black", fill="brown", line=2)
        self.roof.move_horizontal(145)
        self.roof.move_vertical(400)
        self.roof.make_visible()

        self.wall = Square(canvas=self.canvas, size=230, color="Black", fill="tan", line=2)
        self.wall.move_horizontal(60)
        self.wall.move_vertical(80)
        self.wall.make_visible()

        self.window = Square(canvas=self.canvas, size=40, color="black", fill="black", line=1)
        self.window.move_horizontal(150)
        self.window.move_vertical(250)
        self.window.make_visible()

        self.window = Square(canvas=self.canvas, size=40, color="black", fill="black", line=1)
        self.window.move_horizontal(240)
        self.window.move_vertical(200)
        self.window.make_visible()

        self.window = Square(canvas=self.canvas, size=40, color="black", fill="black", line=1)
        self.window.move_horizontal(70)
        self.window.move_vertical(200)
        self.window.make_visible()

        self.window = Square(canvas=self.canvas, size=40, color="black", fill="black", line=1)
        self.window.move_horizontal(150)
        self.window.move_vertical(230)
        self.window.make_visible()

        self.window = Square(canvas=self.canvas, size=40, color="black", fill="black", line=1)
        self.window.move_horizontal(150)
        self.window.move_vertical(270)
        self.window.make_visible()

        self.roof = Triangle(canvas=self.canvas, height=150, width=300, color="black", fill="brown", line=2)
        self.roof.move_horizontal(40)
        self.roof.move_vertical(130)
        self.roof.make_visible()

        self.roof = Triangle(canvas=self.canvas, height=100, width=75, color="black", fill="green", line=2)
        self.roof.move_horizontal(450)
        self.roof.move_vertical(385)
        self.roof.make_visible()

        self.roof = Triangle(canvas=self.canvas, height=100, width=75, color="black", fill="green", line=2)
        self.roof.move_horizontal(420)
        self.roof.move_vertical(385)
        self.roof.make_visible()

        self.roof = Triangle(canvas=self.canvas, height=100, width=75, color="black", fill="green", line=2)
        self.roof.move_horizontal(410)
        self.roof.move_vertical(385)
        self.roof.make_visible()

        self.sun = Circle(canvas=self.canvas, diameter=60, color="yellow", fill="yellow", line=1)
        self.sun.move_horizontal(10)
        self.sun.move_vertical(-10)
        self.sun.make_visible()

        self.sun = Circle(canvas=self.canvas, diameter=60, color="white", fill="white", line=1)
        self.sun.move_horizontal(300)
        self.sun.move_vertical(-1)
        self.sun.make_visible()

        self.sun = Circle(canvas=self.canvas, diameter=60, color="white", fill="white", line=1)
        self.sun.move_horizontal(280)
        self.sun.move_vertical(-7)
        self.sun.make_visible()

        self.sun = Circle(canvas=self.canvas, diameter=60, color="white", fill="white", line=1)
        self.sun.move_horizontal(320)
        self.sun.move_vertical(-15)
        self.sun.make_visible()

        self.sun = Circle(canvas=self.canvas, diameter=60, color="white", fill="white", line=1)
        self.sun.move_horizontal(385)
        self.sun.move_vertical(-5)
        self.sun.make_visible()

        self.sun = Circle(canvas=self.canvas, diameter=60, color="white", fill="white", line=1)
        self.sun.move_horizontal(375)
        self.sun.move_vertical(-2)
        self.sun.make_visible()

        self.sun = Circle(canvas=self.canvas, diameter=60, color="white", fill="white", line=1)
        self.sun.move_horizontal(370)
        self.sun.move_vertical(-3)
        self.sun.make_visible()

        self.sun = Circle(canvas=self.canvas, diameter=60, color="white", fill="white", line=1)
        self.sun.move_horizontal(390)
        self.sun.move_vertical(-7)
        self.sun.make_visible()

    def set_black_and_white(self):
        if self.wall:
            self.wall.change_color("black")
            self.window.change_color("white")
            self.roof.change_color("black")
            self.sun.change_color("black")

    def set_color(self):
        if self.wall:
            self.wall.change_color("red")
            self.window.change_color("black")
            self.roof.change_color("green")
            self.sun.change_color("yellow")
