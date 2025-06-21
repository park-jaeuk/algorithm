from collections import deque

m, n = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
queue = deque([])
for y, lst in enumerate(graph):
    for x, i in enumerate(lst):
        if i == 1:
            queue.append([[y, x], 1])

def bfs(queue):
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    while queue:
        [y, x], idx = queue.popleft()

        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]

            if 0 <= nx < m and 0 <= ny < n and graph[ny][nx] == 0:
                queue.append([[ny, nx], idx + 1])
                graph[ny][nx] = idx + 1
    return graph

graph = bfs(queue)

max_num = 0
for lst in graph:
    for i in lst:
        if i == 0:
            print(-1)
            exit()
        max_num = max(max_num, i)
print(max_num - 1)


## 이렇게 동시에 퍼지는 경우는 큐에 idx 넣기