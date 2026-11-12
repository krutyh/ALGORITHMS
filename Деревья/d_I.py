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

ok = True

def height(pos):
    global ok
    if pos >= len(tree) or tree[pos] is None:
        return 0
    left_h = height(2 * pos + 1)
    right_h = height(2 * pos + 2)
    if abs(left_h - right_h) > 1:
        ok = False
    return max(left_h, right_h) + 1

height(0)
if ok:
    print("YES")
else:
    print("NO")
