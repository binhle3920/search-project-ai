import data as data
import collections

def food_pos(Map):
    for index_i,i in enumerate(Map):
        for index_j,j in enumerate(i):
            if j==2:
                return [index_i,index_j] # vị trí thức ăn

def path_G(Map):
    temp =[]
    for i in range(len(Map)):
        for j in range(len(Map[i])):
            if (Map[i][j] == 0 or Map[i][j] == 2):
                temp.append((i,j))
    #print(temp)
    list = {}
    temp2=[]
    for i in range(len(temp)):
        for j in range(len(temp)):
            if((temp[i][0] + 1 == temp[j][0] and temp[i][1]==temp[j][1]) or (temp[i][1] +1 == temp[j][1] and temp[i][0] == temp[j][0]) or (temp[i][0] - 1 == temp[j][0] and temp[i][1]==temp[j][1]) or(temp[i][1] -1 == temp[j][1] and temp[i][0] == temp[j][0]) ):
                 #print(temp[i])
                 #print(temp[j])
                temp2.append(temp[j])
        
        list[tuple(temp[i])]=temp2
        temp2=[]

   
    
    print(list)
    return list

    



def BFS(path): #path= link dan
    Map,_,Pacman_pos = data.get_maze(path) 
    Food_pos = food_pos(Map)
    
   
    graph = path_G(Map)
    start = tuple(Pacman_pos) #list
   # print(start)
    goal = tuple(Food_pos) # list
   # print(goal)
    if start == goal:
        return [start]
    visited = {start}
    queue = collections.deque([(start, ())])
   # print(queue)
    Time =0
    while queue:
        current, path = queue.popleft()
        #print(current)
        visited.add(current)
        
        Time = Time +1
        for neighbor in graph[current]: 
            #print(neighbor)         
            if neighbor == goal:
                print(path)
                return path + ((current, neighbor)),Time
            if neighbor in visited:
                continue
            queue.append((neighbor, (path + current)))
            visited.add(neighbor) 
            print(queue)  
      
    
    return None



a,c=BFS("../INPUT/map1_lv1.txt")
print(a)







    

