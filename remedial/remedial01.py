print("=" * 60)
print("PYTHON BASIC CODER")
print("=" * 60)


# ============================================================
# 1. 변수
# ============================================================
print("\n[1] 변수")

name = "민지"
age = 20
height = 165.5

print(name)
print(age)
print(height)

# 변수에는 값을 다시 넣을 수 있습니다.
age = 21
print("수정된 나이:", age)

# 변수끼리 사용할 수도 있습니다.
birth_year = 2026 - age
print("계산 결과:", birth_year)

# 변수에는 다른 자료형의 값도 넣을 수 있습니다.
score = 95
message = "합격"
is_student = True

print(score)
print(message)
print(is_student)

"""
[문제 1]
다음 조건을 만족하도록 변수를 만들어 보세요.
이름: student_name → "본인이름 작성"
나이: student_age → 21
점수: python_score → 100
세 변수를 한 번씩 print()하세요.
"""



# ============================================================
# 2. 식별자 명명규칙
# ============================================================
print("\n[2] 식별자 명명규칙")

# 식별자 = 변수, 함수, 클래스 등의 이름으로 사용하는 것
# Python에서는 보통 snake_case를 사용합니다.

student_name = "철수"
total_score = 300
average_score = 100

print(student_name)
print(total_score)
print(average_score)

# 올바른 이름의 예
my_name = "민수"
age2 = 21
score_1 = 95
_private_data = "연습용"

# 사용할 수 없는 이름의 예
# 2age = 20          # 숫자로 시작할 수 없음
# my-name = "지수"   # -는 식별자에 사용할 수 없음
# my name = "지수"   # 공백 사용 불가
# class = "Python"  # 예약어 사용 불가

# Python은 대문자/소문자를 구분합니다.
age = 20
Age = 30

print("age:", age)
print("Age:", Age)

"""
[문제 2]
아래 이름 중 Python 식별자로 사용할 수 있는 것만 골라보세요.

① student
② student_name
③ 1student
④ student-name
⑤ score2
⑥ class
⑦ _score
"""


# ============================================================
# 3. 자료형 - 기본자료형
# ============================================================
print("\n[3] 기본자료형")

# 정수(int)
age = 21
count = 10

# 실수(float)
height = 165.5
temperature = 23.7

# 문자열(str)
name = "지수"
language = "Python"

# 불(bool)
is_student = True
is_teacher = False

print(age)
print(height)
print(name)
print(is_student)

# type()으로 자료형을 확인할 수 있습니다.
print(type(age))
print(type(height))
print(type(name))
print(type(is_student))

# 문자열은 따옴표로 만듭니다.
message1 = "Hello"
message2 = 'Python'

print(message1)
print(message2)

# 문자열은 여러 글자를 저장할 수 있습니다.
school = "경기과학기술대학교"
print(school)

"""
# [문제 3]
# 다음 값을 적절한 자료형으로 만들어 보세요.
type 함수를 이용해 각 변수의 자료형을 출력해보세요.
# ① 학번 20260001
# ② 평균 4.44
# ③ 이름 "성아"
# ④ 졸업여부 False
#
# 변수 이름:
# student_number
# gpa
# student_name
# graduated
"""



# ============================================================
# 4. 자료형 - 컨테이너 자료형
# ============================================================
print("\n[4] 컨테이너 자료형")

# 여러 값을 하나의 변수에 저장할 수 있습니다.

# 리스트(list)
scores = [90, 80, 100, 70]
print(scores)
print(type(scores))

# 튜플(tuple)
coordinates = (10, 20)
print(coordinates)
print(type(coordinates))

# 세트(set)
numbers = {1, 2, 3, 3, 3}
print(numbers)
print(type(numbers))

# 딕셔너리(dict)
student = {
    "name": "성아",
    "age": 21,
    "score": 100
}
print(student)
print(type(student))

# 문자열(str)도 여러 문자를 하나로 묶어 관리합니다.
word = "Python"
print(word)
print(type(word))

