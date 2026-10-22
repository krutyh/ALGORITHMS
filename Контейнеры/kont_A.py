
class Stack:
    def __init__(self):
        self.items = []
        
    def is_empty(self):
        return len(self.items) == 0
        
    def push(self, item):
        self.items.append(item)
        
    def pop(self):
        if self.is_empty():
            return "error"
        return self.items.pop()
        
    def back(self):
        if self.is_empty():
            return "error"
        return self.items[-1]
        
    def size(self):
        return len(self.items)
        
    def clear(self):
        self.items = []

stack = Stack()

while True:
    line = input().strip()
    if not line:
        continue
        
    parts = line.split()
    command = parts[0]
    
    if command == "push":
        n = int(parts[1])
        stack.push(n)
        print("ok")
    elif command == "pop":
        print(stack.pop())
    elif command == "back":
        print(stack.back())
    elif command == "size":
        print(stack.size())
    elif command == "clear":
        stack.clear()
        print("ok")
    elif command == "exit":
        print("bye")
        break
