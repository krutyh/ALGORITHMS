import sys
import heapq

input_data = sys.stdin.read().split()

if input_data:
    n = int(input_data[0])
    
    cargo = []
    idx = 1
    for _ in range(n):
        t = int(input_data[idx])
        l = int(input_data[idx+1])
        cargo.append((t, t + l))
        idx += 2
        
    cargo.sort(key=lambda x: x[0])
    
    machines = []
    
    for t_start, t_end in cargo:
        if machines and machines[0] <= t_start:
            heapq.heappop(machines)
        heapq.heappush(machines, t_end)
        
    print(len(machines))
