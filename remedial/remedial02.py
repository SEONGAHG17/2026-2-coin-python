# Python 기초 코드
# 범위: 조건문 - 반복문 - break/continue - 리스트 컴프리헨션


print("=== 조건문 ===")

score = 85

if score >= 90:
    print("A")
elif score >= 80:
    print("B")
else:
    print("C 이하")


name = "John Doe"

if name == "John Doe":
    print("이름이 일치합니다.")


print("\n=== for 반복문 ===")

for i in range(5):
    print(i)

numbers = [10, 20, 30, 40, 50]

for number in numbers:
    print(number)


print("\n=== 반복문 + 조건문 ===")

for number in range(1, 11):
    if number % 2 == 0:
        print("짝수:", number)
    else:
        print("홀수:", number)


print("\n=== while 반복문 ===")

count = 1

while count <= 5:
    print(count)
    count = count + 1


print("\n=== break ===")

for number in range(1, 11):
    if number == 6:
        break

    print(number)


print("\n=== continue ===")

for number in range(1, 11):
    if number % 2 == 0:
        continue

    print(number)


print("\n=== break + continue ===")

for number in range(1, 11):
    if number == 8:
        break

    if number % 2 == 0:
        continue

    print(number)


print("\n=== 리스트 컴프리헨션 기초 ===")

numbers = [1, 2, 3, 4, 5]

squares = [number * number for number in numbers]

print(squares)

even_numbers = [number for number in numbers if number % 2 == 0]

print(even_numbers)

names = ["John Doe", "Alice", "Bob"]

upper_names = [name.upper() for name in names]

print(upper_names)


print("\n=== 리스트 컴프리헨션 + 조건 ===")

scores = [55, 70, 82, 91, 64]

passed = [score for score in scores if score >= 70]

print(passed)


# 문제 1
# score가 60 이상이면 "합격", 아니면 "불합격"을 출력하세요.

# 문제 2
# 1부터 10까지 홀수만 출력하세요.

# 문제 3
# 1부터 20까지 반복하다가 13이 나오면 종료하세요.

# 문제 4
# 1부터 20까지 3의 배수는 건너뛰고 출력하세요.

# 문제 5
# numbers = [1, 2, 3, 4, 5]의 제곱 리스트를
# 리스트 컴프리헨션으로 만드세요.

# 문제 6
# scores = [45, 72, 88, 51, 93, 64]에서
# 70점 이상만 리스트 컴프리헨션으로 추출하세요.

# 문제 7
# names = ["John Doe", "Alice", "Bob"]을
# 모두 대문자로 바꾼 리스트를 만드세요.

# 문제 8
# 1부터 30까지의 숫자 중 4의 배수만
# 리스트 컴프리헨션으로 만드세요.

# 문제 9
# while문으로 10부터 1까지 역순으로 출력하세요.

# 문제 10
# numbers = [5, 12, 7, 20, 3, 18]에서
# 10보다 작은 숫자는 continue로 건너뛰고 출력하세요.
