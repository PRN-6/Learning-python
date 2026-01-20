grid = [
    ['S', '.', '.', 'X', '.'],
    ['.', 'X', '.', 'X', '.'],
    ['.', '.', '.', '.', '.'],
    ['X', '.', 'X', '.', 'G']
]

agent_pos = (0 ,0)

actions ={
    "UP" : (-1,0),
    "DOWN" : (1,0),
    "LEFT" : (0,-1),
    "RIGHT" : (0,1) 
}

def is_valid_move(grid,position):
    r,c = position
    if r < 0 or c < 0:
        return False
    
    if r >= len(grid) or c >= len(grid[0]):
        return False

    if grid[r][c] == 'X':
        return False

    if grid[r][c] == 'G':
        print("u have reached good")
    return True

print(is_valid_move(grid, (0, 1)))  # True
print(is_valid_move(grid, (0, 3)))  # False (X)
print(is_valid_move(grid, (-1, 0))) # False
print(is_valid_move(grid, (3, 4)))  # True (G)

