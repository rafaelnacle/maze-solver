from tkinter import Tk, BOTH, Canvas


class Window:
    def __init__(self, width, height):
        self.root = Tk()
        self.title = "Maze Solver"
        self.root.title(self.title)
        self.canvas = Canvas(self.root, bg="white", width=width, height=height)
        self.canvas.pack(fill=BOTH, expand=1)
        self.is_running = False
        self.root.protocol("WM_DELETE_WINDOW", self.close)

    def redraw(self):
        self.root.update_idletasks()
        self.root.update()

    def wait_for_close(self):
        self.is_running = True

        def loop():

            if self.is_running:
                self.redraw()
                self.root.after(1000, loop)
        print("window closed")
        loop()

    def close(self):
        self.is_running = False


def main():
    win = Window(800, 600)
    win.wait_for_close()
