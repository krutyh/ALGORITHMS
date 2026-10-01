def s(a, key):
    left = -1
    right = len(a)

    while right - left > 1:
        m = (left + right) // 2
        
        if a[m] <= key:
            left = m
        else:
            right = m

    if left == -1:
        return a[right]

    if right == len(a):
        return a[left]
        
    if (key - a[left]) <= (a[right] - key):
        return a[left]
    else:
        return a[right]

n, k = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

for key in b:
    print(s(a, key))
