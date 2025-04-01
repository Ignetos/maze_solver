from point import Point, Line
from window import Window

class Cell:
    def __init__(self, window: Window, point1: Point, point2: Point):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self._x1 = point1.x
        self._x2 = point2.x
        self._y1 = point1.y
        self._y2 = point2.y
        self._win = window
        self.visited = False
        self.size = [(point2.x - point1.x), (point2.y - point1.y)]

    def draw(self):
        p1 = Point(self._x1, self._y1)
        p2 = Point(self._x2, self._y1)
        p3 = Point(self._x1, self._y2)
        p4 = Point(self._x2, self._y2)
        if self.has_left_wall:
            self._make_wall(p1, p3, 'black')
        else:
            self._make_wall(p1, p3, 'white')
        if self.has_right_wall:
            self._make_wall(p2, p4, 'black')
        else:
            self._make_wall(p2, p4, 'white')
        if self.has_top_wall:
            self._make_wall(p1, p2, 'black')
        else:
            self._make_wall(p1, p2, 'white')
        if self.has_bottom_wall:
            self._make_wall(p3, p4, 'black')
        else:
            self._make_wall(p3, p4, 'white')

    def _make_wall(self, point1: Point, point2: Point, color: str):
        line = Line(point1, point2)
        self._win.draw_line(line, color)

    def draw_move(self, to_cell, undo=False):
        c1 = self.get_center()
        c2 = to_cell.get_center()
        line = Line(c1, c2)
        if undo:
            color = 'grey'
        else:
            color = 'red'
        self._win.draw_line(line, color)

    def get_center(self):
        x = self.size[0] // 2
        y = self.size[1] // 2
        return Point(self._x1 + x, self._y1 + y)