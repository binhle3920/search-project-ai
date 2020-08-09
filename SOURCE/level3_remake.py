import data

#all pos represent as (x, y)
#additional function
def scan_around(pacman_pos):
    #this function will return food pos and monster pos, if not, return [] and []
    #if yes, return [(x1,y1), (x2,y2)] and [(x1,y1), (x2,y2)]
    return [], []
def pacman_moveable_pos(pacman_pos, monster_pos):
    #if monster pos is not empty, using manhattan to find calculate distance pacman and monster
    #find rational way pos for pacman move (Ex: manhattn to monster > 2) 
    #return list of moveable pos
    return []
def move_directly_to_food(pacman_pos, food_pos, monster_pos):
    #find any path to go direct to food in 8x3 size
    #return False if there is no path
    #else return path
    return []
def running_to_food(pacman_pos, food_pos, monster_pos):
    #assume that food is always getable
    #using A* to search for food, every step we will scan again
    #return path, list of new food found, index of food eaten
    return [], [], 0
def monster_move_random(map, monster_path):
    #do everything you want to make monster move random around it initial state
    #return new map with monster pos change and path of each monster move
    return map, monster_path


#using dfs to search for food when there is no food
def food_searching(map, pacman_pos, explored, path, monster_path = []):
    explored.append(pacman_pos)
    map, monster_path = monster_move_random(map, monster_path)
    food_pos, monster_pos = scan_around(pacman_pos)

    if food_pos:
        return [pacman_pos, food_pos, monster_pos, path, explored, monster_path]

    for node in pacman_moveable_pos(pacman_pos, monster_pos):
        if node not in explored:
            path.append(node)
            result = food_searching(map, node, explored, path, monster_path)
            if len(result) == 1:
                map, monster_path = monster_move_random(map, monster_path)
                path.append(pacman_pos)
            elif len(result) != 1:
                return result
                
    return path, monster_path

#main function
def pacman_running(map, pacman_pos):
    path = [pacman_pos]
    monster_path = []
    result = food_searching(map, pacman_pos, explored = [], path = [pacman_pos], monster_path = [])
    
    while len(result) != 2:
        pacman_pos, food_pos, monster_pos, add_path, explored, add_monster_path = result[:]
        path.append(add_path)
        monster_path.append(add_monster_path)

        while food_pos:
            food_path, more_food, food_eat = running_to_food(pacman_pos, food_pos, monster_pos)

            food_pos.append(more_food)
            path.append(food_path)
            pacman_pos = food_path[-1]

            food_pos.pop(food_eat) #pop the food eaten out of food list
            map[food_pos[food_eat][0]][food_pos[food_eat][0][1]] = 0 #remove on map

        result = food_searching(map, pacman_pos, explored, path)

    return path.append(result[0]), monster_path.append(result[1])

def level3_running(path):
    map, size, pacman_pos = data.get_maze(path)
    return pacman_running(map, pacman_pos)
    