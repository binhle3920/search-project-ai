import graphic
import data
import level12_astar
import level12_bfs
import tkinter as tk
import time
import level3_monster
import level3_remake_again as lvl3


def get_maze_path():
    #string = input("Input maze name: ")
    string = 'map3_lv4'
    string = "../INPUT/" + string + ".txt"
    return string


if __name__ == '__main__':
    image_path = get_maze_path()
    #level = int(input("Input level of game (1/2/3/4): "))
    level=4
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
    elif level == 3:
        pacman_path, monster_path,finish_state = lvl3.level3(image_path)
    elif level == 4:
        monster_path = []
        shape = data.get_maze(image_path)
        maze = shape[0]
        pacman_pos = shape[2]
        size = shape[1]

        pacman_path = [(0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0)]
        monster = level3_monster.init_monster(maze, size)
        for i in range(len(monster)):
            monster_path.append(level3_monster.A_star_monster(maze,pacman_pos,i,size))
        
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
