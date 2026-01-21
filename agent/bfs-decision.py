from collections import queue
import time

# grrid environment

grid = [
    ['S', '.', '.', 'X', '.'],
    ['.', 'X', '.', 'X', '.'],
    ['.', '.', '.', '.', '.'],
    ['X', '.', 'X', '.', 'G']
]

# agent actions

actions={
    "UP":(-1,0),
    "DOWN":(1,0),
    "LEFT":(0,-1),
    "RIGHT":(0,1)
}

# check valid move

def is_valid_move(grid,position):
    r,c = position

    if r<0 or c<0:
        return False

    if r>=len(grid) or c>=len(grid[0]):
        return False
    
    if grid[r][c] == 'X':
        return False
    
    return True

# find start or goal

def find_start_goal(grid):
    for r in range(len(grid)):
        for c in range(len(gird[0])):
            if grid[r][c] == target:
                return (r,c)
            

# bfs desision making