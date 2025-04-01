import unittest

from maze import Maze
from window import Window

class Tests(unittest.TestCase):
    def test_maze_create_cells(self):
        win = Window(800, 600)
        num_cols = 15
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 5, 5, win)
        self.assertEqual(
            len(m1._cells),
            num_cols,
        )
        self.assertEqual(
            len(m1._cells[0]),
            num_rows,
        )

if __name__ == "__main__":
    unittest.main()