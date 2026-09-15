# 순차문 : 위에서부터 아래로 순차적 진행
print("프로그램 시작")

name = input("이름: ")
age = int(input("나이: "))

print(name)
print(age)

print("프로그램 종료")

"""
print("프로그램 시작")
        ↓
name 입력
        ↓
age 입력
        ↓
name 출력
        ↓
age 출력
        ↓
print("프로그램 종료")
"""


# 제어문 : 프로그램의 실행 흐름을 변경하는 문법
 : 조건에 따라 실향흐름이 달라진다   
age = 20

if age >= 20:
    print("성인입니다.")
