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
	# 조건문 : 조건에 따라 실행흐름이 달라진다   
	# 반복문 : 일정 주기, 조건 만족 시 순회한다
age = 20

if age >= 20:
    print("성인입니다.")

for i in range(3):
    print("Hello")


# 조건문 : 1. if / 2. else-if / 3. if-elif-else
age = int(input("나이: "))

if age >= 20:
    print("성인입니다.")


age = int(input("나이: "))

if age >= 20:
    print("성인입니다.")
else:
    print("미성년자입니다.")



score = int(input("점수: "))

if score >= 90:
    print("A")
elif score >= 80:
    print("B")
elif score >= 70:
    print("C")
elif score >= 60:
    print("D")
else:
    print("F")




# 중첩 조건문
age = int(input("나이: "))

if age >= 20:
    print("성인입니다.")

    if age >= 65:
        print("65세 이상입니다.")
else:
    print("미성년자입니다.")

# user input: 1~50. 짝/홀수 출력 해보세요

"""
반복문 : 반복의 기준에 따라

for 	"무엇을 하나씩 꺼내면서 반복"
while 	"조건이 참인 동안 반복"

"""
"""
for loop_val in iterable:
	pass
        
# iterable : L,T, s, r, S, D
"""

# 1.range
for i in range(5):
    print(i)

for i in range(1, 6):
    print(i)

for i in range(1, 10, 2):
    print(i)


# 1~50 내 짝/홀수 출력 해보세요

# 2.list
numbers = [10, 20, 30, 40]

for number in numbers:
    print(number)

# 3. tuple
numbers = (10, 20, 30, 40)

for number in numbers:
    print(number)

# 4. str
word = "Python"

for character in word:
    print(character)

# 5. set
# 순서보장 x
numbers = {10, 20, 30, 40}

for number in numbers:
    print(number)

# 6.dict
student = {
    "name": "John Doe",
    "age": 20,
    "score": 95
}

for key in student:
    print(key)

"""
for key in student:
for key in student.keys():
"""

for value in student.values():
    print(value)

for key, value in student.items():
    print(key, value)



"""
for 문으로 index이용

number = [10,20,30,40]
number의 값을 출력해라. 
이때, 각 값의 인덱스와 함께 출력하라

ex.
0 10
1 20 
2 30
3 40



numbers = [10, 20, 30, 40]

for i in range(len(numbers)):
    print(i, numbers[i])

range(len(numbers))
        ↓
0 1 2 3
        ↓
numbers[i]
        ↓
10 20 30 40
"""

# while : 조건을 검사하며 반복
i = 0

while i < 5:
    print(i)
    i += 1

"""
i = 0
 ↓
i < 5 ?
 ↓
print(0)
 ↓
i = 1
 ↓
i < 5 ?
 ↓
print(1)
...
"""


# 위험한 while문 : 반복조건을 변화하는 코드가 필요하다
"""
i = 0

while i < 5:
    print(i)
"""

# 1~50 내 짝/홀수 출력 해보세요

# for vs while
	# 반복 대상이 명확할 때
	# 조건을 기준으로 반복할 때
        
        
# 중첩 반복문 : 반복문 안에 반복문을 넣을 수 있다
for i in range(3):
    for j in range(3):
        print(i, j)

"""
i = 0
 ├─ j = 0
 ├─ j = 1
 └─ j = 2

i = 1
 ├─ j = 0
 ├─ j = 1
 └─ j = 2

i = 2
 ├─ j = 0
 ├─ j = 1
 └─ j = 2
"""

# 구구단 
# 별찍기
# 달팽이


# break keyword : 반복문 즉시 종료 >> 반복문 자체가 종료된다
for i in range(10):
    print(i)

    if i == 4:
        break


# continue keyword : 현재 반복을 건너뛰고 다음 반복으로 넘어간다 >> 현재반복만 종료될 뿐 다음 반복으로 진행된다
for i in range(5):
    if i == 2:
        continue

    print(i)

# 아래 코드는 어떻게 출력이 될까?
for i in range(5):
    for j in range(5):
        print("*", end=" ")
        
        if i == 2:
	    continue
    print()

# while + break
while True: # 무조건 실행
    number = int(input("숫자 입력: "))

    if number == 0: # 그ㄴ데 0이 들어오면 종료
        break

    print("입력한 숫자:", number)

print("프로그램 종료")

# while + continue
i = 0

while i < 10:
    i += 1

    if i % 2 == 0:
        continue

    print(i)

"""
while문에서 continue를 사용 시 어떤 영향이 오나?
변수의 변경 위치! 

i += 1를 continue보다 먼저 실행해야 무한 반복을 피한다
"""

# 중첩 반복문 + break
for i in range(3):
    for j in range(5):
        if j == 2:
            break

        print(i, j)
        
"""
break는 자신이 들어있는 가장 가까운 반복문 하나만 종료한다
for i
 └── for j
      └── break
즉, for jaks whdfygksek

0 0
0 1
1 0
1 1
2 0
2 1
"""




















