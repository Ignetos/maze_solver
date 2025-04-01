from window import Window
from maze import Maze

win = Window(800, 600)
""" cells = []
for i in range(1, 15):
    for j in range(1, 11):
        cells.append(Cell(win, Point(50*i, 50*j), Point((50*i)+50, (50*j)+50)))
for cell in range(len(cells)):
    cells[cell].draw() """
maze = Maze(50, 50, 10, 14, 50, 50, win)
maze.solve()
win.wait_for_close()