import graphic, data, level12_astar, level12_bfs
import tkinter as tk
import time

def get_maze_path():
    string = input("Input maze name: ")
    string = "../INPUT/" + string + ".txt"
    return string

if __name__ == '__main__':
    image_path = get_maze_path()
    level = int(input("Input level of game (1/2/3/4): "))
    
    root = tk.Tk()
    pacman_game = graphic.PacmanGame(image_path, master=root)
    if level == 1 or level == 2:
        start = time.time()
        path = level12_astar.A_star_run(image_path)
        end = time.time()
        execution_time = end - start

    if not isinstance(path, bool):
        pacman_game.master.title("Pacman Game")
        pacman_game.draw_maze()
        pacman_game.draw_pacman()
        score = pacman_game.pacman_move(path, 1)
        print("Score is:", score)
        print("Execution time is: ", execution_time)
        pacman_game.mainloop()
    else:
        print('Cant find any path to get to the food')
