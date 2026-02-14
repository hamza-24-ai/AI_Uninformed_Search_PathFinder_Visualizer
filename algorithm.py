import collections as cl
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

def reconstruct_path(parent,start,goal):
    path = []
    curr = goal
    while curr != start:
        path.append(curr)
        curr = parent[curr]
    return path[::-1]