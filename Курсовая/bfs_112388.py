from collections import deque

rows, cols = [int(x) for x in input().split()]
maze = []
for _ in range(rows):
    row = [int(x) for x in input().split()]
    maze.append(row)

def get_cells(maze, r, c):
    res = []
    steps = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    for dr, dc in steps:
        new_r = r + dr
        new_c = c + dc
        if 0 <= new_r < rows and 0 <= new_c < cols:
            if maze[new_r][new_c] == 0:
                res.append((new_r, new_c))
    return res

start = (0, 0)
finish = (rows - 1, cols - 1)

queue = deque([(start, 0)])
visited = {start}
ans = -1

while queue:
    curr, dist = queue.popleft()
    if curr == finish:
        ans = dist
        break
    for next_cell in get_cells(maze, curr[0], curr[1]):
        if next_cell not in visited:
            visited.add(next_cell)
            queue.append((next_cell, dist + 1))

print(ans)
