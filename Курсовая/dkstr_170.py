import heapq

n = int(input())
start_v, end_v = [int(x) for x in input().split()]
r = int(input())

buses = {i: [] for i in range(1, n + 1)}
for _ in range(r):
    u, t_start, v, t_end = [int(x) for x in input().split()]
    buses[u].append((t_start, v, t_end))

pq = [(0, start_v)]
min_time = {start_v: 0}

while pq:
    curr_time, curr_v = heapq.heappop(pq)
    if curr_v == end_v:
        break
    if curr_time > min_time.get(curr_v, float('inf')):
        continue
    for t_start, next_v, t_end in buses[curr_v]:
        if t_start >= curr_time:
            if t_end < min_time.get(next_v, float('inf')):
                min_time[next_v] = t_end
                heapq.heappush(pq, (t_end, next_v))

print(min_time.get(end_v, -1))
