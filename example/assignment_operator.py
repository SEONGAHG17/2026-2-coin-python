# 할당 연산자

num = 100
print(num) # 100

"""
= : 할당연산자를 통해 자료형이 결정된다

파이썬은 다중할당과 동시할당이 가능하다
"""
"""
동일 할당 : 하나의 값을 여러 변수에 동일참조로 연속 연결 
"""


# 동일 할당, 연쇄 할당
num1 = num2 = num3 = 300
print(num1)
print(num2)
print(num3)

# 다중 할당, 동시 할당
num4, num5 = 400, 500
print(num4)
print(num5)




# 다중 할당 주의점 !!(불변/가변 이슈)
immutable1 = imutablie2 = 0

mutable1 = mutable2 = []
print(mutable1)
print(mutable2)
mutable1.append(1)
print(mutable1)
print(mutable2)



# packing, unpacking
"""
packing : 여러 데이터를 하나의 컨테이너(주로 튜플)로 묶는 것
    - 파이썬에서 줄로 ,로 나열된 값들을 괄호 없이 적으면 자동으로 튜플로 패킹
    - 여러 값 >> 하나의 묶음
    
    
unpacking : 묶여 있는 컬렉션의 요소들을 각각 개발변수로 풀어내는 것
    - 좌변의 변수 개수와 우변의 컬랙션 요소 개수가 정확히 일치해야한다
    - 하나의 묶음 >> 여러 변수
"""


# 동시 할당 
def get_min_max(numbers):
    # 최솟값과 최댓값을 동시에 반환
    return min(numbers), max(numbers)
# 실습: 두 개의 변수에 동시에 나누어 담기
low, high = get_min_max([15, 42, 8, 23, 99])

print(low)   # 출력: 8
print(high)  # 출력: 99



