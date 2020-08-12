import graphic
import data
import level12_astar
import level12_bfs
import tkinter as tk
import time
import level3_remake_again as lvl3


def get_maze_path():
    #string = input("Input maze name: ")
    string = 'map2_lv2'
    string = "../INPUT/" + string + ".txt"
    return string


if __name__ == '__main__':
    image_path = get_maze_path()
    #level = int(input("Input level of game (1/2/3/4): "))
    level=2
    #speed = int(input("Input game speed (ms): "))
    speed=200

    root = tk.Tk()
    pacman_game = graphic.PacmanGame(image_path, master=root)
    if level == 1 or level == 2:
        start = time.time()
        pacman_path = level12_astar.A_star_run(image_path)
        monster_path = []
        end = time.time()
        execution_time = end - start

    if level == 3:
        pacman_path, monster_path,finish_state = lvl3.level3(image_path)

    if not isinstance(pacman_path, bool):
        pacman_game.master.title("Pacman Game")
        pacman_game.draw_maze()
        pacman_game.draw_pacman()
        score = pacman_game.pacman_move(pacman_path, monster_path, 1, speed, 1)
        print("Score is:", score)
        #print("Execution time is: ", execution_time)
        pacman_game.mainloop()

    else:
        print('Cant find any path to get to the food')
