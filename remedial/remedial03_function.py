"""
====================================================================
사용자 정의 함수, Lambda, map/filter, 제네레이터와 yield
====================================================================
"""

# ==================================================================
# 1. 사용자 정의 함수 (User-Defined Function)
# ==================================================================
# - 내장 함수(Built-in Function: print, len, sum 등)와 달리 개발자가
#   'def' 키워드를 사용하여 직접 정의하는 함수입니다.
# - 매개변수(Parameter): 함수 정의 시 전달받는 변수
# - 전달인자(Argument): 함수를 호출할 때 실제로 넘겨주는 값
# - return: 결과값을 호출한 곳으로 반환하며, 함수 실행을 종료합니다.
#   (return문이 없거나 단독으로 쓰이면 None을 반환)

def user_hello(username):
	return (f"hello {username}! '\t' welcome everland ")

inputusername = input("what is your name? : ")
print(user_hello(unputusername))

def add_numbers(a, b):
    result = a + b
    return result

total = add_numbers(10, 20)
print("[1. 사용자 정의 함수] 10 + 20 =", total)


# ==================================================================
# 2. 람다 식 (Lambda Function)
# ==================================================================
# - 이름 없이 한 줄로 간결하게 정의하는 익명 함수(Anonymous Function)입니다.
# - 문법: lambda 매개변수1, 매개변수2, ... : 단일_표현식_반환값
# - 복잡한 로직이나 여러 줄의 코드가 필요 없는 1회성 변환 또는 정렬 키로 적합합니다.

# 일반 함수 정의
def add(x, y):
    return x + y

# 동일한 동작을 하는 lambda 식
add_lambda = lambda x, y: x + y
print(f"[2. Lambda 기본] add_lambda(100, 200) -> {add_lambda(100, 200)}")

# 일반 함수로 만든 경우
def square(x):
    return x * x

# 람다로 간단하게 만든 경우
square_lambda = lambda x: x * x

print("[2. 람다 함수] 일반 함수 square(4):", square(4))
print("[2. 람다 함수] 람다 square_lambda(4):", square_lambda(4))


# ==================================================================
# 3. map() & filter() 함수
# ==================================================================
# - 고차 함수(Higher-Order Function)로, 함수와 iterable 객체를 인자로 받습니다.
# - 결과는 즉시 리스트로 연산되지 않고 '이터레이터 객체'로 반환됩니다. 


# 둘 다 함수와 리스트를 받아서 반복 작업을 한 번에 처리합니다.
# 결과를 보려면 list()로 감싸서 변환해야 합니다.

numbers = [1, 2, 3, 4, 5, 6, 7, 8]


# [map(함수, 반복가능객체)]
# iterable의 모든 원소에 함수를 일괄 적용

# 각 숫자를 10배로 만들기
ten_times = list(map(lambda x: x * 10, numbers))
print("[3. map] 10배 곱하기:", ten_times)

# 각 숫자 제곱하기
squared_numbers = list(map(lambda x: x ** 2, numbers))
print(f"[3. map] 제곱 결과: {squared_numbers}")


# [filter(함수, 반복가능객체)]
# [filter] 함수의 결과가 True인 원소만 걸러내기
# 짝수만 걸러내기
evens = list(filter(lambda x: x % 2 == 0, numbers))
print("[3. filter] 짝수만 추출:", evens)


# [filter(함수, 반복가능객체)]
# 함수의 반환값이 True인 원소만 걸러냄
ages = [11, 45, 44, 78, 27, 9, 20]
adults = list(filter(lambda x: x >= 19, ages))
print(f"[3. filter] 성인 연령 필터링: {adults}")




# [map과 filter 결합 파이프라인]
# 짝수만 추출한 뒤 각각에 10을 곱하기
even_scaled = list(map(lambda x: x * 10, filter(lambda x: x % 2 == 0, numbers)))
print(f"[3. map + filter 파이프라인] 짝수 * 10: {even_scaled}")


# ==================================================================
# 4. 제네레이터(Generator)와 yield
# ==================================================================
# - 일반 함수는 return을 만나면 결과값을 반환하고 스택 프레임이 종료(소멸)됩니다.
# - return : 값으ㄹ 돌려주고 함수가 완전히 끝난다
# - yield : ㄱㅏㅂㅅ으ㄹ 하나 돌려주고, 그 자리에서 잠깜 멈춤 (상태 유지) 
# - next() 함수를 호출할 때마다 중단된 지점부터 다시 실행



def count_up():
    print(">> 첫 번째 숫자 생성 시작")
    yield 1
    print(">> 두 번째 숫자 생성 시작")
    yield 2
    print(">> 세 번째 숫자 생성 시작")
    yield 3

# 제네레이터 객체 생성
gen = count_up()

print("[4. 제네레이터]")
print("1차 next:", next(gen))  # 1 출력 후 일시 정지
print("2차 next:", next(gen))  # 2 출력 후 일시 정지
print("3차 next:", next(gen))  # 3 출력 후 일시 정지


# 반복문과 함께 사용하는 제네레이터 예제
def make_numbers(n):
    num = 1
    while num <= n:
        yield num
        num = num + 1

print("[4. 제네레이터 for문 순회]:")
for val in make_numbers(5):
    print(val, end=" ")
print()