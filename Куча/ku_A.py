import sys

class MaxHeap:
    def __init__(self):
        self.heap = []

    def insert(self, val):
        self.heap.append(val)
        self._sift_up(len(self.heap) - 1)

    def extract(self):
        if not self.heap:
            return None
        if len(self.heap) == 1:
            return self.heap.pop()
        
        max_val = self.heap[0]
        self.heap[0] = self.heap.pop()
        self._sift_down(0)
        return max_val

    def _sift_up(self, idx):
        while idx > 0:
            parent = (idx - 1) // 2
            if self.heap[idx] > self.heap[parent]:
                self.heap[idx], self.heap[parent] = self.heap[parent], self.heap[idx]
                idx = parent
            else:
                break

    def _sift_down(self, idx):
        size = len(self.heap)
        while 2 * idx + 1 < size:
            left = 2 * idx + 1
            right = 2 * idx + 2
            largest = left
            
            if right < size and self.heap[right] > self.heap[left]:
                largest = right
                
            if self.heap[idx] >= self.heap[largest]:
                break
                
            self.heap[idx], self.heap[largest] = self.heap[largest], self.heap[idx]
            idx = largest

lines = sys.stdin.read().splitlines()

if lines:
    n = int(lines[0])
    heap = MaxHeap()
    output = []
    
    for i in range(1, n + 1):
        parts = lines[i].split()
        if not parts:
            continue
            
        command = parts[0]
        if command == '0':
            val = int(parts[1])
            heap.insert(val)
        elif command == '1':
            output.append(str(heap.extract()))

    print('\n'.join(output))
