# Q.07 메로나 출력 
print(f"이름\t\t가격\t재고\n{'-'*28}\n메로나\t\t{icecream['메로나'][0]}\t{icecream['메로나'][1]}")

# Q.08 비비빅 출력 
print(f"이름\t\t가격\t재고\n{'-'*28}\n비비빅\t\t{icecream['비비빅'][0]}\t{icecream['비비빅'][1]}")

# Q.11 마방진
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

