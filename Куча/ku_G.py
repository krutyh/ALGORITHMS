import sys
import heapq

input_data = sys.stdin.read().split()

if input_data:
    n = int(input_data[0])
    populations = [int(x) for x in input_data[1:n+1]]
    
    events = []
    for i in range(n):
        f = populations[i]
        t_next = max(1000 - f, 1)
        heapq.heappush(events, (t_next, i, f))
        
    igor_pos = 0
    igor_time = 0
    
    while events:
        t_birth, idx, f = heapq.heappop(events)
        
        distance = abs(idx - igor_pos)
        if igor_time + distance <= t_birth:
            igor_time = t_birth
            igor_pos = idx
            
            f_new = f + 1
            t_next_birth = t_birth + max(1000 - f_new, 1)
            heapq.heappush(events, (t_next_birth, idx, f_new))
        else:
            print(t_birth)
            break
