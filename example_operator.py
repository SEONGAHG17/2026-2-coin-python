"""
1. 입출력 및 상태 확인 함수 (가장 기본 도구)
프로그램과 사용자가 소통하고, 변수의 정체를 확인할 때 사용합니다.

print(*values, sep=' ', end='\n'): 화면에 값을 출력합니다[cite: 1, 2].

input(prompt): 키보드로 입력을 받습니다. (주의: 무조건 문자열 str로 들어옴)

type(object): 데이터의 자료형을 확인합니다.

id(object): 객체의 고유한 메모리 주소(정수)를 확인합니다.





2. 형변환 (Type Conversion) 함수데이터의 타입을 다른 형태로 강제 변환하여 연산이나 자료구조를 재구성할 때 씁니다.
int(x): 정수로 변환 (int("10") $\to$ 10, int(3.8) $\to$ 3 [소수점 버림])
float(x): 실수로 변환 (float("3.14") $\to$ 3.14)
str(x): 문자열로 변환 (str(100) $\to$ "100")
list(x), tuple(x), set(x): 컬렉션 간 상호 변환[cite: 1, 2]


3. 수치 연산 및 집계 함수
숫자 데이터를 다루거나 리스트 내부를 한눈에 파악할 때 필수적입니다.

len(s): 시퀀스나 컬렉션의 길이(원소 개수)를 반환합니다[cite: 1, 2].

sum(iterable): 내부 숫자들의 총합을 계산합니다.

max(iterable) / min(iterable): 최댓값과 최솟값을 구합니다.

abs(x): 절댓값을 구합니다.

round(number, ndigits): 지정한 자릿수로 반올림합니다 (앞서 배운 부동소수점 오차 해결용).


4. 반복문(for)과 함께 쓰는 순회·조작 도우미 4대장
이 4가지는 잠시 후 배울 제어문(for)의 파트너이므로 반드시 익혀두어야 합니다.

4. 반복문(for)과 함께 쓰는 순회·조작 도우미 4대장
이 4가지는 잠시 후 배울 제어문(for)의 파트너이므로 반드시 익혀두어야 합니다.

range(start, stop, step): 숫자 생성기
숫자를 메모리에 미리 다 만들어두지 않고, 순회할 때마다 필요한 숫자를 만들어냅니다.

sorted(iterable): 안전한 정렬기
핵심: 원본 리스트는 그대로 두고, 새롭게 정렬된 리스트를 반환합니다. (원본을 뜯어고치는 list.sort() 메서드와 명확히 구분)

enumerate(iterable): 번호표 달아주기
리스트를 돌 때 "지금 몇 번째인지(인덱스)"와 "값"을 동시에 꺼내줍니다.

zip(*iterables): 1:1 지퍼 잠그기
길이가 같은 두 개 이상의 리스트를 같은 순번끼리 짝을 지어 튜플로 묶어줍니다.
"""

# 1. print 옵션 활용 (구분자 sep, 끝문자 end)
print("010", "1234", "5678", sep="-")  # 출력: 010-1234-5678
print("Hello", end=" ")
print("World")                          # 출력: Hello World (줄바꿈 없이 연결)

# 2. input과 형변환의 연결 (수강생 단골 실수 방지!)
age_str = input("나이를 입력하세요: ")    # 사용자가 20 입력 시 "20" (문자열) 저장
# age_calc = age_str + 1               # TypeError 발생! (문자열과 숫자 덧셈 불가)
age = int(age_str)                     # 숫자로 명시적 변환
print("내년 나이:", age + 1)



# 컬렉션 상호 변환의 강력한 실무 활용: 리스트 중복 제거
raw_list = [1, 2, 2, 3, 4, 4, 4]
clean_set = set(raw_list)       # {1, 2, 3, 4} (중복 제거)
clean_list = list(clean_set)    # 다시 리스트로 원복
print(clean_list)               # [1, 2, 3, 4]


scores = [70, 85, 90, 100, 60]

print("학생 수:", len(scores))    # 5
print("점수 총합:", sum(scores))   # 405
print("최고 점수:", max(scores))   # 100
print("최저 점수:", min(scores))   # 60

# 평균 구하기: sum / len 조합 (아주 흔히 쓰이는 패턴)
avg = sum(scores) / len(scores)
print("평균:", round(avg, 2))      # 81.0


# 0부터 4까지 (stop 직전까지 생성!)
for i in range(5):
    print(i, end=" ")  # 0 1 2 3 4
print()

# 1부터 10까지 2씩 증가
print(list(range(1, 11, 2)))  # [1, 3, 5, 7, 9]


nums = [4, 1, 3, 2]
sorted_nums = sorted(nums)

print("정렬본:", sorted_nums)  # [1, 2, 3, 4]
print("원본유지:", nums)        # [4, 1, 3, 2]


fruits = ["사과", "바나나", "포도"]

for idx, fruit in enumerate(fruits):
    print(f"{idx}번 과일: {fruit}")
# 0번 과일: 사과
# 1번 과일: 바나나
# 2번 과일: 포도


names = ["철수", "영희", "민수"]
ages = [20, 22, 21]

for name, age in zip(names, ages):
    print(f"{name}의 나이는 {age}살")
# 철수의 나이는 20살
# 영희의 나이는 22살
# 민수의 나이는 21살