"""
[문제 4]
다음 데이터를 컨테이너 자료형으로 만들어 보세요.

좋아하는 숫자 3개 → 리스트
좌표 (100, 200) → 튜플
중복 없는 숫자 1, 2, 3 → 세트
이름과 나이 → 딕셔너리
"""



# ============================================================
# 5. 자료형의 메소드
# ============================================================
print("\n[5] 자료형의 메소드")

# 메소드 = 특정 자료형이 가지고 있는 기능
# 사용 형태:
# 변수.메소드()

# ----------------------------
# 문자열 메소드
# ----------------------------
text = "python programming"

print(text.upper())       # 대문자로
print(text.lower())       # 소문자로
print(text.replace("python", "Python"))
print(text.count("p"))
print(text.find("programming"))

# split()은 문자열을 나누어 리스트로 만듭니다.
sentence = "Python is easy"
words = sentence.split()

print(words)
print(type(words))

# ----------------------------
# 리스트 메소드
# ----------------------------
fruits = ["apple", "banana", "orange"]

fruits.append("melon")
print(fruits)

fruits.insert(1, "grape")
print(fruits)

fruits.remove("banana")
print(fruits)

last_fruit = fruits.pop()
print("꺼낸 값:", last_fruit)
print(fruits)

# sort()는 정렬합니다.
numbers = [50, 10, 30, 20, 40]
numbers.sort()
print(numbers)

# reverse()는 순서를 뒤집습니다.
numbers.reverse()
print(numbers)

# ----------------------------
# 딕셔너리 메소드
# ----------------------------
student = {
    "name": "성아",
    "age": 21,
    "score": 100
}

print(student.keys())
print(student.values())
print(student.items())

"""
[문제 5]
다음 리스트를 메소드를 이용해 완성하세요.

foods = ["김밥", "라면"]

① "떡볶이"를 마지막에 추가
② "우동"을 두 번째 위치에 추가
③ "라면" 삭제
"""


# ============================================================
# 6. 인덱싱
# ============================================================
print("\n[6] 인덱싱")

# 인덱스는 0부터 시작합니다.

animals = ["강아지", "고양이", "토끼", "햄스터"]

print(animals[0])
print(animals[1])
print(animals[2])
print(animals[3])

# 음수 인덱스
print(animals[-1])
print(animals[-2])

word = "Python"

print(word[0])
print(word[1])
print(word[-1])

# 딕셔너리는 인덱스가 아니라 key를 사용합니다.
student = {
    "name": "민수",
    "age": 21
}

print(student["name"])
print(student["age"])

"""
[문제 6]
아래 리스트에서 다음 값을 출력하세요.

colors = ["빨강", "주황", "노랑", "초록", "파랑"]

① "빨강"
② "노랑"
③ "파랑"
④ 뒤에서 두 번째 값
"""


# ============================================================
# 7. 슬라이싱
# ============================================================
print("\n[7] 슬라이싱")

numbers = [0, 1, 2, 3, 4, 5]

# [시작:끝]
# 끝 번호는 포함하지 않습니다.

print(numbers[0:3])
print(numbers[1:4])
print(numbers[2:])

# 시작을 생략
print(numbers[:3])

# 전체
print(numbers[:])

# 일정한 간격
print(numbers[0:6:2])

# 역순
print(numbers[::-1])

word = "PYTHON"

print(word[0:3])
print(word[2:5])
print(word[::-1])

"""
# [문제 7]
# word = "PROGRAMMING"
#
# ① "PRO" 출력
# ② "GRAM" 출력
# ③ 마지막 3글자 출력
# ④ 문자열을 거꾸로 출력
"""


# ============================================================
# 8. 연산자 - 산술 연산자
# ============================================================
print("\n[8] 산술 연산자")

a = 10
b = 3

