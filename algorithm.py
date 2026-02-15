import collections as cl
from collections import deque
import heapq

def bfs(grid,start,goal,callback):
    # Order Up,Right,Bottom,Bottom_Right,Left,Top_Left
    directions = [(-1,0), (0,1), (1,0),(1,1), (0,-1), (-1,-1)]

    rows, cols = grid.shape
    queue = cl.deque([start])
    visited = set()
    visited.add(start)
    parent = {}

    while queue:
        curr = queue.popleft()

        if curr == goal:
            return reconstruct_path(parent, start, goal)

        for dr, dc in directions:
            r,c = curr[0]+dr, curr[1]+dc

            if 0 <= r < rows and 0 <= c < cols and grid[r][c] != 1 and (r,c) not in visited:
                visited.add((r,c))
                parent[(r, c)] = curr

                if (r,c) != goal:
                    grid[r][c] = 4
                callback(grid)

                queue.append((r, c))

    return None


def dfs(grid,start,goal,callback):

    directions = [(-1,0),(0,1),(1,0),(1,1),(0,-1),(-1,-1)]
    rows,cols = grid.shape
    stack = [start]
    visited = {start}
    parent = {start: None}

    while stack:
        curr = stack.pop()

        if curr == goal:
            return reconstruct_path(parent,start,goal)

        for dr,dc in reversed(directions):
            r,c = curr[0]+dr, curr[1]+dc

            if 0<=r<rows and 0<=c<cols and grid[r][c] != 1 and (r,c) not in visited:
                visited.add((r,c))
                parent[(r,c)] = curr

                if(r,c) != goal:
                    grid[r][c] = 4

                callback(grid)
                stack.append((r,c))

                if (r,c)==goal:
                    break

    return None


def ucs(grid, costs, start, goal, callback):
    directions = [(-1, 0), (0, 1), (1, 0), (1, 1), (0, -1), (-1, -1)]
    rows, cols = grid.shape

    pq = [(0, start)]
    min_cost = {start: 0}
    parent = {start: None}
    visited = set()

    while pq:
        current_priority_cost, curr = heapq.heappop(pq)

        if curr == goal:
            return reconstruct_path(parent, start, goal)

        if curr in visited:
            continue
        visited.add(curr)

        for dr, dc in directions:
            r, c = curr[0] + dr, curr[1] + dc

            if 0 <= r < rows and 0 <= c < cols and grid[r][c] != 1:

                step_cost = costs[r, c]
                new_cost = current_priority_cost + step_cost

                if (r, c) not in min_cost or new_cost < min_cost[(r, c)]:
                    min_cost[(r, c)] = new_cost
                    parent[(r, c)] = curr

                    if (r, c) != goal:
                        grid[r][c] = 4  # Blue exploration

                    callback(grid)
                    heapq.heappush(pq, (new_cost, (r, c)))
    return None


def dls(grid, start, goal, limit, callback):

    directions = [(-1, 0), (0, 1), (1, 0), (1, 1), (0, -1), (-1, -1)]

    stack = [(start, 0)]
    visited = {start: 0}
    parent = {start: None}

    while stack:
        curr, depth = stack.pop()

        if curr == goal:
            return reconstruct_path(parent, start, goal)

        if depth < limit:
            for dr, dc in reversed(directions):
                r, c = curr[0] + dr, curr[1] + dc

                if 0 <= r < len(grid) and 0 <= c < len(grid[0]) and grid[r][c] != 1:
                    # Depth check for visiting
                    if (r, c) not in visited or depth + 1 < visited[(r, c)]:
                        visited[(r, c)] = depth + 1
                        parent[(r, c)] = curr

                        if (r, c) != goal:
                            grid[r][c] = 4

                        callback(grid)
                        stack.append(((r, c), depth + 1))
    return None


def iddfs(grid, start, goal, max_limit, callback):
    # Iteratively increase the limit
    for limit in range(max_limit):
        print(f"Searching with Limit: {limit}")

        temp_grid = grid.copy()

        path = dls(temp_grid, start, goal, limit, callback)

        if path:

            return path

    return None


def bidirectional_search(grid, start, goal, callback):
    directions = [(-1, 0), (0, 1), (1, 0), (1, 1), (0, -1), (-1, -1)]
    rows, cols = grid.shape

    # Forward Search Setup
    q_f = deque([start])
    parent_f = {start: None}
    visited_f = {start}

    # Backward Search Setup
    q_b = deque([goal])
    parent_b = {goal: None}
    visited_b = {goal}

    while q_f and q_b:
        # 1. Forward Step
        curr_f = q_f.popleft()
        for dr, dc in directions:
            r, c = curr_f[0] + dr, curr_f[1] + dc
            if 0 <= r < rows and 0 <= c < cols and grid[r][c] != 1:
                if (r, c) not in visited_f:
                    visited_f.add((r, c))
                    parent_f[(r, c)] = curr_f
                    if (r, c) != goal and (r, c) != start:
                        grid[r][c] = 4  # Blue exploration
                    q_f.append((r, c))

                    # Intersection Check: Kya ye Backward search ne pehle hi dekha hua hai?
                    if (r, c) in visited_b:
                        callback(grid)
                        return assemble_bidirectional_path(parent_f, parent_b, (r, c), start, goal)

        # 2. Backward Step
        curr_b = q_b.popleft()
        for dr, dc in directions:
            r, c = curr_b[0] + dr, curr_b[1] + dc
            if 0 <= r < rows and 0 <= c < cols and grid[r][c] != 1:
                if (r, c) not in visited_b:
                    visited_b.add((r, c))
                    parent_b[(r, c)] = curr_b
                    if (r, c) != goal and (r, c) != start:
                        grid[r][c] = 4
                    q_b.append((r, c))

                    # Intersection Check: Kya ye Forward search ne pehle hi dekha hua hai?
                    if (r, c) in visited_f:
                        callback(grid)
                        return assemble_bidirectional_path(parent_f, parent_b, (r, c), start, goal)

        callback(grid)

    return None


def assemble_bidirectional_path(parent_f, parent_b, meeting_node, start, goal):
    # Path from start to meeting point
    path_f = []
    curr = meeting_node
    while curr is not None:
        path_f.append(curr)
        curr = parent_f[curr]
    path_f = path_f[::-1]

    # Path from meeting point to goal
    path_b = []
    curr = parent_b[meeting_node]  # Meeting node ka parent Backward side par
    while curr is not None:
        path_b.append(curr)
        curr = parent_b[curr]

    return path_f + path_b

def reconstruct_path(parent,start,goal):
    path = []
    curr = goal
    while curr != start:
        path.append(curr)
        curr = parent[curr]
    return path[::-1]