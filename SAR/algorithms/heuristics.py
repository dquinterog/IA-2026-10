from typing import Any, Tuple
from algorithms import utils
from algorithms.problems import MultiSurvivorProblem


def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0


def manhattanHeuristic(state, problem):
    """
    The Manhattan distance heuristic.
    """
    goal = problem.goal
    return abs(state[0] - goal[0]) + abs(state[1] - goal[1])


def euclideanHeuristic(state, problem):
    """
    The Euclidean distance heuristic.
    """
    goal = problem.goal
    return ((state[0] - goal[0]) ** 2 + (state[1] - goal[1]) ** 2) ** 0.5


def survivorHeuristic(state: Tuple[Tuple, Any], problem: MultiSurvivorProblem):
    """
    Heuristic for the MultiSurvivorProblem.

    h(n) = Manhattan distance to the closest survivor
        + MST over the remaining survivors (using Manhattan distance).
    """
    position, survivors_grid = state
    survivors = survivors_grid.asList()

    if not survivors:
        return 0

    # Manhattan distance to the closest survivor
    min_to_any = min(abs(position[0]-sx) + abs(position[1]-sy) for (sx, sy) in survivors)

    # If only one survivor remains, that distance is the total lower bound
    if len(survivors) == 1:
        return min_to_any

    # --- MST using Prim's algorithm with Manhattan distance ---
    # Cache pairwise distances between survivors to avoid recomputation
    # (Cache key: sorted tuple of survivor positions)
    key = tuple(sorted(survivors))
    if key not in problem.heuristicInfo:
        # Precompute pairwise Manhattan distances
        pairDist = {}
        for i in range(len(key)):
            for j in range(i+1, len(key)):
                a = key[i]
                b = key[j]
                d = abs(a[0]-b[0]) + abs(a[1]-b[1])
                pairDist[(a, b)] = d
                pairDist[(b, a)] = d
        problem.heuristicInfo[key] = pairDist

    pairDist = problem.heuristicInfo[key]

    # Prim's algorithm
    unvisited = set(survivors)
    start = next(iter(unvisited))
    unvisited.remove(start)
    visited = {start}

    mst_cost = 0

    # For efficiency, store the best connection cost to the current tree
    best_edge = {u: abs(u[0]-start[0]) + abs(u[1]-start[1]) for u in unvisited}

    while unvisited:
        # Select the node with the smallest connection cost
        nxt = min(unvisited, key=lambda u: best_edge[u])
        mst_cost += best_edge[nxt]
        unvisited.remove(nxt)
        visited.add(nxt)

        # Update connection costs for remaining nodes
        for u in unvisited:
            # Use cached distance if available, otherwise compute Manhattan directly
            d = pairDist.get((nxt, u), abs(nxt[0]-u[0]) + abs(nxt[1]-u[1]))
            if d < best_edge[u]:
                best_edge[u] = d

    return min_to_any + mst_cost