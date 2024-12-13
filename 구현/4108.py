import sys


n = int(sys.stdin.readline())
temp = [[] for _ in range(101)]
dic = [{} for i in range(101)]
cnt = 0

# 반복문을 통해 단어를 확인
for i in range(n):
    num = 0
    m = str(sys.stdin.readline()).rstrip('\n')

    # 반복문을 통해 알파벳을 확인하고
    # 그 알파벳을 수와 같이 딕셔너리형으로 추가한다.
    for j in m:
        if j not in dic[i]:
            dic[i][j] = str(num)
            num += 1

        # 현재 확인한 알파벳을 temp에 추가한다.
        temp[i] += dic[i][j]
print(dic)
print(temp)