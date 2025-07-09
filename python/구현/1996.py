n = int(input())
graph = [list(input()) for _ in range(n)]
result = [[0] * n for _ in range(n)]
move_list = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (1, -1), (-1, 1), (-1, -1)]

for y in range(n):
    for x in range(n):
        if graph[y][x] != '.':
            result[y][x] = "*"
        else:
            for nx, ny in move_list:
                dx = x + nx
                dy = y + ny

                if 0 <= dx < n and 0 <= dy < n and graph[dy][dx] != '.':
                    result[y][x] += int(graph[dy][dx])
            if result[y][x] >= 10:
                result[y][x] = "M"

for lst in result:
    for i in lst:
        print(i, end = '')
    print('')