print(a + b)   # 덧셈
print(a - b)   # 뺄셈
print(a * b)   # 곱셈
print(a / b)   # 나눗셈
print(a // b)  # 몫
print(a % b)   # 나머지
print(a ** b)  # 거듭제곱

"""
[문제 8]
사탕 25개를 4명에게 똑같이 나누어 줍니다.
① 한 명이 받는 사탕 개수
② 남는 사탕 개수
"""


# ============================================================
# 9. 대입 연산자
# ============================================================
print("\n[9] 대입 연산자")

score = 10

score += 5
print(score)

score -= 3
print(score)

score *= 2
print(score)

score /= 4
print(score)

"""
[문제 9]
money = 10000에서 시작합니다.
① 3000원을 더하고
② 2000원을 빼고
③ 2배로 만든 뒤
최종 금액을 출력하세요.
"""


# ============================================================
# 10. 비교 연산자
# ============================================================
print("\n[10] 비교 연산자")

a = 10
b = 20

print(a == b)
print(a != b)
print(a > b)
print(a < b)
print(a >= b)
print(a <= b)

# 비교 연산자의 결과는 True 또는 False입니다.

"""
[문제 10]
age = 20일 때 다음 결과를 출력하세요.

① age가 19보다 큰가?
② age가 20과 같은가?
③ age가 30보다 작은가?
"""


# ============================================================
# 11. 논리 연산자
# ============================================================
print("\n[11] 논리 연산자")

age = 21
has_ticket = True

print(age >= 20 and has_ticket)
print(age < 20 or has_ticket)
print(not has_ticket)

# and : 둘 다 True여야 True
# or  : 하나라도 True이면 True
# not : True/False를 반대로

"""
# [문제 11]
# 시험 점수가 80점 이상이고 출석률이 70% 이상이면 True가 되도록
# 코드를 작성하세요.
#
# score = 85
# attendance = 80
"""


# ============================================================
# 12. 문자열 + 숫자와 형 변환
# ============================================================
print("\n[12] 형 변환")

# 서로 다른 자료형을 그대로 더할 수는 없습니다.
age = 21

# print("나이: " + age)  # 오류 발생

# 숫자를 문자열로 바꾸기
print("나이: " + str(age))

# 문자열을 숫자로 바꾸기
number1 = int("100")
number2 = float("3.14")

print(number1)
print(number2)

"""
[문제 12]
아래 값들을 계산하여 150이 나오도록 하세요.

a = "100"
b = "50"

문자열이므로 형 변환이 필요합니다.
"""

# ============================================================
# 13. 종합 문제
# ============================================================
print("\n[13] 종합 문제")

"""
다음 정보를 하나의 딕셔너리에 저장하세요.

이름: "철수"
나이: 21
좋아하는 언어: "Python"
점수: [90, 95, 100]

그리고 다음을 출력하세요.

① 이름
② 점수 중 첫 번째 점수
③ 점수 중 마지막 점수
④ 점수의 평균

힌트:
딕셔너리에서 key를 이용해 값을 가져온 후
리스트에서 인덱싱할 수 있습니다.
"""


# ============================================================
# 14. 최종 미션
# ============================================================
print("\n[14] FINAL MISSION")

"""
아래 조건만 보고 직접 프로그램을 완성하세요.

[상황]
학생의 시험 성적을 관리하는 프로그램입니다.

이름: "Python"
점수: 87, 92, 76, 100, 83

해야 할 일:

① 이름을 변수에 저장
② 점수를 리스트에 저장
③ 첫 번째 점수 출력
④ 마지막 점수 출력
⑤ 점수 리스트를 오름차순으로 정렬
⑥ 정렬된 점수 출력
⑦ 80점 이상인 점수가 몇 개인지 직접 세어보기
⑧ 평균 점수를 계산하여 출력
⑨ 평균 점수가 80점 이상인지 비교 연산자로 출력

주의:
아직 조건문을 배우지 않았다면 ⑦은 직접 값을 세어도 됩니다.
"""

