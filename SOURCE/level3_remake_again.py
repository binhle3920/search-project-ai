import data
import level3_monster as ms
import random

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
    if pacman_pos[0] >= size_maze[0] or pacman_pos[1] >= size_maze[1] or pacman_pos[0] < 0 or pacman_pos[1] < 0:
        return False
    else:
        return True

def pacman_moveable_pos(maze, pacman_pos, monster_pos, size):
    pacman_moveable_pos = []
    pacman_pos_mov = []
    if monster_pos:
        if in_maze((pacman_pos[0], pacman_pos[1] + 1), size):
            if (maze[pacman_pos[0]][pacman_pos[1] + 1] ==0) or (maze[pacman_pos[0]][pacman_pos[1] + 1] ==2) :
                pacman_pos_mov = (pacman_pos[0], pacman_pos[1]+1) 
                if check_pac_to_allmonster(pacman_pos_mov,monster_pos)==True:
                    pacman_moveable_pos.append(pacman_pos_mov)

        if in_maze((pacman_pos[0], pacman_pos[1] - 1), size):
            if (maze[pacman_pos[0]][pacman_pos[1]-1] ==0) or (maze[pacman_pos[0]][pacman_pos[1]-1] ==2):
                pacman_pos_mov = (pacman_pos[0],pacman_pos[1]-1) 
                if check_pac_to_allmonster(pacman_pos_mov,monster_pos)==True:
                    pacman_moveable_pos.append(pacman_pos_mov)

        if in_maze((pacman_pos[0] + 1, pacman_pos[1]), size):
            if (maze[pacman_pos[0]+1][pacman_pos[1]] ==0) or (maze[pacman_pos[0]+1][pacman_pos[1]] ==2):
                pacman_pos_mov = (pacman_pos[0]+1,pacman_pos[1])
                if check_pac_to_allmonster(pacman_pos_mov,monster_pos)==True:
                    pacman_moveable_pos.append(pacman_pos_mov)

        if in_maze((pacman_pos[0] - 1, pacman_pos[1]), size):
            if (maze[pacman_pos[0]-1][pacman_pos[1]] == 0) or (maze[pacman_pos[0]-1][pacman_pos[1]] == 2):
                pacman_pos_mov = (pacman_pos[0]-1,pacman_pos[1]) 
                if check_pac_to_allmonster(pacman_pos_mov,monster_pos)==True:
                    pacman_moveable_pos.append(pacman_pos_mov)
    else:
        if in_maze((pacman_pos[0], pacman_pos[1] + 1), size):
            pacman_moveable_pos.append((pacman_pos[0], pacman_pos[1] + 1))
        if in_maze((pacman_pos[0], pacman_pos[1] - 1), size):
            pacman_moveable_pos.append((pacman_pos[0], pacman_pos[1] - 1))
        if in_maze((pacman_pos[0] + 1, pacman_pos[1]), size):
            pacman_moveable_pos.append((pacman_pos[0] + 1, pacman_pos[1]))
        if in_maze((pacman_pos[0] - 1, pacman_pos[1]), size):
            pacman_moveable_pos.append((pacman_pos[0] - 1, pacman_pos[1]))

    return pacman_moveable_pos

def level3(path):
    maze, size, pacman_pos = data.get_maze(path)
    path_pacman,monster_path=A_star_call(maze,size,tuple(pacman_pos))
    #print(path_pacman)
    #print(monster_path)
    return path_pacman, monster_path

def Manhattan_food(u, v):
    return abs(u[0]-v[0])+abs(u[1]-v[1])


def findValue(l, v):
    for index, i in enumerate(l):
        if i == v:
            return index
    return -1


def AddNode(v, x):
    # 0 hang-1,cot
    # 1 hang,cot-1
    # 2 hang+1,cot
    # 3 hang,cot+1
    if x == 0:
        return (v[0]-1, v[1])
    elif x == 1:
        return (v[0], v[1]-1)
    elif x == 2:
        return (v[0]+1, v[1])
    elif x == 3:
        return (v[0], v[1]+1)
    else:
        return -1


def solution(trace, v, start):
    path_list = []
    while(trace[v[0]][v[1]] != -1):
        path_list.append(v)
        v = trace[v[0]][v[1]]
    path_list.append(start)
    path_list.reverse()
    return path_list


