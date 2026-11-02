import heapq

def get_cells(maze, r, c):
    """Находит соседние доступные клетки"""
    res = []
    steps = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    rows = len(maze)
    cols = len(maze[0]) if rows > 0 else 0
    
    for dr, dc in steps:
        new_r = r + dr
        new_c = c + dc
        if 0 <= new_r < rows and 0 <= new_c < cols:
            if maze[new_r][new_c] == 0:
                res.append((new_r, new_c))
    return res

def get_final_path(history, start, finish):
    """Восстанавливает итоговый путь от финиша к старту"""
    path = []
    curr = finish
    while curr is not None:
        path.append(curr)
        curr = history.get(curr)
    path.reverse()
    if path and path[0] == start:
        return path
    return []

def run_dijkstra(maze, start, finish):
    """Поиск кратчайшего пути методом Дейкстры"""
    pq = [(0, start)]  
    dist = {start: 0}
    history = {start: None}
    count = 0

    while pq:
        curr_dist, curr = heapq.heappop(pq)
        count += 1
        
        if curr == finish:
            final_path = get_final_path(history, start, finish)
            return final_path, count
            
        if curr_dist > dist.get(curr, float('inf')):
            continue
            
        for next_cell in get_cells(maze, curr[0], curr[1]):
            new_dist = curr_dist + 1
            
            if new_dist < dist.get(next_cell, float('inf')):
                dist[next_cell] = new_dist
                history[next_cell] = curr
                heapq.heappush(pq, (new_dist, next_cell))
                
    return [], count

print("Настройка лабиринта (Алгоритм Дейкстры)")
rows = int(input("Введите количество строк лабиринта: "))
cols = int(input("Введите количество столбцов лабиринта: "))

print(f"\nВведите матрицу лабиринта построчно ({rows} строк). Используйте 0 (свободно) и 1 (стена) через пробел:")
maze_map = []
for i in range(rows):
    row_input = input(f"Строка {i}: ").split()
    row_data = [int(x) for x in row_input]
    maze_map.append(row_data)

print("\nВведите координаты точек через пробел (строка столбец):")
start_input = input("Координаты начальной точки: ").split()
start_point = (int(start_input[0]), int(start_input[1]))

finish_input = input("Координаты конечной точки: ").split()
end_point = (int(finish_input[0]), int(finish_input[1]))

path, steps = run_dijkstra(maze_map, start_point, end_point)

print("\nРезультат: Алгоритм Дейкстры")
print(f"Найденный путь: {path}")
print(f"Проверено клеток лабиринта: {steps}")
