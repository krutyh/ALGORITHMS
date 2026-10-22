class Queue:
    def __init__(self):
        self.items = []
        
    def is_empty(self):
        return len(self.items) == 0
        
    def push(self, item):
        self.items.append(item)
        
    def pop(self):
        if self.is_empty():
            return "error"
        return self.items.pop(0)
        
    def front(self):
        if self.is_empty():
            return "error"
        return self.items[0]
        
    def size(self):
        return len(self.items)
        
    def clear(self):
        self.items.clear()

queue = Queue()

while True:
    line = input().strip()
    if not line:
        continue
        
    parts = line.split()
    command = parts[0]
    
    if command == "push":
        n = int(parts[1])
        queue.push(n)
        print("ok")
    elif command == "pop":
        print(queue.pop())
    elif command == "front":
        print(queue.front())
    elif command == "size":
        print(queue.size())
    elif command == "clear":
        queue.clear()
        print("ok")
    elif command == "exit":
        print("bye")
        break
