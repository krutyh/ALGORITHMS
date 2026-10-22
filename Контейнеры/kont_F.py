from collections import deque

n, k = map(int, input().split())
arr = list(map(int, input().split()))

d = deque()

for i in range(n):
    if d and d[0] <= i - k:
        d.popleft()

    while d and arr[d[-1]] >= arr[i]:
        d.pop()

    d.append(i)
    
    if i >= k - 1:
        print(arr[d[0]])
