import sys

def sift_down(arr, n, idx):
    """Просеивание элемента вниз для поддержания свойств Max-Heap"""
    while 2 * idx + 1 < n:
        left = 2 * idx + 1
        right = 2 * idx + 2
        largest = left

        if right < n and arr[right] > arr[left]:
            largest = right

        if arr[idx] >= arr[largest]:
            break

        arr[idx], arr[largest] = arr[largest], arr[idx]
        idx = largest

def heap_sort(arr):
    """Основная функция пирамидальной сортировки"""
    n = len(arr)

    for i in range(n // 2 - 1, -1, -1):
        sift_down(arr, n, i)

    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        sift_down(arr, i, 0)

input_data = sys.stdin.read().split()

if input_data:
    n = int(input_data[0])
    arr = [int(x) for x in input_data[1:n+1]]

    heap_sort(arr)

    print(*arr)
