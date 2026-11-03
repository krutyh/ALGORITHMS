import sys
import heapq

input_data = sys.stdin.read().split()

if input_data:
    n = int(input_data[0])
    arr = [int(x) for x in input_data[1:n+1]]
    
    heapq.heapify(arr)
    
    total_cost = 0.0
    
    while len(arr) > 1:
        first = heapq.heappop(arr)
        second = heapq.heappop(arr)
        
        current_sum = first + second
        total_cost += current_sum * 0.05
        
        heapq.heappush(arr, current_sum)
        
    print(f"{total_cost:.2f}")
