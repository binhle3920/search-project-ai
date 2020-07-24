import tkinter as tk

class PacmanGame(tk.Frame):
    def __init__(self, master = None):
        super().__init__(master)


if __name__ == '__main__':
    root = tk.Tk()
    pacman_game = PacmanGame(master=root)
    pacman_game.master.title("Pacman Game")
    pacman_game.master.minsize(1400, 900)
    pacman_game.mainloop()
