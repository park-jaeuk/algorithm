from collections import Counter

name = input()
n = int(input())
name_list = [input() for _ in range(n)]
name_list.sort()  # 점수 동점일 경우 사전순 우선

def counter(a, b):
    combined = a + b
    count = Counter(combined)
    return {
        'L': count.get('L', 0),
        'O': count.get('O', 0),
        'V': count.get('V', 0),
        'E': count.get('E', 0)
    }

def calculator(dic):
    return (
        (dic["L"] + dic['O']) *
        (dic["L"] + dic['V']) *
        (dic["L"] + dic['E']) *
        (dic["O"] + dic['V']) *
        (dic["O"] + dic['E']) *
        (dic["V"] + dic['E'])
    ) % 100

answer = 0
answer_name = ''
for x in name_list:
    name_dict = counter(name, x)
    result = calculator(name_dict)

    if result > answer:
        answer = result
        answer_name = x

if answer == 0:
    answer_name = name_list[0]
print(answer_name)