class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

def selection_sort(points):
    n = len(points)
    for i in range(0, n - 1):
        min_index = i
        for j in range(i + 1, n):
            dist_j = points[j].x**2 + points[j].y**2  
            dist_min = points[min_index].x**2 + points[min_index].y**2
            
            if dist_j < dist_min:
                min_index = j
        if min_index != i:
            points[i], points[min_index] = points[min_index], points[i]

n = int(input())
points = []
for _ in range(n):
    x, y = map(int, input().split())
    points.append(Point(x, y))

selection_sort(points)

for p in points:
    print(p.x, p.y) 
