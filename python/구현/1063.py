king, rock, n = input().split()
alpha_num = {"A" : 1, "B" : 2, "C" : 3, "D" : 4, "E" : 5, "F" : 6, "G" : 7, "H" : 8}
num_alpha = {1 : "A", 2 : "B", 3 : "C", 4 : "D", 5 : "E", 6 : "F", 7 : "G", 8 : "H"}

king_col, king_row = king[0], king[1]
king = (alpha_num[king_col], int(king_row))

rock_col, rock_row = rock[0], rock[1]
rock = (alpha_num[rock_col], int(rock_row))


map_dict = {"R" : (1, 0), "L" : (-1, 0), "B" : (0, -1), "T" : (0, 1), "RT" : (1, 1), "LT" : (-1, 1), "RB" : (1, -1), "LB" : (-1, -1)}
graph = [map_dict[input()] for _ in range(int(n))]


for nx, ny in graph:
    x, y = king

    dx = x + nx
    dy = y + ny
    if 0 < dx <= 8 and 0 < dy <= 8:
        # 킹이 돌 위치로 가면
        if dx == rock[0] and dy == rock[1]:
            rx = rock[0] + nx
            ry = rock[1] + ny
            if 0 < rx <= 8 and 0 < ry <= 8:
                king = (dx, dy)
                rock = (rx, ry)
        else:
            king = (dx, dy)


print(num_alpha[king[0]] + str(king[1]))
print(num_alpha[rock[0]] + str(rock[1]))