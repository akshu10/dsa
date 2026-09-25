from typing import Optional
from pprint import pprint
from collections import deque

"""
Graph Algorithms
Pseudocode: 
    Pick a node to start node 
    Prioritize depth
    Go to neighbours and their depths. 
    If no neighbours for a particular node we backtrack return back to starting node.

    
    The recursive one still uses a Stack.

Important things to have for Traversals: (keeping track of seen nodes)
    A seen/visited node track. Use Sets (seen sets allow us to avoid CYCLES.)
"""


# def recursive_depth_first_search(
#     graph: dict[int, list[int]], node: int, visited: set[int], order: list[int]
# ) -> list[int]:
#     pass


"""
Pseudocode: 
    Uses the same seen/visited Set as well
    Uses a stack to keep track of what node we are visiting.

    Insert start/source node into stack 
    while stack is not empty:
        pop node off (it aways LIFO for sets)
        if neighbour not in set() 
        push all neighbouring nodes to the stack 

"""


def iterative_depth_first_search(graph: dict[int, list[int]], start: int) -> list[int]:
    seen, path, return_list = set(), [], []

    path = [start]

    while len(path) > 0:
        current_element = path.pop()

        # prevents visiting the same vertex again.
        if current_element in seen:
            continue
        else:
            # Add current vertex to the return list/seen set to prevent revisiting
            seen.add(current_element)
            return_list.append(current_element)

        # Get current vertexes neighbours
        neighbours = graph[current_element]

        for neighbour in neighbours:
            # If neighbour not visited then add it to the iterative stack. (so it can be visited)
            if neighbour not in seen:
                path.append(neighbour)

    return return_list


"""
Pseudocode:
    Uses the same seen/visited Set as well
    Uses a queue (FIFO) instead of a stack, so it visits level by level (prioritizes breadth).

    Insert start/source node into queue
    while queue is not empty:
        pop node off the front
        if neighbour not in set()
        push all neighbouring nodes to the back of the queue

"""


def iterative_breadth_first_search(
    graph: dict[int, list[int]], start: int
) -> list[int]:
    seen, queue, return_list = {start}, deque([start]), []

    while queue:
        current_element = queue.popleft()
        return_list.append(current_element)

        # neighbours
        neighbours = graph[current_element]

        for neighbour in neighbours:
            if neighbour not in seen:
                seen.add(neighbour)
                queue.append(neighbour)

    return return_list


# ---------------------------------------------------------------------------
# Tests: run `python3 src/python/graphs.py`
# PASS = visits exactly the reachable nodes, once each, starting at `start`.
# DFS-order = whether the order is a genuine depth-first order (goes deep
# before backtracking). Informational only; different valid DFS runs can
# produce different orders.
# ---------------------------------------------------------------------------
def _is_dfs_order(graph, order):
    seen, path = set(), []
    for node in order:
        while path and node not in graph[path[-1]]:
            if any(n not in seen for n in graph[path[-1]]):
                return (
                    False  # jumped away while current node still had unvisited children
                )
            path.pop()
        if path == [] and seen:
            return False
        seen.add(node)
        path.append(node)
    return True


TEST_CASES = [
    # (name, graph, start, expected reachable set)
    ("single node", {0: []}, 0, {0}),
    ("linear chain", {0: [1], 1: [2], 2: [3], 3: []}, 0, {0, 1, 2, 3}),
    (
        "directed, from 3",
        {0: [1], 1: [2], 2: [], 3: [4, 6, 7], 4: [2, 5], 5: [2], 6: [], 7: []},
        3,
        {3, 4, 6, 7, 2, 5},
    ),
    (
        "directed, from 0 (can't reach 3's side)",
        {0: [1], 1: [2], 2: [], 3: [4, 6, 7], 4: [2, 5], 5: [2], 6: [], 7: []},
        0,
        {0, 1, 2},
    ),
    ("diamond (shared child)", {0: [1, 2], 1: [3], 2: [3], 3: []}, 0, {0, 1, 2, 3}),
    (
        # 1 is a child of both 0 and 4. True DFS must visit 1 right after 4.
        "shared child deep in the tree",
        {0: [1, 2], 1: [], 2: [3, 4], 3: [], 4: [1]},
        0,
        {0, 1, 2, 3, 4},
    ),
    ("cycle", {0: [1], 1: [2], 2: [0]}, 0, {0, 1, 2}),
    ("self loop", {0: [0, 1], 1: []}, 0, {0, 1}),
    (
        "undirected (edges both ways)",
        {0: [1, 2], 1: [0, 3], 2: [0, 3], 3: [1, 2]},
        0,
        {0, 1, 2, 3},
    ),
    (
        "disconnected",
        {0: [1], 1: [0], 2: [3], 3: [2]},
        2,
        {2, 3},
    ),
    (
        "deep chain (2000 nodes)",
        {i: [i + 1] for i in range(1999)} | {1999: []},
        0,
        set(range(2000)),
    ),
]


