# 할당 연산자

num = 100
print(num) # 100

"""
= : 할당연산자를 통해 자료형이 결정된다

파이썬은 다중할당과 동시할당이 가능하다
"""
# 다중 할당
num1 = num2 = num3 = 300
print(num1)
print(num2)
print(num3)

# 동시 할당
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




# 동시 할당 
def get_min_max(numbers):
    # 최솟값과 최댓값을 동시에 반환
    return min(numbers), max(numbers)


# packing, unpacking


# 실습: 두 개의 변수에 동시에 나누어 담기
low, high = get_min_max([15, 42, 8, 23, 99])

print(low)   # 출력: 8
print(high)  # 출력: 99
