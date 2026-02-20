from algorithms.problems import SearchProblem
import algorithms.utils as utils
from world.game import Directions
from algorithms.heuristics import nullHeuristic


def tinyHouseSearch(problem: SearchProblem):
    """
    Returns a sequence of moves that solves tinyHouse. For any other building, the
    sequence of moves will be incorrect, so only use this for tinyHouse.
    """
    s = Directions.SOUTH
    w = Directions.WEST
    return [s, s, w, s, w, w, s, w]


def depthFirstSearch(problem: SearchProblem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print("Start:", problem.getStartState())
    print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    print("Start's successors:", problem.getSuccessors(problem.getStartState()))
    """
    stack = utils.Stack()
    visited = set()
    stack.push((problem.getStartState(), []))
    
    while not stack.isEmpty():
        state, actions = stack.pop()
        #prints to prove the states and the actions
        #print("Current state:", state)
        #print("Actions to reach current state:", actions)
        if problem.isGoalState(state):
            return actions
        
        if state not in visited:
            visited.add(state)
            for successor, action, _ in problem.getSuccessors(state):
                new_actions = actions + [action]
                stack.push((successor, new_actions))
    return []  # Return an empty list if no solution is found

def breadthFirstSearch(problem: SearchProblem):
    """
    Search the shallowest nodes in the search tree first.
    """
    queue = utils.Queue()
    visited = set()
    queue.push((problem.getStartState(), []))
    
    while not queue.isEmpty():
        state, actions = queue.pop()
        if problem.isGoalState(state):
            return actions
        
        if state not in visited:
            visited.add(state)
            for successor, action, _ in problem.getSuccessors(state):
                new_actions = actions + [action]
                queue.push((successor, new_actions))
    return []  # Return an empty list if no solution is found


def uniformCostSearch(problem: SearchProblem):
    """
    Search the node of least total cost first.
    """
    priority_queue = utils.PriorityQueue()
    visited = set()
    priority_queue.push((problem.getStartState(), [], 0), 0)
    
    while not priority_queue.isEmpty():
        state, actions, cost = priority_queue.pop()
        if problem.isGoalState(state):
            return actions
        
        if state not in visited:
            visited.add(state)
            for successor, action, step_cost in problem.getSuccessors(state):
                new_actions = actions + [action]
                new_cost = cost + step_cost
                priority_queue.push((successor, new_actions, new_cost), new_cost)
    return []  # Return an empty list if no solution is found


def aStarSearch(problem: SearchProblem, heuristic=nullHeuristic):
    """
    Search the node that has the lowest combined cost and heuristic first.
    """
    priority_queue = utils.PriorityQueue()
    visited = set()
    start_state = problem.getStartState()
    priority_queue.push((start_state, [], 0), heuristic(start_state, problem))
    
    while not priority_queue.isEmpty():
        state, actions, cost = priority_queue.pop()
        if problem.isGoalState(state):
            return actions
        
        if state not in visited:
            visited.add(state)
            for successor, action, step_cost in problem.getSuccessors(state):
                new_actions = actions + [action]
                new_cost = cost + step_cost
                priority_queue.push((successor, new_actions, new_cost), new_cost + heuristic(successor, problem))
    return []  # Return an empty list if no solution is found


# Abbreviations (you can use them for the -f option in main.py)
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
