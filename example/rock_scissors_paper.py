# 사용자 정의 예외 클래스
class InvalidInputError(Exception):
    """가위, 바위, 보 이외의 값이 입력되었을 때 발생하는 예외"""
    pass


win = 0
lose = 0
draw = 0
computer_number = 1

try:
    while win < 3:
        print("\n가위 / 바위 / 보 (종료하려면 '그만')")
        user = input("당신의 선택: ").strip()

        try:
            # 1. 중단 키워드 입력 시 강제 종료 예외 발생
            if user in ["그만", "종료", "exit", "quit"]:
                raise KeyboardInterrupt

            # 2. 잘못된 입력 시 사용자 정의 예외 발생
            if user not in ["가위", "바위", "보"]:
                raise InvalidInputError(f"'{user}'은(는) 유효한 선택지가 아닙니다.")

        except InvalidInputError as e:
            print(f"[입력 오류] {e} '가위', '바위', '보' 중 하나를 입력하세요.")
            continue  # 다시 입력받도록 루프 처음으로 이동

        # 컴퓨터 선택 (1: 가위, 2: 바위, 3: 보)
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
            draw += 1
        elif (
            (user == "가위" and computer == "보")
            or (user == "바위" and computer == "가위")
            or (user == "보" and computer == "바위")
        ):
            print("당신이 이겼습니다!")
            win += 1
        else:
            print("당신이 졌습니다!")
            lose += 1

        # 컴퓨터 다음 선택 순환 (1 -> 2 -> 3 -> 1)
        computer_number = computer_number + 1
        if computer_number > 3:
            computer_number = 1

    print("\n당신이 3번 이겼어요!!\n가위바위보를 종료합니다.\n")

except (KeyboardInterrupt, EOFError):
    print("\n\n게임을 종료합니다.")

except Exception as e:
    print(f"\n예상치 못한 오류 발생: {e}")

finally:
    total_games = win + lose + draw
    print(f"최종 결과\n{total_games}전 {win}승 {lose}패 {draw}무")













win = 0
lose = 0
draw = 0
computer_number = 1

while win < 3:
    print("\n가위 / 바위 / 보")
    user = input("당신의 선택: ")

    # 잘못된 입력 검사 
    if user not in ["가위", "바위", "보"]:
        print("잘못된 입력입니다!")
        continue

    # 컴퓨터 선택 (1: 가위, 2: 바위, 3: 보)
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
        draw += 1
    elif (user == "가위" and computer == "보") or 
         (user == "바위" and computer == "가위") or 
         (user == "보" and computer == "바위"):
        print("당신이 이겼습니다!")
        win += 1
    else:
        print("당신이 졌습니다!")
        lose += 1

    # 컴퓨터 다음 선택 순환 (1 -> 2 -> 3 -> 1)
    computer_number = computer_number + 1
    if computer_number > 3:
        computer_number = 1

print("\n당신이 3번 이겼어요!!\n가위바위보를 종료합니다.\n")
print(f"최종 결과\n{win + lose + draw}전 {win}승 {lose}패 {draw}무")


















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
