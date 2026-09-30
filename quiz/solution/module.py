"""
[파이썬 기초 실습: 표준 모듈과 문자열 처리 20제]
각 함수의 번호를 선택하여 실행해볼 수 있습니다.
"""

from datetime import datetime
import time
import math
import random
import sys
import os


# ----------------------------------------------------
# [datetime 모듈 실습: 1 ~ 4번]
# ----------------------------------------------------
def problem_01():
    print("\n--- [문제 1] 날짜 문자열 속성 출력 (datetime) ---")
    date_str = input("날짜 입력(YYYY-MM-DD): ")
    dt = datetime.strptime(date_str, "%Y-%m-%d")
    print(f"연도: {dt.year}")
    print(f"월: {dt.month}")
    print(f"일: {dt.day}")


def problem_02():
    print("\n--- [문제 2] 날짜 문자열의 일(Day) 수정 (datetime) ---")
    date_str = input("날짜 입력(YYYY-MM-DD): ")
    dt = datetime.strptime(date_str, "%Y-%m-%d")
    new_dt = dt.replace(day=15)
    print("수정된 날짜:", new_dt.strftime("%Y/%m/%d"))


def problem_03():
    print("\n--- [문제 3] 시간 문자열 포맷 변환 (datetime) ---")
    time_str = input("시간 입력(HH:MM:SS): ")
    t = datetime.strptime(time_str, "%H:%M:%S")
    print("변환된 시간:", t.strftime("%H시 %M분 %S초"))


def problem_04():
    print("\n--- [문제 4] 두 날짜 간 일수 차이 계산 (datetime) ---")
    d1_str, d2_str = input("두 날짜 입력(공백 구분, YYYY-MM-DD): ").split()
    d1 = datetime.strptime(d1_str, "%Y-%m-%d")
    d2 = datetime.strptime(d2_str, "%Y-%m-%d")
    diff = abs((d1 - d2).days)
    print(f"차이: {diff}일")


# ----------------------------------------------------
# [time 모듈 실습: 5 ~ 6번]
# ----------------------------------------------------
def problem_05():
    print("\n--- [문제 5] 문자열 지연 출력기 (time) ---")
    text = input("단어 입력: ")
    for char in text:
        print(char, end="", flush=True)
        time.sleep(0.5)
    print()


def problem_06():
    print("\n--- [문제 6] 지정 초 카운트다운 (time) ---")
    sec = int(input("초 입력(정수): "))
    for s in range(sec, 0, -1):
        print(f"{s}초 남음")
        time.sleep(1)
    print("종료")


# ----------------------------------------------------
# [math 모듈 실습: 7 ~ 10번]
# ----------------------------------------------------
def problem_07():
    print("\n--- [문제 7] 소수 올림/내림 처리 (math) ---")
    num_str = input("실수 입력: ")
    val = float(num_str)
    print(f"올림: {math.ceil(val)}")
    print(f"내림: {math.floor(val)}")


def problem_08():
    print("\n--- [문제 8] 음수 절대값 계산 (math) ---")
    num_str = input("실수 입력: ")
    print(f"절대값: {math.fabs(float(num_str))}")


def problem_09():
    print("\n--- [문제 9] 밑수와 지수 거듭제곱 (math) ---")
    a, b = map(float, input("밑과 지수 입력(공백 구분): ").split())
    print("거듭제곱 결과:", math.pow(a, b))


def problem_10():
    print("\n--- [문제 10] 로그 값 계산 (math) ---")
    x, base = map(float, input("진수와 밑 입력(공백 구분): ").split())
    print("로그 값:", math.log(x, base))


# ----------------------------------------------------
# [random 모듈 실습: 11 ~ 14번]
# ----------------------------------------------------
def problem_11():
    print("\n--- [문제 11] 범위 내 정수 난수 생성 (random) ---")
    start, end = map(int, input("시작과 끝 정수 입력(공백 구분): ").split())
    print(f"생성된 난수: {random.randint(start, end)}")


def problem_12():
    print("\n--- [문제 12] 단어 목록 무작위 셔플 (random) ---")
    words = input("단어들 입력(공백 구분): ").split()
    random.shuffle(words)
    print("셔플된 결과:", words)


def problem_13():
    print("\n--- [문제 13] 메뉴 목록 중 1개 랜덤 선택 (random) ---")
    menus = input("메뉴 입력(쉼표 구분): ").split(",")
    print(f"추천 메뉴: {random.choice(menus).strip()}")


def problem_14():
    print("\n--- [문제 14] 비복원 랜덤 추출 (random) ---")
    students = input("이름들 입력(공백 구분): ").split()
    k = int(input("뽑을 인원수: "))
    print(f"당첨자: {random.sample(students, k)}")


# ----------------------------------------------------
# [sys 모듈 및 파일 제어 실습: 15 ~ 16번]
# ----------------------------------------------------
def problem_15():
    print("\n--- [문제 15] sys.path 경로 포함 여부 확인 (sys) ---")
    dir_path = input("검사할 경로 입력: ")
    print(f"등록 여부: {dir_path in sys.path}")


def problem_16():
    print("\n--- [문제 16] 파일 커서 이동 및 읽기 (seek) ---")
    text = input("영문 문자열 입력: ")
    temp_file = "temp_sample.txt"
    with open(temp_file, "w+", encoding="utf-8") as f:
        f.write(text)
        f.seek(3, 0)
        print(f"3바이트 이동 후 읽은 내용: {f.read()}")
    if os.path.exists(temp_file):
        os.remove(temp_file)




# ----------------------------------------------------
# 메인 실행 제어기
# ----------------------------------------------------
PROBLEMS = {
    1: problem_01,
    2: problem_02,
    3: problem_03,
    4: problem_04,
    5: problem_05,
    6: problem_06,
    7: problem_07,
    8: problem_08,
    9: problem_09,
    10: problem_10,
    11: problem_11,
    12: problem_12,
    13: problem_13,
    14: problem_14,
    15: problem_15,
    16: problem_16,
    17: problem_17,

}

if __name__ == "__main__":
    while True:
        print("\n" + "=" * 45)
        print("파이썬 표준 모듈 실습 20제 (종료: 0)")
        print("=" * 45)
        user_choice = input("실행할 문제 번호를 입력하세요 (1~20): ").strip()

        if user_choice == "0":
            print("실습을 종료합니다.")
            break

        if user_choice.isdigit() and int(user_choice) in PROBLEMS:
            PROBLEMS[int(user_choice)]()
        else:
            print("1부터 20 사이의 올바른 숫자를 입력해주세요.")