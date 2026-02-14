import collections as cl

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


def reconstruct_path(parent,start,goal):
    path = []
    curr = goal
    while curr != start:
        path.append(curr)
        curr = parent[curr]
    return path[::-1]