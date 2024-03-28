from pathfinder import Node, Problem, astar_search, heuristic

# example grid
grid = [
    ['S', '.', '.', '.', '#'],
    ['.', '#', '.', '.', '.'],
    ['.', '#', '.', '#', '.'],
    ['.', '.', '.', '#', '.'],
    ['#', '.', '.', '.', 'G']
]

# start state (row, col)
start = (0, 0)
# goal state (row, col)
goal = (4, 4)

# using problem instance
problem = Problem(grid, start, goal)

# call astar_search() function
solution_node = astar_search(problem)
# print out path
if solution_node:
    path = solution_node.solution()
    print("Path found: ", path)
else:
    print("No path found.")