"""
decorator 이해를 위한 사전 지식 3 가지
	1. 함수를 변수 안에 담을 수 있다
	2. 함수를 다른 함수의 인자로 전달할 수 있다
	3. 함수 안에 또 다른 함수를 만들고 반환할 수 있다
"""

# 1. 함수를 변수 안에 담을 수 있다
def say_hi():
    print("안녕!")

# 괄호()를 붙이지 않고 이름만 가져오면 함수 자체를 변수에 대입할 수 있음
my_func = say_hi
my_func()  # "안녕!" 출력



# 2. 함수를 다른 함수의 인자로 전달할 수 있다
def run_twice(func):
    func()
    func()

run_twice(say_hi)  # "안녕!"이 2번 출력됨


# 3. 함수 안에 또 다른 함수를 만들고 반환할 수 있다
def outer():
    def inner():
        print("내부 함수 실행!")
    return inner  # 함수 껍데기 자체를 밖으로 던져줌

new_func = outer()
new_func()  # "내부 함수 실행!" 출력
