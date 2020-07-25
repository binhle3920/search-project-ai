import tkinter as tk
from PIL import Image, ImageTk
import data 

size_of_block = 50 

class PacmanGame(tk.Frame):
    def __init__(self, maze_name, master = None):
        super().__init__(master)
        self.maze, self.size, self.pacman_pos = data.get_maze(maze_name)
        self.maze_frame = tk.Canvas(width = self.size[1] * size_of_block, height = self.size[0] * size_of_block, bg = "black")
        self.maze_frame.pack() 
    
    def draw_maze(self):
        wall_block_image = Image.open("../IMAGE/wall_block.png")
        wall_block_image = wall_block_image.resize((size_of_block, size_of_block), Image.ANTIALIAS)
        wall_block_image = ImageTk.PhotoImage(wall_block_image)

        food_image = Image.open("../IMAGE/food.png")
        food_image = food_image.resize((size_of_block, size_of_block), Image.ANTIALIAS)
        food_image = ImageTk.PhotoImage(food_image)

        ghost_image = Image.open("../IMAGE/ghost.png")
        ghost_image = ghost_image.resize((size_of_block, size_of_block), Image.ANTIALIAS)
        ghost_image = ImageTk.PhotoImage(ghost_image)

        for row in range(self.size[0]):
            for column in range(self.size[1]):
                if self.maze[row][column] == 1:
                    self.maze_frame.create_image(column * size_of_block, row * size_of_block, anchor='nw', image=wall_block_image)
                if self.maze[row][column] == 2:
                    self.maze_frame.create_image(column * size_of_block, row * size_of_block, anchor='nw', image=food_image)
                if self.maze[row][column] == 3:
                    self.maze_frame.create_image(column * size_of_block, row * size_of_block, anchor='nw', image=ghost_image)
        
        self.maze_frame.image = [wall_block_image, food_image, ghost_image]


    def draw_pacman(self):
        pacman_image = Image.open("../IMAGE/pacman.png")
        pacman_image = pacman_image.resize((size_of_block, size_of_block), Image.ANTIALIAS)
        pacman_image = ImageTk.PhotoImage(pacman_image)

        self.maze_frame.create_image(self.pacman_pos[1] * size_of_block, self.pacman_pos[0] * size_of_block, anchor='nw', image=pacman_image)
        self.maze_frame.image.append(pacman_image)

if __name__ == '__main__':
    root = tk.Tk()
    pacman_game = PacmanGame("../INPUT/map5_lv4.txt", master=root)
    pacman_game.master.title("Pacman Game")
    pacman_game.draw_maze()
    pacman_game.draw_pacman()
    pacman_game.mainloop()
    
