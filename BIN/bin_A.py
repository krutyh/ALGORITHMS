def s(a, key):
    left = -1
    right = len(a)
    
    while right - left > 1:
        m = (left + right) // 2
        if a[m] < key:
            left = m
        else:
            right = m

    if right < len(a) and a[right] == key:
        return True
    return False

n, k = map(int, input().split())

a = list(map(int, input().split()))

b = list(map(int, input().split()))

for key in b:
    if s(a, key):
        print("YES")
    else:
        print("NO")
