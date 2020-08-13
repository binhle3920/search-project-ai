import level3_monster
import random
import data





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


def smart_monster(maze, pacman_pos, index, size , monster):
    start = monster[index][0]
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

def A_star_monster(maze, pacman_pos,index, size,monster):
    return smart_monster(maze, pacman_pos, index, size,monster)


def monster_move(maze,pacman_pos,index,size,monster):
    path = A_star_monster(maze,pacman_pos, index, size , monster)
    print("monster thu 1",path)
    smart_path = []
    num = 0
    num = random.randint(2,len(path))
    print("len",len(path))
    print(num)
    for i in range(num):
        smart_path.append(path[i])
    return smart_path
    

def path_for_each_monster(path):
    maze,size,pacman_pos = data.get_maze(path)
    monster = level3_monster.init_monster(maze, size)

    monster_path = []
    for i in range(len(monster)):

        monster_path.append(monster_move(maze,pacman_pos,i,size,monster))
    print("each monster path",monster_path)
    
    return monster_path


