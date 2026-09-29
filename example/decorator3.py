"""
@ 사용하기! 
"""

def my_decorator(original_func):
    def wrapper():
        print("--- [준비 시작] ---")
        original_func()  # 전달받은 원본 함수 실행
        print("--- [동작 완료] ---")
    return wrapper  # 포장이 끝난 새로운 함수를 반환


@my_decoraor
def start_car():
    print("부릉! 자동차 시동을 겁니다.")


# 실행
start_car()