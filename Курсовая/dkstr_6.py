import heapq

n, start_v, end_v = [int(x) for x in input().split()]
start_v -= 1
end_v -= 1

matrix = []
for _ in range(n):
    row = [int(x) for x in input().split()]
    matrix.append(row)

pq = [(0, start_v)]
dist = {start_v: 0}
history = {start_v: None}

while pq:
    curr_dist, curr = heapq.heappop(pq)
    if curr == end_v:
        break
    if curr_dist > dist.get(curr, float('inf')):
        continue
    for next_v in range(n):
        weight = matrix[curr][next_v]
        if weight >= 0 and curr != next_v:
            new_dist = curr_dist + weight
            if new_dist < dist.get(next_v, float('inf')):
                dist[next_v] = new_dist
                history[next_v] = curr
                heapq.heappush(pq, (new_dist, next_v))

if end_v not in dist:
    print(-1)
else:
    path = []
    curr = end_v
    while curr is not None:
        path.append(curr + 1)
        curr = history.get(curr)
    path.reverse()
    print(*path)
