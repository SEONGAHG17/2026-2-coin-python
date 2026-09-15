# round(number, ndigits) : 지정한 자릿수로 반올림


###############################################################

# sorted(이터러블) vs list.sort() : 정렬


#list.sort() 메서드
nums1 = [4, 2, 5, 1, 3]
res1 = nums1.sort()

print("nums1 (원본 변경됨):", nums1)  # [1, 2, 3, 4, 5]
print("res1 (반환값 없음):", res1)   # None

#sorted() 내장 함수
nums2 = [4, 2, 5, 1, 3]
res2 = sorted(nums2)

print("nums2 (원본 보존됨):", nums2)  # [4, 2, 5, 1, 3]
print("res2 (새 정렬 리스트):", res2) # [1, 2, 3, 4, 5]



"""
- 소속 및 호출 형태
    - 리스트 객체에 딸려있는 메서드
    - 어떤 반복가능한 객체든 인자로 받아 정렬하는 내장함수

- 원본 유지 여부
    - 리스트 메서드의 경우 원본 리스트의 자체 순서를 뜯어고침
    - 내장함수의 경우 원본을 전혀 건드리지 않음


- 반환값 
    - 리스트 메서드의 경우 아무것도 반환하지 않고 None을 반환한다 
    >> 결과를 변수에 할당할 수 없다
    - 내장함수는 원본을 전혀 건드리지 않고 안전하게 보존한다 
    >> 새롭게 정렬된 list 객체 반환한다
"""








# enumerate(이터러블)

fruits = ['사과', '바나나', '포도']

# 1. 기본 사용 (0번부터 시작)
for idx, fruit in enumerate(fruits):
    print(f"{idx}번: {fruit}")
# 0번: 사과
# 1번: 바나나
# 2번: 포도

# 2. 시작 번호 지정 (start=1)
for rank, fruit in enumerate(fruits, start=1):
    print(f"{rank}등 과일: {fruit}")
# 1등 과일: 사과
# 2등 과일: 바나나
# 3등 과일: 포도

"""
반복문(for)을 순회할 때 "현재 몇 번째 인덱스인지"와 "그 위치의 값"을 동시에 튜플 형태로 꺼내주는 함수
별도의 카운트 변수를 선언해서 i += 1을 할 필요가 없어 코드가 간결해진다


기본 문법: enumerate(iterable, start=0)
두 번째 인자인 start를 지정하면 인덱스 시작 번호를 1 등 원하는 숫자로 바꿀 수 있다
"""


# zip(이터러블)

names = ["Kim", "Lee", "Park"]
scores = [95, 88, 72]
grades = ["A", "B", "C"]

# 1. 두 리스트를 1:1로 묶기
for name, score in zip(names, scores):
    print(f"{name} 학생의 점수는 {score}점입니다.")
# Kim 학생의 점수는 95점입니다.
# Lee 학생의 점수는 88점입니다.
# Park 학생의 점수는 72점입니다.

# 2. 3개 이상의 리스트 묶기 및 딕셔너리 생성 활용
students_dict = dict(zip(names, scores))
print("딕셔너리 변환:", students_dict)
# {'Kim': 95, 'Lee': 88, 'Park': 72}

"""
길이가 같거나 다른 여러 개의 시퀀스(또는 이터러블)를 병렬로 엮어서 동일한 순번의 원소끼리 튜플로 묶어 반환

묶인 결과는 튜플 형태 (elem1, elem2, ...)로 순회
둘 이상의 리스트 길이가 서로 다를 경우, 기본적으로 가장 짧은 리스트의 길이에 맞춰 순회가 종료됩니다.
"""




# 결합 응용 : enumerate와 zip의 결합

names = ["민수", "영희", "철수"]
scores = [90, 85, 95]

# zip으로 묶은 뒤 enumerate로 번호표 달기
for idx, (name, score) in enumerate(zip(names, scores), start=1):
    print(f"[{idx}번 참가자] 이름: {name}, 성적: {score}")

# [출력 결과]
# [1번 참가자] 이름: 민수, 성적: 90
# [2번 참가자] 이름: 영희, 성적: 85
# [3번 참가자] 이름: 철수, 성적: 95