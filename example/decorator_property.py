"""
@property
getter / setter 

1. 기존 getter setter 
2. @property ver.
3. @property issue
"""

"""
1. 기존 getter setter 
특징: 무조건 my_car.get_fuel(), my_car.set_fuel(80)처럼 함수 호출 형태(소괄호)로 써야 합니다.
"""
class Car:
    def __init__(self, model, fuel):
        self.model = model
        self.__fuel = fuel  # 비공개 변수

    # 게터(Getter) 함수
    def get_fuel(self):
        return self.__fuel

    # 세터(Setter) 함수
    def set_fuel(self, amount):
        if amount < 0:
            print("[경고] 연료는 0 미만이 될 수 없습니다.")
        else:
            self.__fuel = amount
            print(f"연료 설정 완료: {self.__fuel}L")


# --- 사용부 ---
my_car = Car("Urus", 50)

# 1. 읽을 때: 뒤에 소괄호 ()를 붙여 함수로 호출
print(my_car.get_fuel())  # 출력: 50

# 2. 수정할 때: 함수 인자로 값을 넘김
my_car.set_fuel(80)       # 출력: 연료 설정 완료: 80L
my_car.set_fuel(-10)      # 출력: [경고] 연료는 0 미만이 될 수 없습니다.






"""
2. @property ver.
"""
class Car:
    def __init__(self, model, fuel):
        self.model = model
        self.__fuel = fuel  # 비공개 변수

    # 1. 게터: @property 데코레이터 부착
    @property
    def fuel(self):
        return self.__fuel

    # 2. 세터: @<이름>.setter 데코레이터 부착
    @fuel.setter
    def fuel(self, amount):
        if amount < 0:
            print("[경고] 연료는 0 미만이 될 수 없습니다.")
        else:
            self.__fuel = amount
            print(f"연료 설정 완료: {self.__fuel}L")


# --- 사용부 ---
my_car = Car("Urus", 50)

# 1. 읽을 때: 소괄호 () 없이 일반 변수처럼 접근
print(my_car.fuel)        # 출력: 50 (내부에서 @property fuel 함수 자동 실행)

# 2. 수정할 때: 변수에 값 대입하듯 = 사용
my_car.fuel = 80          # 출력: 연료 설정 완료: 80L (내부에서 @fuel.setter 함수 자동 실행)
my_car.fuel = -10         # 출력: [경고] 연료는 0 미만이 될 수 없습니다.











