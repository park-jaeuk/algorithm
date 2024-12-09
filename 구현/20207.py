calendar = [0] * 366
n = int(input())
for _ in range(n):
    start, end = map(int, input().split())
    for i in range(start, end + 1):
        calendar[i] += 1
        
result = []
current_group = []

for num in calendar:
    if num == 0:
        if current_group:    
            result.append(current_group)
            current_group = []
    else:
        current_group.append(num)
if current_group:    
    result.append(current_group)
    
    
answer = 0
for lst in result:
    answer += (max(lst) * len(lst))
print(answer)