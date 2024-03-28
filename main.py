from astar_search import A_Star

start1 = (0, 0)
goal1 = (3, 2)
grid = [
    ['.', '.', '.', '.', '.'],
    ['.', '.', '#', '#', '.'],
    ['.', '.', '#', '.', '.'],
    ['.', '#', '.', '.', '.'],
    ['.', '#', '.', '.', '.']
]
print("Starting....")
a = A_Star(start1, goal1, grid)
path = a.astar_search()
if path:
    for i in range(len(path)):
        print("{0}){1}".format(i, path[i]))
