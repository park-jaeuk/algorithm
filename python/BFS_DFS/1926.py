from collections import deque, Counter

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

def bfs(y, x, size):
    queue = deque([[y, x]])
    graph[y][x] = size

    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    while queue:
        y, x = queue.popleft()

        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]

            if 0 <= nx < m and 0 <= ny < n and graph[ny][nx] == 1:
                queue.append([ny, nx])
                graph[ny][nx] = size
size = 2
for y in range(n):
    for x in range(m):
        if graph[y][x] == 1:
            bfs(y, x, size)
            size += 1

total_list = [i for lst in graph for i in lst if i != 0]
total_dict = dict(Counter(total_list))

max_value = 0
for key, value in total_dict.items():
    if max_value < value:
        max_value = value
print(len(total_dict))
print(max_value)