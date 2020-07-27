import tkinter as tk
from PIL import Image, ImageTk
import time
import data 

size_of_block = 50 
path=[[0,0],[1,0],[1,1],[1,2],[1,3],[2,3],[3,3],[3,4],[3,5],[3,6],[3,7],[3,8],[4,8],[5,8],[6,8],[7,8],[7,7]]
class PacmanGame(tk.Frame):
    def __init__(self, maze_name, master = None):
        super().__init__(master)
        self.maze, self.size, self.pacman_pos = data.get_maze(maze_name)
        self.pacman = None
        self.food = []
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
                    self.food.append((self.maze_frame.create_image(column * size_of_block, row * size_of_block, anchor='nw', image=food_image), (row, column)))
                if self.maze[row][column] == 3:
                    self.maze_frame.create_image(column * size_of_block, row * size_of_block, anchor='nw', image=ghost_image)
        
        self.maze_frame.image = [wall_block_image, food_image, ghost_image]


    def draw_pacman(self):
        pacman_image = Image.open("../IMAGE/pacman.png")
        pacman_image = pacman_image.resize((size_of_block, size_of_block), Image.ANTIALIAS)
        pacman_image = ImageTk.PhotoImage(pacman_image)

        self.pacman = self.maze_frame.create_image(self.pacman_pos[1] * size_of_block, self.pacman_pos[0] * size_of_block, anchor='nw', image=pacman_image)
        self.maze_frame.image.append(pacman_image)
    
    
    def move_step(self, pacman_pos, old_coor):
        pass

    def pacman_move(self, path, index_path):
        #stop
        if index_path == len(path):
            return

        #check food
        if self.maze[path[index_path][0]][path[index_path][1]] == 2:
            for i in range(len(self.food)):
                if self.food[i][1] == path[index_path]:
                    del_image = self.food.pop(i)
                    self.maze_frame.delete(del_image)

        #continue
        self.maze_frame.move(self.pacman, (path[index_path][1] - path[index_path - 1][1]) * size_of_block,  (path[index_path][0] - path[index_path - 1][0]) * size_of_block )
        self.maze_frame.after(500)
        self.maze_frame.update()
        self.pacman_move(path, index_path + 1)

if __name__ == '__main__':
    root = tk.Tk()
    pacman_game = PacmanGame("../INPUT/map1_lv1.txt", master=root)
    pacman_game.master.title("Pacman Game")
    pacman_game.draw_maze()
    pacman_game.draw_pacman()
    pacman_game.pacman_move(path, 1)
    pacman_game.mainloop()
