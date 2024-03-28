import heapq
import itertools

class PuzzleNode:
    goal_state = (1, 2, 3, 4, 5, 6, 7, 8, 0)
    
    def __init__(self, state, parent=None, move=None, cost=0):
        self.state = state
        self.parent = parent
        self.move = move
        self.depth = 0
        self.cost = cost
        if parent:
            self.depth = parent.depth + 1
            
    def __lt__(self, other):
        return (self.depth + self.cost) < (other.depth + other.cost)  
    
    def __eq__(self, other):
        return self.state == other.state
    
    def __hash__(self):
        return hash(self.state)
    
    def get_children(self):
        children = []
        idx = self.state.index(0)
        for move in self.get_possible_moves(idx):
            new_state = list(self.state)
            new_state[idx], new_state[move] = new_state[move], new_state[idx]
            children.append(PuzzleNode(tuple(new_state), self, move, 1)) 
        return children
    
    def get_possible_moves(self, idx):
        moves = []
        if idx not in (0, 1, 2):
            moves.append(idx - 3)
        if idx not in (0, 3, 6):
            moves.append(idx - 1)
        if idx not in (2, 5, 8):
            moves.append(idx + 1)
        if idx not in (6, 7, 8):
            moves.append(idx + 3)
        return moves
    
    def is_goal_state(self):
        return self.state == self.goal_state
    
    def get_solution_path(self):
        path = []
        node = self
        while node:
            path.append(node)
            node = node.parent
        return reversed(path)

def heuristic(state):
    distance = 0
    for i in range(9):
        if state[i] != 0:
            distance += abs(i % 3 - (state[i] - 1) % 3) + abs(i // 3 - (state[i] - 1) // 3)
    return distance

def a_star_search(initial_state):
    start_node = PuzzleNode(initial_state)
    if start_node.is_goal_state():
        return start_node.get_solution_path()
    frontier = []
    heapq.heappush(frontier, start_node)
    explored = set()
    while frontier:
        node = heapq.heappop(frontier)
        if node.is_goal_state():
            return node.get_solution_path()
        explored.add(node)
        for child in node.get_children():
            if child not in explored:
                child.cost += heuristic(child.state)
                heapq.heappush(frontier, child)

def print_solution_path(solution_path):
    print("Solution Steps:")
    cost = 0  # Initialize cost
    for step, node in enumerate(solution_path):
        print(f"Step {step}: Move {node.move}")
        print_state(node.state)
        print()
        cost += node.cost
    print("Total Cost:", cost) 

def print_state(state):
    for i in range(0, 9, 3):
        print(state[i:i+3])

if __name__ == "__main__":
    initial_state = tuple(map(int, input("Enter initial state of the puzzle (use 0 for the empty tile): ").split()))
    solution_path = a_star_search(initial_state)
    print_solution_path(solution_path)
