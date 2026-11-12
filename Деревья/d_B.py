nums = list(map(int, input().split()))
tree = []
max_level = 0

for x in nums:
    if x == 0:
        break
    
    pos = 0
    level = 1
    
    while True:
        while len(tree) <= pos:
            tree.append(None)
            
        if tree[pos] is None:
            tree[pos] = x
            if level > max_level:
                max_level = level
            break
        elif x < tree[pos]:
            pos = 2 * pos + 1
            level += 1
        elif x > tree[pos]:
            pos = 2 * pos + 2
            level += 1
        else:
            break

print(max_level)
