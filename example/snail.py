"""
사용자로부터 n을 입력받으세요.
입력받은 n을 이용하여 n x n 크기의 달팽이 배열을 만드세요.

예시
n = 5

 1  2  3  4  5
16 17 18 19  6
15 24 25 20  7
14 23 22 21  8
13 12 11 10  9

반복문을 사용하여 구현하세요.
"""

















































































#############################################################################
#############################################################################
#############################################################################
n = int(input("n을 입력하세요: "))

# n x n 배열 만들기
board = []

for i in range(n):
    board.append([0] * n)

number = 1

top = 0
bottom = n - 1
left = 0
right = n - 1

while top <= bottom and left <= right:

    # 왼쪽 → 오른쪽
    for col in range(left, right + 1):
        board[top][col] = number
        number = number + 1

    top = top + 1

    # 위쪽 → 아래쪽
    for row in range(top, bottom + 1):
        board[row][right] = number
        number = number + 1

    right = right - 1

    # 오른쪽 → 왼쪽
    if top <= bottom:
        for col in range(right, left - 1, -1):
            board[bottom][col] = number
            number = number + 1

        bottom = bottom - 1

    # 아래쪽 → 위쪽
    if left <= right:
        for row in range(bottom, top - 1, -1):
            board[row][left] = number
            number = number + 1

        left = left + 1


# 배열 출력
for row in board:
    for number in row:
        print(number, end=" ")
    print()