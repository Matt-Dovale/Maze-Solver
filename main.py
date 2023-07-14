

maze = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 1, 1, 1, 1, 1, 1],
    [1, 1, 0, 1, 1, 1, 1, 1, 1],
    [1, 1, 0, 1, 1, 1, 1, 1, 1],
    [1, 1, 0, 1, 1, 1, 1, 1, 1],
    [1, 1, 0, 1, 1, 1, 1, 1, 1],
    [1, 1, 0, 1, 1, 1, 1, 1, 1],
    [1, 1, 0, 1, 1, 1, 1, 1, 1],
    [1, 1, 0, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1]
]

start = (1, 1)
destination = (9, 6)

def dfs(current_pos, destination, visited):


    if current_pos == destination:
        return True
    
    if current_pos in visited or maze[current_pos[0]][current_pos[1]] == 1:
        return False
    
    visited.add(current_pos)

    for neighbor in get_neighbors(current_pos, maze):
        if dfs(neighbor, destination, visited):
            return True
    

def get_neighbors(position,maze): # assits in finding all the neighboring positions

    # movement: right, down, up, left
    movement = [(0,1), (1,0), (-1,0), (0,-1)]

    neighbors=[] # all possible neightbors
    row, col = position

    for dx, dy in movement:
        new_row =  row + dx
        new_col = col + dy

        if 0 <= new_row < len(maze) and 0 <= new_col < len(maze[0]):
            neighbors.append((new_row, new_col))

    return neighbors


visited = set()

if dfs(start, destination, visited):
    print("Path Found")
else:
    print("No path found")


