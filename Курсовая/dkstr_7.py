import heapq

n = int(input())
prices = [int(x) for x in input().split()]
m = int(input())

roads = {i: [] for i in range(n)}
for _ in range(m):
    u, v = [int(x) - 1 for x in input().split()]
    roads[u].append(v)
    roads[v].append(u)

pq = [(0, 0)]
dist = {0: 0}

while pq:
    curr_cost, curr = heapq.heappop(pq)
    if curr == n - 1:
        break
    if curr_cost > dist.get(curr, float('inf')):
        continue
    for next_v in roads[curr]:
        new_cost = curr_cost + prices[curr]
        if new_cost < dist.get(next_v, float('inf')):
            dist[next_v] = new_cost
            heapq.heappush(pq, (new_cost, next_v))

print(dist.get(n - 1, -1))
