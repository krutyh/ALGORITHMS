nums = list(map(int, input().split()))
tree = []
cnt = []

for x in nums:
    if x == 0:
        break
    pos = 0
    while True:
        while len(tree) <= pos:
            tree.append(None)
            cnt.append(0)
        if tree[pos] is None:
            tree[pos] = x
            cnt[pos] = 1
            break
        elif x < tree[pos]:
            pos = 2 * pos + 1
        elif x > tree[pos]:
            pos = 2 * pos + 2
        else:
            cnt[pos] += 1
            break

def walk(pos):
    if pos >= len(tree) or tree[pos] is None:
        return
    walk(2 * pos + 1)
    print(tree[pos], cnt[pos])
    walk(2 * pos + 2)

walk(0)
