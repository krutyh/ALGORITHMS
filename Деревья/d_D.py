nums = list(map(int, input().split()))
tree = []

for x in nums:
    if x == 0:
        break
    pos = 0
    while True:
        while len(tree) <= pos:
            tree.append(None)
        if tree[pos] is None:
            tree[pos] = x
            break
        elif x < tree[pos]:
            pos = 2 * pos + 1
        elif x > tree[pos]:
            pos = 2 * pos + 2
        else:
            break

curr = 0
parent = -1
while 2 * curr + 2 < len(tree) and tree[2 * curr + 2] is not None:
    parent = curr
    curr = 2 * curr + 2

if 2 * curr + 1 < len(tree) and tree[2 * curr + 1] is not None:
    curr = 2 * curr + 1
    while 2 * curr + 2 < len(tree) and tree[2 * curr + 2] is not None:
        curr = 2 * curr + 2
    print(tree[curr])
else:
    print(tree[parent])
