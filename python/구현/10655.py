n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]

total = 0
for i in range(n - 1):
    total += abs(graph[i][0] - graph[i + 1][0]) + abs(graph[i][1] - graph[i + 1][1])

max_gain = 0
for j in range(1, n - 1):
    a, b = graph[j - 1][0], graph[j - 1][1]
    c, d = graph[j][0], graph[j][1]
    e, f = graph[j + 1][0], graph[j + 1][1]

    origin = abs(a-c) + abs(b-d) + abs(c-e) + abs(d-f)
    skip = abs(a-e) + abs(b-f)

    gain = origin - skip
    max_gain = max(max_gain, gain)
print(total - max_gain)