from canvas import Window, Line, Point


def main():
    window = Window(800, 600)
    line = Line(Point(30, 30), Point(300, 300))
    window.draw_line(line, "black")
    window.wait_for_close()


main()
