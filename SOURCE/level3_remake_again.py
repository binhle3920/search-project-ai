import data
import level3_monster as ms

def scan_around(maze, pacman_pos, size):
    food_pos = []
    monster_pos = []

    for i in range(-3, 4):
        for j in range(-3, 4):
            if pacman_pos[0] + i >= 0 and pacman_pos[0] + i < size[0] and pacman_pos[1] + j >= 0 and  pacman_pos[1] + j < size[1]:
                if maze[pacman_pos[0] + i][pacman_pos[1] + j] == 2:
                    food_pos.append((pacman_pos[0] + i, pacman_pos[1] + j))
                elif maze[pacman_pos[0] + i][pacman_pos[1] + j] == 3:
                    monster_pos.append((pacman_pos[0] + i, pacman_pos[1] + j))
    return food_pos, monster_pos

def Manhattan (pacman_pos, monster_pos):
    return abs(pacman_pos[0]-monster_pos[0]) + abs (pacman_pos[1]-monster_pos[1])

def check_pac_to_allmonster(pacman_pos,monster_pos):
    for i in range(len(monster_pos)):
        if Manhattan(pacman_pos,monster_pos[i]) < 2:
                return False
                break
    return True

def in_maze(pacman_pos,size_maze):
    print(pacman_pos, size_maze)
    if pacman_pos[0] >= size_maze[0] or pacman_pos[1] >= size_maze[1] or pacman_pos[0] < 0 or pacman_pos[1] < 0:
        return False
    else:
        return True

def pacman_moveable_pos(maze, pacman_pos, monster_pos, size):
    pacman_moveable_pos = []
    pacman_pos_mov = []
    if monster_pos:
        if in_maze((pacman_pos[0], pacman_pos[1] + 1), size):
            if maze[pacman_pos[0]][pacman_pos[1] + 1] == 0:
                pacman_pos_mov = (pacman_pos[0], pacman_pos[1]+1) 
                if check_pac_to_allmonster(pacman_pos_mov,monster_pos)==True:
                    pacman_moveable_pos.append(pacman_pos_mov)

        if in_maze((pacman_pos[0], pacman_pos[1] - 1), size):
            if maze[pacman_pos[0]][pacman_pos[1]-1] == 0:
                pacman_pos_mov = (pacman_pos[0],pacman_pos[1]-1) 
                if check_pac_to_allmonster(pacman_pos_mov,monster_pos)==True:
                    pacman_moveable_pos.append(pacman_pos_mov)

        if in_maze((pacman_pos[0] + 1, pacman_pos[1]), size):
            if maze[pacman_pos[0]+1][pacman_pos[1]] == 0:
                pacman_pos_mov = (pacman_pos[0]+1,pacman_pos[1])
                if check_pac_to_allmonster(pacman_pos_mov,monster_pos)==True:
                    pacman_moveable_pos.append(pacman_pos_mov)

        if in_maze((pacman_pos[0] - 1, pacman_pos[1]), size):
            if maze[pacman_pos[0]-1][pacman_pos[1]] == 0:
                pacman_pos_mov = (pacman_pos[0]-1,pacman_pos[1]) 
                if check_pac_to_allmonster(pacman_pos_mov,monster_pos)==True:
                    pacman_moveable_pos.append(pacman_pos_mov)

    return pacman_moveable_pos

def level3(path):
    maze, size, pacman_pos = data.get_maze(path)

    monster_path = ms.init_monster(maze, size)
    monster_path = ms.monster_move(maze, monster_path)

