import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def dfs(x, y):
    dx = [0,0,-1,1]
    dy = [1,-1,0,0]

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if m > nx >= 0 and n > ny >= 0 and graph[ny][nx] == 1:
            graph[ny][nx] = -1
            dfs(nx, ny)
            
t = int(input()) 
for _ in range(t):
    m, n, k = map(int, input().split()) # 가로, 세로, 배추 개수
    graph = [[0 for _ in range(m)] for _ in range(n)]

    # 배추 위치
    for _ in range(k):
        X, Y = map(int, input().split()) 
        graph[Y][X] = 1

    cnt = 0
    for i in range(m):
        for j in range(n):
            if graph[j][i] == 1:
                dfs(i, j)
                cnt += 1
    print(cnt)