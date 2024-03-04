from canvas import Window, Line, Point
from cell import Cell


def main():
    window = Window(800, 600)

    cell = Cell(window)
    cell.has_left_wall = False
    cell.draw(30, 30, 100, 100)

    cell = Cell(window)
    cell.has_right_wall = False
    cell.draw(135, 135, 200, 200)

    cell = Cell(window)
    cell.has_bottom_wall = False
    cell.draw(100, 100, 250, 250)

    cell = Cell(window)
    cell.has_top_wall = False
    cell.draw(440, 440, 500, 500)

    window.wait_for_close()


main()
