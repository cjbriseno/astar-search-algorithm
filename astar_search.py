
from queue import PriorityQueue

class Node(object):
    # constructor 
    def __init__(self, state, parent, start = 0, goal = 0):
        self.state = state
        self.parent = parent
        # empty list for children nodes
        self.children = []
        # placeholder
        self.x = 0
        # check if parent is not None
        if parent:
            # if node has parent: copy parents start to current node
            self.start = parent.start
            # assign goal of parent node to goal of current node
            self.goal = parent.goal
            # create copy of parent node path & assign to current node path
            self.path = parent.path[:]
            # update path from start node to current node
            self.path.append(state)
        # if parent is NONE
        else:
            # set path of current node to state list
            self.path = [state]
            self.start = start
            self.goal = goal

    # -- these are placeholders for Grid --
    def heuristic(self):
        pass

    def create_child(self):
        pass

# grid based pathfinding
class Grid(Node):
    # constructor
    def __init__(self, state, parent, start = 0, goal = 0, grid = None):
        # call constructor of Node class, initializes Grid class instance
        super(Grid, self).__init__(state, parent, start, goal)
        # calculates heuristic of current state
        self.x = self.heuristic()
        # save grid to use later
        self.grid = grid

    # uses manhattan distance 
    def heuristic(self):
        # base case: if we are at the goal
        if self.state == self.goal:
            return 0
        # calculate the distance from current state to goal
        # the sum of absolute differnces
        return abs(self.state[0] - self.goal[0]) + abs(self.state[1] - self.goal[1])

    # create child states from current state (what is next?)
    def create_child(self):
        # base case: check if children list is empty
        if not self.children:
            # loop through tuple of possible moves
            # (0,1) = right, (0,-1) = left
            # (1,0) = down, (-1,0) = up
            for i in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                # calculate row & column index of children
                row = self.state[0] + i[0]
                col = self.state[1] + i[1]
                # check if node is within grid & not #
                if 0 <= row < len(self.grid) and 0 <= col < len(self.grid[0]) and self.grid[row][col] != '#':
                    # new node that is availible
                    new_child = (row, col)
                    # 
                    child = Grid(new_child, self, grid=self.grid)
                    self.children.append(child)

class A_Star:
    def __init__(self, start, goal, grid):
        self.start = start
        self.goal = goal
        self.grid = grid
        self.path = []
        self.visited = []
        self.priorityQueue = PriorityQueue()

    def astar_search(self):
        start_state = Grid(self.start, 0, self.start, self.goal, self.grid)

        count = 0
        self.priorityQueue.put((0, count, start_state))
        while not self.path and self.priorityQueue.qsize():
            possible_child = self.priorityQueue.get()[2]
            if possible_child.state == self.goal:
                self.path = possible_child.path
                break
            possible_child.create_child()
            self.visited.append(possible_child.state)
            for child in possible_child.children:
                if child.state not in self.visited:
                    count += 1
                    self.priorityQueue.put((child.x, count, child))
        if not self.path:
            print("Goal is not possible!" + str(self.goal))
        return self.path
