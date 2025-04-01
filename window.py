from tkinter import Tk, BOTH, Canvas
from point import Line

class Window:
    def __init__(self, width, height):
        self.__root = Tk()
        self.__root.title('Maze')
        self.__canvas = Canvas(self.__root, height= height,
                             width= width, bg= 'white',
                             relief= 'solid')
        self.__canvas.pack(fill= BOTH, expand= 1)
        self.running = False
        self.__root.protocol("WM_DELETE_WINDOW", self.close)

    def redraw(self):
        self.__root.update_idletasks()
        self.__root.update()

    def draw_line(self, line: Line, fill_color: str):
        line.draw(self.__canvas, fill_color)

    def wait_for_close(self):
        self.running = True
        while self.running:
            self.redraw()

    def close(self):
        self.running = False
