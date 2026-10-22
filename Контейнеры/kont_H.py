import sys
from collections import deque

data = sys.stdin.read().split()

if data:
    n = int(data[0])
    
    left = deque()
    right = deque()
    
    idx = 1
    output = []
    
    for _ in range(n):
        command = data[idx]
        
        if command == '+':
            goblin = data[idx+1]
            right.append(goblin)
            idx += 2
        elif command == '*':
            goblin = data[idx+1]
            right.appendleft(goblin)
            idx += 2
        elif command == '-':
            output.append(left.popleft())
            idx += 1
            
        if len(left) < len(right):
            left.append(right.popleft())
        elif len(left) > len(right) + 1:
            right.appendleft(left.pop())

    print('\n'.join(output))
