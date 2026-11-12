import sys

class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def add(self, node, key):
        if node is None:
            print("DONE")
            return Node(key)
        if key == node.key:
            print("ALREADY")
            return node
        if key < node.key:
            node.left = self.add(node.left, key)
        else:
            node.right = self.add(node.right, key)
        return node

    def search(self, node, key):
        if node is None:
            return False
        if key == node.key:
            return True
        if key < node.key:
            return self.search(node.left, key)
        return self.search(node.right, key)

    def delete(self, node, key):
        if node is None:
            return None
        if key < node.key:
            node.left = self.delete(node.left, key)
        elif key > node.key:
            node.right = self.delete(node.right, key)
        else:
            if node.left is None:
                return node.right
            if node.right is None:
                return node.left
            
            max_left = node.left
            while max_left.right is not None:
                max_left = max_left.right
            node.key = max_left.key
            node.left = self.delete(node.left, max_left.key)
        return node

    def print_tree(self, node, level=0):
        if node is None:
            return
        self.print_tree(node.left, level + 1)
        print("." * level + str(node.key))
        self.print_tree(node.right, level + 1)

tree = BinarySearchTree()

for line in sys.stdin.read().splitlines():
    parts = line.split()
    if not parts:
        continue
    
    cmd = parts[0]
    if cmd == "PRINTTREE":
        tree.print_tree(tree.root, 0)
    else:
        val = int(parts[1])
        if cmd == "ADD":
            tree.root = tree.add(tree.root, val)
        elif cmd == "SEARCH":
            print("YES" if tree.search(tree.root, val) else "NO")
        elif cmd == "DELETE":
            if tree.search(tree.root, val):
                tree.root = tree.delete(tree.root, val)
                print("DONE")
            else:
                print("CANNOT")
