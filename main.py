from canvas import Window, Line, Point
from cell import Cell


def main():
    window = Window(800, 600)

    cell1 = Cell(window)
    cell1.has_right_wall = False
    cell1.draw(50, 50, 100, 100)

    cell2 = Cell(window)
    cell2.has_left_wall = False
    cell2.has_bottom_wall = False
    cell2.draw(100, 50, 150, 100)

    cell1.draw_move(cell2)

    cell3 = Cell(window)
    cell3.has_top_wall = False
    cell3.has_right_wall = False
    cell3.draw(100, 100, 150, 150)

    cell2.draw_move(cell3)

    cell4 = Cell(window)
    cell4.has_left_wall = False
    cell4.draw(150, 100, 200, 150)

    cell3.draw_move(cell4, True)

    window.wait_for_close()


main()
