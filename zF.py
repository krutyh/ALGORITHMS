from random import randint

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    op = arr[randint(0, len(arr) - 1)]
    left = [el for el in arr if el < op]
    center = [el for el in arr if el == op]
    right = list(filter(lambda x: x > op, arr))
    return quick_sort(left) + center + quick_sort(right)

n = int(input())

arr = [int(x) for x in input().split()]

arr = quick_sort(arr)

print(*arr)