IMPLEMENTATIONS = {
    # "recursive": lambda g, s: recursive_depth_first_search(g, s, set(), []),
    "iterative": iterative_depth_first_search,
    # "iterative_v2": iterative_depth_first_search_v2,
    "bfs": iterative_breadth_first_search,
}


def _short(value, limit: int = 10):
    """Keep huge test inputs (like the 2000-node chain) from flooding the terminal."""
    if value is not None and len(value) > limit:
        items = list(value.items() if isinstance(value, dict) else value)[:limit]
        return f"{dict(items) if isinstance(value, dict) else items} ... ({len(value)} total)"
    return value


def run_tests(impl_name: str, case_number: Optional[int] = None) -> None:
    dfs = IMPLEMENTATIONS[impl_name]
    cases = list(enumerate(TEST_CASES, start=1))
    if case_number is not None:
        cases = [cases[case_number - 1]]

    print(f"\n=== {impl_name} ===")
    passed = 0
    for number, (name, graph, start, expected) in cases:
        # Header first, so your print() output shows up under the right case
        print(f"\n--- #{number} {name} ---")
        try:
            result = dfs(graph, start)
        except RecursionError:
            print(
                "  Result:          ERROR  RecursionError (Python's default limit is ~1000 frames)"
            )
            continue

        problems = []
        if result is None:
            problems.append("function returned None (missing `return`?)")
        else:
            extra = set(result) - expected
            missing = expected - set(result)
            dupes = sorted({n for n in result if result.count(n) > 1})
            if extra:
                problems.append(
                    f"visited {sorted(extra)}, which can't be reached from {start}"
                )
            if missing:
                problems.append(f"never visited {sorted(missing)}")
            if dupes:
                problems.append(f"visited {dupes} more than once")
            if result and result[0] != start:
                problems.append(
                    f"first node is {result[0]}, should be the start node {start}"
                )
        ok = not problems
        passed += ok

        print(f"  Input:           graph={_short(graph)}, start={start}")
        print(f"  Output:          {_short(result)}")
        print(
            f"  Expected output: {_short(sorted(expected))}  (these nodes, each once, starting with {start}, any {'BFS' if impl_name == 'bfs' else 'DFS'} order)"
        )
        if ok and impl_name == "bfs":
            print("  Result:          PASS")
        elif ok:
            depth_first = _is_dfs_order(graph, result)
            print(
                f"  Result:          PASS  (DFS order: {'yes' if depth_first else 'no, not depth-first'})"
            )
        else:
            print("  Result:          FAIL")
            for problem in problems:
                print(f"    Why: {problem}")
    print(f"  {passed}/{len(cases)} passed")


# Usage:
#   python3 src/python/graphs.py                -> all functions, all cases
#   python3 src/python/graphs.py iterative      -> just the iterative DFS
#   python3 src/python/graphs.py recursive 6    -> just case #6 on recursive DFS
if __name__ == "__main__":
    import sys

    names = [sys.argv[1]] if len(sys.argv) > 1 else list(IMPLEMENTATIONS)
    case_number = int(sys.argv[2]) if len(sys.argv) > 2 else None
    for impl_name in names:
        run_tests(impl_name, case_number)
