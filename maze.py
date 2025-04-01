import time
import random

from window import Window
from cell import Cell
from point import Point

class Maze:
    def __init__(
            self,
            x1,
            y1,
            num_rows,
            num_cols,
            cell_size_x,
            cell_size_y,
            win: Window,
            seed= None,
            ):
        self._x = x1
        self._y = y1
        self._num_rows = num_rows
        self._num_cols = num_cols
        self._cell_size = [cell_size_x, cell_size_y]
        self._win = win
        self._cells = [[0 for i in range(self._num_rows)] for j in range(self._num_cols)]

        self._create_cells()
        self._break_entrance_and_exit()
        self._break_walls_r(0, 0)
        self._reset_cells_visited()

    def solve(self):
        return self._solve_r()
    
    def _solve_r(self, i= 0, j= 0):
        end = (i == self._num_cols-1 and j == self._num_rows-1)
        current = self._cells[i][j]
        to_visit = []
        if (i-1) >= 0:
            if not self._cells[i-1][j].visited and not current.has_left_wall:
                to_visit.append((i-1, j))
        if (i+1) < self._num_cols:
            if not self._cells[i+1][j].visited and not current.has_right_wall:
                to_visit.append((i+1, j))
        if (j-1) >= 0:
            if not self._cells[i][j-1].visited and not current.has_top_wall:
                to_visit.append((i, j-1))
        if (j+1) < self._num_rows:
            if not self._cells[i][j+1].visited and not current.has_bottom_wall:
                to_visit.append((i, j+1))
        if end:
            return True
        elif not end and len(to_visit) == 0:
            return False
        else:
            self._animate(0.1)
            self._cells[i][j].visited = True
            for move in to_visit:
                current.draw_move(self._cells[move[0]][move[1]])
                if self._solve_r(move[0], move[1]):
                    current.draw_move(self._cells[move[0]][move[1]])
                    return True
                else:
                    current.draw_move(self._cells[move[0]][move[1]], True)

    def _create_cells(self):
        for i in range(self._num_cols):
            for j in range(self._num_rows):
                x = self._x + (i * self._cell_size[0])
                y = self._y + (j * self._cell_size[1])
                self._cells[i][j] = Cell(self._win, Point(x, y), Point(x + self._cell_size[0], y + self._cell_size[1]))
                self._draw_cell(i, j)

    def _reset_cells_visited(self):
        for i in range(self._num_cols):
            for j in range(self._num_rows):
                self._cells[i][j].visited = False

    def _draw_cell(self, i, j):
        self._cells[i][j].draw()
        self._animate(0.001)

    def _break_entrance_and_exit(self):
        self._cells[0][0].has_top_wall = False
        self._draw_cell(0, 0)
        self._cells[-1][-1].has_bottom_wall = False
        self._draw_cell(-1, -1)

    def _break_walls_r(self, i, j):
        self._cells[i][j].visited = True
        while True:
            to_visit = []
            random.seed()
            if (i-1) >= 0:
                if not self._cells[i-1][j].visited:
                    to_visit.append((i-1, j, 'left'))
            if (i+1) < self._num_cols:
                if not self._cells[i+1][j].visited:
                    to_visit.append((i+1, j, 'right'))
            if (j-1) >= 0:
                if not self._cells[i][j-1].visited:
                    to_visit.append((i, j-1, 'up'))
            if (j+1) < self._num_rows:
                if not self._cells[i][j+1].visited:
                    to_visit.append((i, j+1, 'down'))
            if len(to_visit) == 0:
                self._draw_cell(i, j)
                return
            else:
                move = random.choice(to_visit)
                if move[2] == 'left':
                    self._cells[i][j].has_left_wall = False
                if move[2] == 'right':
                    self._cells[i][j].has_right_wall = False
                if move[2] == 'up':
                    self._cells[i][j].has_top_wall = False
                if move[2] == 'down':
                    self._cells[i][j].has_bottom_wall = False
                self._break_walls_r(move[0], move[1])

    def _animate(self, sec):
        self._win.redraw()
        time.sleep(sec)