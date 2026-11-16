from collections import deque

n = int(input())
x1, y1 = [int(x) for x in input().split()]
x2, y2 = [int(x) for x in input().split()]

start = (x1, y1)
finish = (x2, y2)

def get_knight_cells(r, c):
    res = []
    steps = [(-2, -1), (-2, 1), (-1, -2), (-1, 2), (1, -2), (1, 2), (2, -1), (2, 1)]
    for dr, dc in steps:
        new_r = r + dr
        new_c = c + dc
        if 1 <= new_r <= n and 1 <= new_c <= n:
            res.append((new_r, new_c))
    return res

queue = deque([start])
visited = {start}
history = {start: None}

while queue:
    curr = queue.popleft()
    if curr == finish:
        break
    for next_cell in get_knight_cells(curr[0], curr[1]):
        if next_cell not in visited:
            visited.add(next_cell)
            history[next_cell] = curr
            queue.append(next_cell)

path = []
curr = finish
while curr is not None:
    path.append(curr)
    curr = history.get(curr)
path.reverse()

print(len(path) - 1)
for cell in path:
    print(cell[0], cell[1])
