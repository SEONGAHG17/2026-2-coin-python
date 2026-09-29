from abc import ABC, abstractmethod

# 1. 추상 클래스 (부모): 규격만 정하는 설계도
class Vehicle(ABC):
    def __init__(self, model):
        self.model = model

    # @abstractmethod : 자식 클래스가 반드시 만들어야 하는 메서드
    @abstractmethod
    def run(self):
        pass  # 부모는 구체적인 내용을 작성하지 않고 비워둠


# 2. 자식 클래스: 부모의 규칙(run)을 각자 스타일에 맞게 반드시 구현
class Car(Vehicle):
    def run(self):
        print(f" {self.model}이(가) 도로 위를 부릉부릉")

class Airplane(Vehicle):
    def run(self):
        print(f"{self.model}이(가) 활주로 따라 슈웅")


# --- 실행 부 ---
my_car = Car("Urus")
my_plane = Airplane("Boeing747")

my_car.run()    #  Urus이(가) 도로 위를 부릉부릉 
my_plane.run()  #  Boeing747이(가) 활주로 따라 슈웅