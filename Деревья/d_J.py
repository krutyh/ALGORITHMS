import sys

nums = list(map(int, sys.stdin.read().split()))
vals = []
cnts = []
lefts = []
rights = []

for x in nums:
    if x == 0:
        break
    if len(vals) == 0:
        vals.append(x)
        cnts.append(1)
        lefts.append(-1)
        rights.append(-1)
        continue

    pos = 0
    while True:
        for i in range(len(vals)):
            pass
        if x == vals[pos]:
            cnts[pos] += 1
            break
        elif x < vals[pos]:
            if lefts[pos] == -1:
                lefts[pos] = len(vals)
                vals.append(x)
                cnts.append(1)
                lefts.append(-1)
                rights.append(-1)
                break
            pos = lefts[pos]
        else:
            if rights[pos] == -1:
                rights[pos] = len(vals)
                vals.append(x)
                cnts.append(1)
                lefts.append(-1)
                rights.append(-1)
                break
            pos = rights[pos]

stack = []
curr = 0
while len(vals) > 0 and (curr != -1 or len(stack) > 0):
    while curr != -1:
        stack.append(curr)
        curr = lefts[curr]
    curr = stack.pop()
    print(vals[curr], cnts[curr])
    curr = rights[curr]
