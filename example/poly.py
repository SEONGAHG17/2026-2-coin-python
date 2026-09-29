# [4단계: 추상 메서드 run()을 각자의 방식으로 완성한 자식 클래스들]

# 1) 내연기관 차
class Car(Vehicle):
    def __init__(self, model, fuel_type, fuel=50):
        super().__init__(model, fuel)
        self.fuel_type = fuel_type

    # 추상 메서드 run() 오버라이딩 (가솔린/디젤 방식)
    def run(self, distance):
        current = self.get_fuel()
        needed = distance * 0.1
        if current >= needed:
            self.set_fuel(current - needed)
            print(f"🚗 {self.model}이(가) [{self.fuel_type}] 엔진 소리를 '부르릉' 내며 {distance}km 주행!")
        else:
            print(f"🚗 {self.model}: 연료가 부족합니다.")


# 2) 전기차
class ElectricCar(Vehicle):
    def __init__(self, model, battery_capacity, fuel=100):
        super().__init__(model, fuel)
        self.battery_capacity = battery_capacity

    # 추상 메서드 run() 오버라이딩 (전기 모터 방식)
    def run(self, distance):
        current = self.get_fuel()
        needed = distance * 0.1
        if current >= needed:
            self.set_fuel(current - needed)
            print(f"⚡ {self.model}이(가) 모터 소음 없이 조용하게 {distance}km 주행! (남은 배터리: {self.get_fuel():.1f}%)")
        else:
            print(f"⚡ {self.model}: 배터리가 부족합니다.")


# [다형성 발휘 구간]
# 서로 다른 종류의 탈것 객체 생성
my_car = Car("아반떼 N", fuel_type="휘발유", fuel=40)
my_ev = ElectricCar("아이오닉 6", battery_capacity=77.4, fuel=80)

# 차고지(리스트)에 함께 보관
garage = [my_car, my_ev]

# 중요: if문으로 차종을 따지지 않고 동일하게 vehicle.run()을 호출하지만, 각자 알맞게 달림!
print("=== 다형성 실행 (동일한 호출, 서로 다른 반응) ===")
for vehicle in garage:
    vehicle.run(50)