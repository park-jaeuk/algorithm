num_frame = int(input())
n = int(input())
rec_list = list(map(int, input().split()))

frames = dict() # {번호 : [추천수, 시간]}
time = 0

for student in rec_list:
    time += 1
    if student in frames:
        frames[student][0] += 1
    else:
        if len(frames) < num_frame:
            frames[student] = [1, time]
        else:
            del_key = sorted(frames.items(), key = lambda x: (x[1][0], x[1][1]))[0][0]
            del frames[del_key]
            frames[student] = [1, time]
print(*sorted(frames.keys()))