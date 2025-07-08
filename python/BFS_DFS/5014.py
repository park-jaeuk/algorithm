from collections import deque
f, s, g, u, d = map(int, input().split())
visited = [False] * (f + 1)

queue = deque([[s, 0]])
visited[s] = True

while queue:
    v, idx = queue.popleft()

    if v == g:
        print(idx)
        break

    du = v + u
    dd = v - d

    if 1 <= du <= f and not visited[du]:
        queue.append([du, idx + 1])
        visited[du] = True
    if 1 <= dd <= f and not visited[dd]:
        queue.append([dd, idx + 1])
        visited[dd] = True


if not visited[g]:
    print('use the stairs')