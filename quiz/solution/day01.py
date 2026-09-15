magic_square = []

for i in range(4): # 행 row
    row = []
    for j in range(4): # 열 column
        num = i * 4 + j + 1
        # 대각선 위치면 뒤집고(17 - num), 아니면 그대로 추가
        row.append(17 - num if (i == j or i + j == 3) else num)
    magic_square.append(row)

for row in magic_square:
    print(row)

