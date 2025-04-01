from tkinter import Canvas

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Line:
    def __init__(self, point1: Point, point2: Point):
        self.x1 = point1.x
        self.x2 = point2.x
        self.y1 = point1.y
        self.y2 = point2.y
    
    def draw(self, canvas: Canvas, fill_color: str):
        canvas.create_line(self.x1, self.y1, self.x2, self.y2, fill= fill_color, width= 2)
