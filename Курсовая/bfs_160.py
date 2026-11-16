from collections import deque

n = int(input())
matrix = []
for _ in range(n):
    row = [int(x) for x in input().split()]
    matrix.append(row)

start_v, end_v = [int(x) - 1 for x in input().split()]

def get_path(history, start, finish):
    path = []
    curr = finish
    while curr is not None:
        path.append(curr + 1)
        curr = history.get(curr)
    path.reverse()
    return path

queue = deque([start_v])
visited = {start_v}
history = {start_v: None}
found = False

while queue:
    curr = queue.popleft()
    if curr == end_v:
        found = True
        break
    for next_v in range(n):
        if matrix[curr][next_v] == 1 and next_v not in visited:
            visited.add(next_v)
            history[next_v] = curr
            queue.append(next_v)

if not found:
    print(-1)
else:
    res = get_path(history, start_v, end_v)
    print(len(res) - 1)
    if len(res) > 1:
        print(*res)
