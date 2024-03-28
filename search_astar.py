# this is new file
from queue import PriorityQueue

# this class is used for steps used in A* algorithm
class Node(object):
    def __init__(self, state, parent, start = 0, goal = 0):
        self.children = []
        self.parent = parent
        self.state = state
        self.x = 0
        if parent:
            self.start = parent.start
            self.goal = parent.goal
            self.path = parent.path[:]
            self.path.append(state)
        else:
            self.path = [state]
            self.start = start
            self.goal = goal

    def heuristic(self):
        pass

    def create_child(self):
        pass


class Grid(Node):
    def __init__(self, state, parent, start = 0, goal = 0):
        super(Grid, self).__init__(state, parent, start, goal)
        self.x = self.heuristic()

    def heuristic(self):
        if self.state == self.goal:
            return 0
        return abs(self.state[0] - self.goal[0]) + abs(self.state[1] - self.goal[1])
    
    def create_child(self):
        if not self.children:
            for i in [(0,1), (1,-1), (1,0), (-1,0)]:
                row = self.state[0] + i[0]
                col = self.state[1] + i[1]
                if 0 <= (row < len(self.goal)) and 0 <= (col < len(self.goal[0])
                                                         and self.goal[row][col] != '#'):
                    new_child = (row, col)
                    child = Grid(new_child, self)
                    self.children.append(child)

class A_Star:
    def __init__(self, start, goal, grid):
        self.path = []
        self.visited = []
        self.priorityQueue = PriorityQueue()
        self.start = start
        self.goal = goal
        self.grid = grid

    def astar_serach(self):
        start_state = Grid(self.start, 0, self.start, self.goal)
        count = 0
        self.priorityQueue.put((0, count, start_state))
        while(not self.path and self.priorityQueue.qsize()):
            possible_child = self.priorityQueue.get()[2]
            possible_child.create_child()
            self.visited.append(possible_child.value)
            for child in possible_child.children:
                if child.value not in self.visited:
                    count += 1
                    if not child.x:
                        self.path = child.path
                        break
                    self.priorityQueue.put((child.x, count, child))
        if not self.path:
            print("-- GOAL STATE CANNOT BE REACHED: " + str(self.goal), " --")
        return self.path