n = int(input())
s = []
last_y = 0
has_query = False

for step in range(n):
    op, val = input().split()
    x = int(val)
    if op == "+":
        if has_query:
            x = (x + last_y) % 1000000000
        if x not in s:
            s.append(x)
        has_query = False
    else:
        ans = -1
        for item in s:
            if item >= x:
                if ans == -1 or item < ans:
                    ans = item
        print(ans)
        last_y = ans
        has_query = True