def A_star(MapLen, Map, start, goal, food_pos,monster_path):
    frontier = []
    explored = []
    trace = []
    frontier = [(Manhattan_food(start, goal), start)]
    for i in range(MapLen[0]):
        temp = [-1]*MapLen[1]
        trace.append(temp)

    while(len(frontier) > 0):
        frontier = sorted(frontier)
        u = frontier.pop(0)
        more_food, monsters_pos = scan_around(Map, u[1], MapLen)
        for food in more_food:
            if food not in food_pos:
                food_pos.append(food)
        u_Fcost = u[0]
        u_node = u[1]        
        explored.append(u_node)
        if u_node!=start:
            monster_path,Map = ms.monster_move(Map, monster_path)
        if u_node == goal:
            return Map,solution(trace, goal, start)
        path_cost = u_Fcost-Manhattan_food(u_node, goal)
        if Map[u_node[0]][u_node[1]] == 2:
            index=food_pos.index(u_node)
            food_pos.pop(index)
            Map[u_node[0]][u_node[1]]=0
        check = False
        moveable_pos=pacman_moveable_pos(Map, u_node, monsters_pos, MapLen)
        for v in range(4):
            # hang-1,cot
            if (u_node[0] > 0) and (v == 0):
                temp = AddNode(u_node, v)
                check = True
            # hang,cot-1
            if (u_node[1] > 0) and (v == 1):
                temp = AddNode(u_node, v)
                check = True
            # hang+1,cot
            if (u_node[0] < MapLen[0]-1) and (v == 2):
                temp = AddNode(u_node, v)
                check = True
            # hang,cot+1
            if (u_node[1] < MapLen[1]-1) and (v == 3):
                temp = AddNode(u_node, v)
                check = True
            if (check) and (Map[temp[0]][temp[1]] != 1) and (temp in moveable_pos):
                pos_frontier = findValue(frontier, temp)
                if (temp not in explored) and (pos_frontier == -1):
                    trace[temp[0]][temp[1]] = (u_node[0], u_node[1])
                    frontier.append((path_cost+1+Manhattan_food(temp, goal), temp))
                elif pos_frontier != -1:
                    if frontier[pos_frontier][0] > path_cost+1+Manhattan_food(temp, goal):
                        trace[temp[0]][temp[1]] = (u_node[0], u_node[1])
                        frontier[pos_frontier] = (
                            path_cost+1+Manhattan_food(temp, goal), temp)
    return Map,False
def random_find_food(Map,MapLen,path_pacman,monster_path,explored_cells):
    count_random=0
    pacman_pos=path_pacman[-1]
    food_pos=[]
    while count_random <30 :
        priority_cells=[]
        more_food, monsters_pos = scan_around(Map, pacman_pos, MapLen)
        moveable_pos=pacman_moveable_pos(Map, pacman_pos, monsters_pos, MapLen)
        for pos in moveable_pos:
            if pos not in explored_cells:
                priority_cells.append(pos)
        if len(priority_cells)>0:
            random_step = random.choice(priority_cells)
        else:
            random_step = random.choice(moveable_pos)
        path_pacman.append(random_step)
        monster_path,Map = ms.monster_move(Map, monster_path)
        more_food, monsters_pos = scan_around(Map, pacman_pos, MapLen)
        for food in more_food:
            if food not in food_pos:
                food_pos.append(food)
        if len(food_pos)>0:
            return Map,monster_path,food_pos
        count_random+=1
    return Map, monster_path,food_pos
    
def A_star_call(Map,MapLen,PacmanPos):
    start = PacmanPos
    food_pos,monsters_pos = scan_around(Map, PacmanPos, MapLen)
    path_pacman=[]
    monster_path = ms.init_monster(Map, MapLen)
    explored_cells=[]
    while (True):
        food_pos = sorted(
            food_pos, key=lambda food: Manhattan_food(start, food))
        if len(food_pos)==0:
            Map,monster_path,food_pos=random_find_food(Map,MapLen,path_pacman,monster_path,explored_cells)
            if len(food_pos)==0:
                return path_pacman,monster_path
        Map,path_food = A_star(MapLen, Map, start, food_pos[0], food_pos,monster_path)
        next_food = food_pos.pop(0)
        if path_food == False:
            print('not have path')
        else:
            Map[next_food[0]][next_food[1]]=0
            start=next_food
            for i in range(len(path_food)-1):
                path_pacman.append(path_food[i])
                explored_cells.append(i)
                

