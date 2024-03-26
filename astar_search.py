import heapq

class Node:
    def __init__(self, state, parent=None, action=None, path_cost=0):
        """Create a search tree Node, derived from a parent by an action."""
        self.state = state
        self.parent = parent
        self.action = action
        self.path_cost = path_cost
        self.depth = 0
        if parent:
            self.depth = parent.depth + 1

    def __repr__(self):
        return "<Node {}>".format(self.state)

    def __lt__(self, node):
        return self.state < node.state

    def expand(self, problem):
        """List the nodes reachable in one step from this node."""
        return [self.child_node(problem, action)
                for action in problem.actions(self.state)]

    def child_node(self, problem, action):
        next_state = problem.result(self.state, action)
        next_node = Node(next_state, self, action, problem.path_cost(self.path_cost, self.state, action, next_state))
        return next_node

    def solution(self):
        """Return the sequence of actions to go from the root to this node."""
        return [node.action for node in self.path()[1:]]

    def path(self):
        """Return a list of nodes forming the path from the root to this node."""
        node, path_back = self, []
        while node:
            path_back.append(node)
            node = node.parent
        return list(reversed(path_back))

    def __eq__(self, other):
        return isinstance(other, Node) and self.state == other.state

    def __hash__(self):
        return hash(self.state)
    
# 2D list that is a grid
class Problem:
    def __init__(self, grid, start, goal):
        self.grid = grid
        self.start = start
        self.goal = goal

    def actions(self, state):
        row, col = state
        possible_actions = []

        # check if cell above is valid move
        if row > 0 and self.grid[row - 1][col] != '#':
            # then move up
            possible_actions.append((-1, 0))
        # check if cell below is valid move
        if row < len(self.grid) - 1 and self.grid[row + 1][col] != '#':
            # then move down
            possible_actions.append((1, 0))
        # check if cell left is valid
        if col > 0 and self.grid[row][col - 1] != '#':
            # then move left
            possible_actions.append((0, -1))
        # check if cell right is valid
        if col < len(self.grid[0]) - 1 and self.grid[row][col + 1] != '#':
            # then move right
            possible_actions.append((0, 1))
        return possible_actions
    
    def result(self, state, action):
        return state[0] + action[0], state[1] + action[1]
    
    def goal_test(self, state):
        return state == self.goal
    
    def path_cost(self, cost_so_far, state1, action, state2):
        # we add 1 due to actions costing 1
        return cost_so_far + 1

# A* algorithm
def astar_search(problem):
    frontier = []

    # add start node to frontier + estimate from goal node
    heapq.heappush(frontier, (0 + heuristic(problem.start, problem.goal), Node(problem.start)))
    # store explored states into set
    explored = set()

    # loop until frontier is empty
    while frontier:
        # pop lowest cost node (with no priority)
        _, current_node = heapq.heappop(frontier)
        
        # check if current_node is goal state
        if problem.goal_test(current_node.state):
            return current_node
        
        # add current_node to explored 
        explored.add(current_node.state)

        # check for possible actions from current_state
        for action in problem.actions(current_node.state):
            # determine child
            child_state = problem.result(current_node.state, action)
            # create Noode object 
            child_node = Node(child_state, current_node, action, current_node.path_cost + 1)

            if child_state not in explored:
                # push to frontier: path cost of current + estimate to goal
                heapq.heappush(frontier, (child_node.path_cost 
                                          + heuristic(child_state, problem.goal),
                                          child_node))
                
    return None


# manhatan distance heuristic
def heuristic(state, goal):
    # absolute of rows + absolute of columns
    return abs(state[0] - goal[0]) + abs(state[1] - goal[1])