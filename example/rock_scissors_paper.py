# random 모듈 안쓰고!

win = 0
lose = 0
draw = 0

computer_number = 1

while win < 3:

    print()
    print("가위 / 바위 / 보")
    user = input("당신의 선택: ")

    # 잘못된 입력
    if user != "가위" and user != "바위" and user != "보":
        print("잘못된 입력입니다!")
        continue

    # 컴퓨터 선택
    if computer_number == 1:
        computer = "가위"
    elif computer_number == 2:
        computer = "바위"
    else:
        computer = "보"

    print("컴퓨터:", computer)

    # 승부 판정
    if user == computer:
        print("비겼습니다!")
        draw = draw + 1

    elif user == "가위" and computer == "보":
        print("당신이 이겼습니다!")
        win = win + 1

    elif user == "바위" and computer == "가위":
        print("당신이 이겼습니다!")
        win = win + 1

    elif user == "보" and computer == "바위":
        print("당신이 이겼습니다!")
        win = win + 1

    else:
        print("당신이 졌습니다!")
        lose = lose + 1

    # 컴퓨터 선택 변경
    computer_number = computer_number + 1

    if computer_number > 3:
        computer_number = 1


print()
print("당신이 3번 이겼어요!!")
print("가위바위보를 종료합니다.")

print()
print("최종 결과")
print(win + lose + draw, "전", win, "승", lose, "패", draw, "무")