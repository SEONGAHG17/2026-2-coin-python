"""
decorator 탄생 신화 (등장 배경)
- 문제 상황 : 반복되는 전후처리 코드
- 해결책 : 함수를 받아 포장지(Wrapper) 씌우는 공장 함수 만들기
"""

# 1. problem
def start_car():
    print("--- [준비 시작] ---")
    print("부릉! 자동차 시동을 겁니다.")
    print("--- [동작 완료] ---")

def stop_car():
    print("--- [준비 시작] ---")
    print("끼익! 자동차를 멈춥니다.")
    print("--- [동작 완료] ---")



# 2. solution
# 포장해 주는 공장 함수 (데코레이터의 실체)
def my_decorator(original_func):
    def wrapper():
        print("--- [준비 시작] ---")
        original_func()  # 전달받은 원본 함수 실행
        print("--- [동작 완료] ---")
    return wrapper  # 포장이 끝난 새로운 함수를 반환

# 원본 함수는 자기 할 일만 순수하게 정의
def start_car():
    print("부릉! 자동차 시동을 겁니다.")

# 수동으로 포장하기
start_car = my_decorator(start_car)

# 실행
start_car()

"""
>>

--- [준비 시작] ---
부릉! 자동차 시동을 겁니다.
--- [동작 완료] ---
"""




