import random

monster_init_pos = [] 
monster_cur_pos = []
monster_possible_pos = []
monster_over_food = []

def get_monster_init_pos(maze, size):
    for i in range(size[0]):
        for j in range(size[1]):
            if maze[i][j] == 3:
                monster_init_pos.append((i, j))
                monster_over_food.append(0)

def monster_possible_move(maze, size):
    a_monster_move = []
    for monster in monster_init_pos:
        for i in range(-1, 2):
            for j in range(-1, 2):
                if monster[0] + i >= 0 and monster[0] + i < size[0] and monster[1] + j >= 0 and  monster[1] + j < size[1]:
                    if maze[monster[0] + i][monster[1] + j] == 0 or maze[monster[0] + i][monster[1] + j] == 2:
                        a_monster_move.append((monster[0] + i, monster[1] + j))
        monster_possible_pos.append(a_monster_move)
        a_monster_move = []

def possible_choice(monster_number, direction):
    if direction == "up":
        pos = (monster_cur_pos[monster_number][0] + 1, monster_cur_pos[monster_number][1])
        if pos in monster_possible_pos[monster_number]:
            return pos
        else:
            return "up"
    elif direction == "down":
        pos = (monster_cur_pos[monster_number][0] - 1, monster_cur_pos[monster_number][1])
        if pos in monster_possible_pos[monster_number]:
            return pos
        else:
            return "down"
    elif direction == "left":
        pos = (monster_cur_pos[monster_number][0], monster_cur_pos[monster_number][1] - 1)
        if pos in monster_possible_pos[monster_number]:
            return pos
        else:
            return "left"
    elif direction == "right":
        pos = (monster_cur_pos[monster_number][0], monster_cur_pos[monster_number][1] + 1)
        if pos in monster_possible_pos[monster_number]:
            return pos
        else:
            return "right"

monster_cur_pos = monster_init_pos
def init_monster(maze, size):
    get_monster_init_pos(maze, size)
    monster_possible_move(maze, size)
    
    monster_path = []
    for i in range(len(monster_init_pos)):
        monster_path.append([monster_init_pos[i]])
    return monster_path

def monster_move(maze, monster_path):
    for monster_number in range(len(monster_init_pos)):
        available_direction = ["up", "down", "left", "right"]
        while len(available_direction) > 0:
            direction = random.choice(available_direction)
            pos = possible_choice(monster_number, direction)
            if isinstance(pos, tuple):
                monster_path[monster_number].append(pos)

                if monster_over_food[monster_number] == 1:
                    maze[monster_cur_pos[monster_number][0]][monster_cur_pos[monster_number][1]] = 2
                else:
                    maze[monster_cur_pos[monster_number][0]][monster_cur_pos[monster_number][1]] = 0

                if maze[pos[0]][pos[1]] == 2:
                    monster_over_food[monster_number] = 1
                else:
                    monster_over_food[monster_number] = 0

                maze[pos[0]][pos[1]] = 3
                    
                monster_cur_pos[monster_number] = pos
                break
            else:
                available_direction.pop(available_direction.index(pos))
        if len(available_direction) == 0:
            monster_path[monster_number].append(monster_cur_pos[monster_number])
    
    return monster_path, maze
        
def solution(trace,v,start):
    path_list=[]
    while(trace[v[0]][v[1]]!=-1):
        path_list.append(v)
        v=trace[v[0]][v[1]]
    path_list.append(start)
    path_list.reverse()
    return path_list

   
def Manhattan(u,v):
    return abs(u[0]-v[0])+abs(u[1]-v[1])


def AddNode(v,x):
    #0 hang-1,cot
    #1 hang,cot-1
    #2 hang+1,cot
    #3 hang,cot+1
    if x==0:
        return (v[0]-1, v[1])
    elif x==1: 
        return (v[0], v[1]-1)
    elif x==2: 
        return (v[0]+1, v[1])
    elif x==3: 
        return (v[0],v[1]+1)
    else: return -1

def findValue(l,v):
    for index,i in enumerate(l):
        if i == v:
            return index
    return -1

def smart_monster(maze, pacman_pos, index, size):
    start = monster_init_pos[index]
    temp = (pacman_pos[1], pacman_pos[0])
    goal = temp
    frontier=[(Manhattan(start,goal),start)]
    explored=[]
    trace=[]
    for i in range(size[0]):
        temp=[-1]*size[1]
        trace.append(temp)
            
    while(len(frontier)>0):
        frontier=sorted(frontier, key=lambda element: (element[0], element[1]))
        u=frontier.pop(0)
        u_Fcost=u[0]
        u_node=u[1]
        explored.append(u_node)
        if u_node==goal:
            return solution(trace,u_node,start)
        path_cost=u_Fcost-Manhattan(u_node,goal)
        check=False
        for v in range(4):
            #hang-1,cot
            if (u_node[0]>0) and (v==0):
                temp=AddNode(u_node,v)
                check=True
            #hang,cot-1
            if (u_node[1]>0) and (v==1):
                temp=AddNode(u_node,v)
                check=True
            #hang+1,cot
            if (u_node[0]<size[0]-1) and (v==2):
                temp=AddNode(u_node,v)
                check=True
            #hang,cot+1
            if (u_node[1]<size[1]-1) and (v==3):
                temp=AddNode(u_node,v)
                check=True
            if (check) and (maze[temp[0]][temp[1]]!=1):
                pos_frontier = findValue(frontier,temp)
                if (temp not in explored) and (pos_frontier == -1):
                    trace[temp[0]][temp[1]]=(u_node[0],u_node[1])
                    frontier.append((path_cost+1+Manhattan(temp,goal),temp))
                elif pos_frontier != -1:
                    if frontier[pos_frontier][0]> path_cost+1+Manhattan(temp,goal):
                        trace[temp[0]][temp[1]]=(u_node[0],u_node[1])
                        frontier[pos_frontier]=(path_cost+1+Manhattan(temp,goal),temp)
    return [monster_pos]

def A_star_monster(maze, pacman_pos,index, size):
    return smart_monster(maze, pacman_pos, index, size)