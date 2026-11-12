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

def walk(pos):
    if pos >= len(tree) or tree[pos] is None:
        return
    left = 2 * pos + 1
    right = 2 * pos + 2
    walk(left)
    has_left = left < len(tree) and tree[left] is not None
    has_right = right < len(tree) and tree[right] is not None
    if has_left != has_right:
        print(tree[pos])
    walk(right)

walk(0)
