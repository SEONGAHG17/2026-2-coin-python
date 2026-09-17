# ==================================================================
# 1. 함수의 정의와 사용 이유
# ==================================================================
# [정의]
# 특정 작업이나 연산을 수행하기 위해 하나로 묶어둔 독립적인 코드 블록입니다.
#
# [사용 이유]
# 1) 재사용성: 동일한 코드를 복사/붙여넣기 할 필요 없이 이름만 호출하여 재실행
# 2) 유지보수 용이: 로직 수정 시 함수 내부만 수정하면 호출한 모든 곳에 일괄 적용
# 3) 모듈화 및 추상화: 복잡한 시스템을 기능별 작은 단위로 분할하여 관리
# ==================================================================

# 예제: 사용자 정의 함수 기본 구조 (def 키워드 사용)
def greet(name):
    return f"안녕하세요, {name}님!"

print("=== 1. 함수 정의 및 호출 예제 ===")
print(greet("파이썬"))
print()

# [기초 문제 1]
# 두 개의 정수를 전달받아 두 수의 합을 반환하는 함수 `add_numbers(a, b)`를 정의하고 호출해보세요.
# --- 작성 공간 ---
def add_numbers(a, b):
    return a + b

print("문제 1 결과:", add_numbers(10, 20))
print("-" * 50)


# ==================================================================
# 2. 내장 함수 - 입출력 및 상태 확인 (print, input, type, id)
# ==================================================================
#  print(*values, sep=' ', end='\n'): 화면 출력, sep(구분자), end(끝 문자)
#  input(prompt): 키보드로 입력받음 (결과는 항상 문자열 str)
#  type(object): 객체의 자료형 확인
#  id(object): 객체의 고유한 메모리 주소(정수) 반환
# ==================================================================

print("=== 2. 입출력 및 상태 확인 예제 ===")
# sep, end 활용
print("010", "1234", "5678", sep="-")
print("Hello", end=" ")
print("World")

# type, id 확인
val = 100
print("val의 타입:", type(val))
print("val의 고유 메모리 주소(id):", id(val))
print()

# [기초 문제 2]
# print 함수를 사용하여 세 단어 "Python", "is", "Fun"을 언더바(_)로 연결하여 출력하고,
# 줄바꿈 없이 끝에 "!"가 붙도록 작성해보세요. (sep와 end 활용)
# --- 작성 공간 ---
print("문제 2 결과:", end=" ")
print("Python", "is", "Fun", sep="_", end="!\n")
print("-" * 50)


# ==================================================================
# 3. 내장 함수 - 형변환 함수 (int, float, str, list, tuple, set)
# ==================================================================
#  int(x): 정수로 변환 (소수점 버림)
#  float(x): 실수로 변환
#  str(x): 문자열로 변환
#  컬렉션 상호 변환: set을 이용해 중복 제거 후 list로 원복 가능
# ==================================================================

print("=== 3. 형변환 함수 예제 ===")
print("int('10'):", int("10"), "int(3.8):", int(3.8))
print("float('3.14'):", float("3.14"))
print("str(100):", type(str(100)))

# 중복 제거 패턴
raw_list = [1, 2, 2, 3, 4, 4, 4]
clean_list = list(set(raw_list))
print("중복 제거 결과:", clean_list)
print()

# [기초 문제 3]
# numbers = ["10", "20", "30", "20", "10"] 문자열 리스트가 있습니다.
# 중복을 제거한 뒤, 각 요소를 정수형(int)으로 변환하여 새로운 리스트를 만들어 출력해보세요.
# --- 작성 공간 ---
numbers = ["10", "20", "30", "20", "10"]
unique_ints = []
for item in set(numbers):
    unique_ints.append(int(item))
print("문제 3 결과:", sorted(unique_ints))
print("-" * 50)


# ==================================================================
# 4. 내장 함수 - 수치 연산 및 집계 함수 (len, sum, max, min, abs, round)
# ==================================================================
# • len(s): 길이/원소 개수 반환
# • sum(iterable): 숫자들의 총합
# • max(iterable) / min(iterable): 최댓값, 최솟값
# • abs(x): 절댓값
# • round(number, ndigits): 반올림
# ==================================================================

print("=== 4. 수치 연산 및 집계 예제 ===")
scores = [85, 92, 78, 90, 88]
print("개수:", len(scores))
print("총합:", sum(scores))
print("최고/최저:", max(scores), min(scores))
print("절댓값 abs(-15):", abs(-15))
print("반올림 round(3.141592, 2):", round(3.141592, 2))
print()

# [기초 문제 4]
# scores = [70, 85, 93, 64, 78] 리스트가 주어졌을 때,
# 최고점과 최저점의 차이(절댓값)와 전체 평균(소수점 둘째 자리까지 반올림)을 구해보세요.
# --- 작성 공간 ---
scores = [70, 85, 93, 64, 78]
diff = abs(max(scores) - min(scores))
avg = round(sum(scores) / len(scores), 2)
print(f"문제 4 결과: 차이={diff}, 평균={avg}")
print("-" * 50)


# ==================================================================
# 5. 내장 함수 - 반복문 연계 (range, sorted, enumerate, zip)
# ==================================================================
#  range(start, stop, step): 숫자 시퀀스 생성 (순회 시점에 생성)
#  sorted(iterable): 원본을 유지하며 정렬된 새 리스트 반환 (list.sort()와 차이)
#  enumerate(iterable): (인덱스, 값)을 튜플로 반환
#  zip(iter1, iter2): 동일 인덱스 요소들을 튜플로 묶음
# ==================================================================

print("=== 5. 반복문 연계 내장 함수 예제 ===")
# sorted
original = [5, 2, 8, 1]
sorted_list = sorted(original)
print("원본 유지:", original, "정렬본:", sorted_list)

# enumerate
fruits = ["apple", "banana", "cherry"]
for idx, fruit in enumerate(fruits, start=1):
    print(f"{idx}번 과일: {fruit}")

# zip
names = ["철수", "영희", "민수"]
ages = [15, 16, 15]
for name, age in zip(names, ages):
    print(f"{name}: {age}세")
print()

# [기초 문제 5]
# subjects = ["국어", "수학", "영어"]
# scores = [90, 80, 100]
# zip과 enumerate를 활용하여 "1등 과목: 국어 (90점)" 형식으로 순서대로 출력해보세요.
# --- 작성 공간 ---
print("문제 5 결과:")
for rank, (subj, score) in enumerate(zip(subjects, scores), start=1):
    print(f"{rank}등 과목: {subj} ({score}점)")
print("-" * 50)