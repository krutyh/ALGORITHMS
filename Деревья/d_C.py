nums = list(map(int, input().split()))
tree = []
count = 0

for x in nums:
    if x == 0:
        break
        
    pos = 0
    while True:
        while len(tree) <= pos:
            tree.append(None)
            
        if tree[pos] is None:
            tree[pos] = x
            count += 1
            break
        elif x < tree[pos]:
            pos = 2 * pos + 1
        elif x > tree[pos]:
            pos = 2 * pos + 2
        else:
            break

print(count)
