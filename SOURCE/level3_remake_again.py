import data

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
