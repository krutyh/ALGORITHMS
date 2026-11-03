import sys
import heapq

lines = sys.stdin.read().splitlines()

heap = []

for line in lines:
    if not line:
        continue
        
    parts = line.split()
    command = parts[0]
    
    if command == "ADD":
        n = int(parts[1])
        heapq.heappush(heap, -n)
        
    elif command == "EXTRACT":
        if not heap:
            print("CANNOT")
        else:
            max_val = -heapq.heappop(heap)
            print(max_val)
            
    elif command == "CLEAR":
        heap.clear()
