import graphic
import data
import level12_astar
import level12_bfs
import tkinter as tk
import time
import level3_monster
import level4_monster
import level3_remake_again as lvl3


def get_maze_path():
    #string = input("Input maze name: ")
    string = 'map5_lv4'
import level3 as lvl3


def get_maze_path():
    string = input("Input maze name: ")
    string = "../INPUT/" + string + ".txt"
    return string


if __name__ == '__main__':
    image_path = get_maze_path()
    level = int(input("Input level of game (1/2/3/4): "))
    speed = int(input("Input game speed (ms): "))

    root = tk.Tk()
    pacman_game = graphic.PacmanGame(image_path, master=root)
    if level == 1 or level == 2:
        start = time.time()
        pacman_path = level12_astar.A_star_run(image_path)
        monster_path = []
        end = time.time()
        execution_time = end - start

    elif level == 3:
        start = time.time()
        pacman_path, monster_path,finish_state = lvl3.level3(image_path)
        end = time.time()
        execution_time = end - start
    elif level == 4:
        monster_path = []
        pacman_path = [(0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0)]
        monster_path = level4_monster.path_for_each_monster(image_path)
        pass

    if not isinstance(pacman_path, bool):
        pacman_game.master.title("Pacman Game")
        pacman_game.draw_maze()
        pacman_game.draw_pacman()
        pacman_game.show_score()
        score = pacman_game.pacman_move(pacman_path, monster_path, 1, speed)
        print("Score is:", score)
        print("Execution time is: ", execution_time)
        pacman_game.mainloop()

    else:
        print('Cant find any path to get to the food')
