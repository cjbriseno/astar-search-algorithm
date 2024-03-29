from tkinter import *
from astar_search import A_Star

grid = [
    ['.', '.', '.', '.', '.', '#', '.', '.', '.', '.'],
    ['.', '.', '#', '#', '.', '#', '.', '.', '.', '.'],
    ['.', '.', '#', '.', '.', '.', '.', '#', '.', '#'],
    ['.', '#', '.', '#', '#', '.', '.', '#', '.', '.'],
    ['.', '#', '.', '.', '#', '.', '.', '#', '#', '.'],
    ['.', '#', '.', '.', '#', '.', '.', '#', '.', '.'],
    ['.', '#', '.', '.', '.', '.', '.', '#', '.', '#'],
    ['.', '#', '.', '.', '.', '#', '.', '#', '.', '.'],
    ['.', '#', '.', '#', '#', '#', '#', '#', '.', '.'],
    ['.', '.', '.', '#', '.', '.', '.', '.', '.', '.']
]

# Prompt the user for start and goal coordinates
print("\n**** Welcome to step-by-step navigation ****\n")

for row in grid:
    for cell in row:
        print(cell, end=' ')
    print()

start_row = int(input("\nEnter row number for start state (0-9): "))
start_col = int(input("Enter column number for start state (0-9): "))
goal_row = int(input("Enter row number for goal state (0-9): "))
goal_col = int(input("Enter column number for goal state (0-9): "))

start1 = (start_row, start_col)
goal1 = (goal_row, goal_col)



print("\nRouting....\n")
a = A_Star(start1, goal1, grid)
path = a.pathfinder()
if path:
    for i in range(1, len(path)):
        prev_x, prev_y = path[i - 1]
        x, y = path[i]
        if x > prev_x:
            print("Step {0}: Down".format(i))
        elif x < prev_x:
            print("Step {0}: Up".format(i))
        elif y > prev_y:
            print("Step {0}: Right".format(i))
        elif y < prev_y:
            print("Step {0}: Left".format(i))