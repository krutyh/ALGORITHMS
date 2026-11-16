from collections import deque

n = int(input())
cave = []
start = None

for z in range(n):
    input()
    level = []
    for r in range(n):
        row = list(input().strip())
        if 'S' in row:
            start = (z, r, row.index('S'))
        level.append(row)
    cave.append(level)

def get_cells(z, r, c):
    res = []
    steps = [(-1, 0, 0), (1, 0, 0), (0, -1, 0), (0, 1, 0), (0, 0, -1), (0, 0, 1)]
    for dz, dr, dc in steps:
        nz = z + dz
        nr = r + dr
        nc = c + dc
        if 0 <= nz < n and 0 <= nr < n and 0 <= nc < n:
            if cave[nz][nr][nc] != '#':
                res.append((nz, nr, nc))
    return res

queue = deque([(start, 0)])
visited = {start}
ans = 0

while queue:
    curr, dist = queue.popleft()
    if curr[0] == 0:
        ans = dist
        break
    for next_cell in get_cells(curr[0], curr[1], curr[2]):
        if next_cell not in visited:
            visited.add(next_cell)
            queue.append((next_cell, dist + 1))

print(ans)
