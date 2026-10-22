
class Deque:
    def __init__(self):
        self.items = []
        
    def is_empty(self):
        return self.items == []
        
    def push_front(self, item):
        self.items = [item] + self.items
        
    def push_back(self, item):
        self.items.append(item)
        
    def pop_front(self):
        if self.is_empty():
            return "error"
        return self.items.pop(0)
        
    def pop_back(self):
        if self.is_empty():
            return "error"
        return self.items.pop()
        
    def front(self):
        if self.is_empty():
            return "error"
        return self.items[0]
        
    def back(self):
        if self.is_empty():
            return "error"
        return self.items[-1]
        
    def size(self):
        return len(self.items)
        
    def clear(self):
        self.items.clear()

deque = Deque()

while True:
    line = input().strip()
    if not line:
        continue
        
    parts = line.split()
    command = parts[0]
    
    if command == "push_front":
        n = int(parts[1])
        deque.push_front(n)
        print("ok")
    elif command == "push_back":
        n = int(parts[1])
        deque.push_back(n)
        print("ok")
    elif command == "pop_front":
        print(deque.pop_front())
    elif command == "pop_back":
        print(deque.pop_back())
    elif command == "front":
        print(deque.front())
    elif command == "back":
        print(deque.back())
    elif command == "size":
        print(deque.size())
    elif command == "clear":
        deque.clear()
        print("ok")
    elif command == "exit":
        print("bye")
        break
