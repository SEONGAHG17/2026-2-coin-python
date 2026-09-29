# [부모 클래스]
class Car:
    def __init__(self, model, color):
        self.model = model
        self.color = color

    def drive(self):
        print(f" {self.color} {self.model}이(가) 달립니다.")


# [자식 클래스 1] 내연기관 자동차
class Gasoline(Car):
    def __init__(self, model, color, fuel_type):
        # 부모 생성자 호출하여 model, color 초기화
        super().__init__(model, color)
        # 자식 고유 속성 추가
        self.fuel_type = fuel_type

    # drive() 메서드 오버라이딩
    def drive(self):
        print(f" {self.color} {self.model}이(가) 부릉부릉 배기음을 내며 달립니다! (연료: {self.fuel_type})")


# [자식 클래스 2] 전기 자동차
class Electric(Car):
    def __init__(self, model, color, battery_size):
        # 부모 생성자 호출하여 model, color 초기화
        super().__init__(model, color)
        # 자식 고유 속성 추가
        self.battery_size = battery_size

    # drive() 메서드 오버라이딩
    def drive(self):
        print(f" {self.color} {self.model}이(가) 모터 소리로 조용히 달립니다! (배터리: {self.battery_size}kWh)")


# --- 실행 및 검증 ---
car1 = Gasoline("G", "화이트", "가솔린")
car2 = Electric("I", "블랙", 77.4)

car1.drive()
car2.drive()