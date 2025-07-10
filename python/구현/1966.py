from collections import deque
num_case = int(input())

for _ in range(num_case):
    n, target = map(int, input().split())
    array = list(map(int, input().split()))

    queue = deque()
    for idx, i in enumerate(array):
        queue.append((i, idx))


    max_num = max(array)
    cnt = 1
    while True:
        num, idx = queue.popleft()

        if num != max_num:
            queue.append((num, idx))

            continue
        else:
            if idx == target:
                break
            else:
                array.remove(num)
                max_num = max(array)
                cnt += 1

    print(cnt)
