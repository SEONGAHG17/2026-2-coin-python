# List Comprihension (내포)
"""
기존 for 문으로 리스트를 만드는 과정 >> 리스트컴프리핸션
"""

# for 문으로 리스트 만들기
"""
1부터 5의 값을 리스트에 저장하세요
[1,2,3,4,5]
"""
numbers = []

for i in range(1, 6):
    numbers.append(i)

print(numbers)


# 리스트컴프리핸션으로 진행
numbers = [i for i in range(1, 6)]

print(numbers)


"""
구조 : [표현식 for 변수 in 반복가능한_객체]
"""

# 값 변형 : 1부터 5까지의 숫자를 각각 2배한 리스트 
# >> [2, 4, 6, 8, 10]
	# for문
	# List Comprihension
   
# 문자열 변형 : 리스트의 모든 이름을 대문자로 변경
cars = ["cayenne", "taycan"]  
# >> ['CAYENNE', 'TAYCAN'] 
	# for문
	# List Comprihension
    


    
"""
numbers = []

for i in range(1, 6):
    numbers.append(i * 2)

print(numbers)

numbers = [i * 2 for i in range(1, 6)]

print(numbers)


upper_names = [name.upper() for name in names]

print(upper_names)

numbers = [i for i in range(1, 11) if i % 2 == 0]

print(numbers)

"""
    
# 조건 추가 : 1~10 중 짝수/훌수만 리스트에 저장
    # [표현식 for 변수 in 반복가능한_객체 if 조건]
numbers = [i for i in range(1, 11) if i % 2 == 0]
print(numbers)

"""
numbers = []

for i in range(1, 11):
    if i % 2 == 1:
        numbers.append(i)

print(numbers)
"""
numbers = [i for i in range(1, 11) if i % 2 == 1]
print(numbers)
"""~~조금 다른 형태 랄까나~~"""
# 조건에 따라 값 변경 : 1~5 에서 짝수는 "짝수"라, 홀수는 "홀수"라 저장
    
result = [
    "짝수" if i % 2 == 0 else "홀수" # if는 for뒤에 있는 조건 필터가 아닌 표현식 내부 조건
    for i in range(1, 6)
]

print(result)
# >> ['홀수', '짝수', '홀수', '짝수', '홀수']   

# 문자열에서 조건 필터링
names = ["John", "Tom", "Jane", "Kim"]

result = [name for name in names if len(name) >= 4]

print(result)

# 중첩 리스트컴프리핸션
"""
result = []

for row in numbers:
    for number in row:
        result.append(number)
"""

numbers = [
    [1, 2, 3],
    [4, 5, 6]
]
result = [number for row in numbers for number in row]

print(result) 
# >> [1, 2, 3, 4, 5, 6]
    
# 주어진 리스트에서 10보다 큰 숫자만 골라서 제곱한 새 리스트를 만들어라 
numbers_quiz = [3, 12, 7, 20, 5, 15]
    
    
    
    
    
"""
result = [number ** 2 for number in numbers if number > 10]

print(result) 
# >> [144, 400, 225]
"""    
    
    
    


""" [핵심 정리]

- 간단하게 나타내기 위해 등장!

- 기본형 / 조건형 / 조건에 따른 값 선택 형으로 3가지로 분류 가능

[표현식 for 변수 in iterable]
[표현식 for 변수 in iterable if 조건]
[참일_때_값 if 조건 else 거짓일_때_값 for 변수 in iterable]
"""
