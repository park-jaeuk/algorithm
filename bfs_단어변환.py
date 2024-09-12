from collections import deque
def diff(v, word):
    cnt = 0
    for i in range(len(v)):
        if v[i] != word[i]:
            cnt += 1
    if cnt == 1:
        return True
    
def bfs(begin, target, words):
    visited = {word : False for word in words}
    queue = deque([[begin, 0]])

    while queue:
        v, dist = queue.popleft()
        if v == target:
            return dist
            break
            
        for word in words:
            if diff(v, word) and visited[word] == False:
                queue.append([word, dist+1])
                visited[word] = True
    return 0

def solution(begin, target, words):
    answer = bfs(begin, target, words)
    return answer