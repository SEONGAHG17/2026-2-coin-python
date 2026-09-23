"""
class >> oop 4대 개념 >> 캡슐화 >> 상속 >> 추상화 >> 다형성 
"""
# ======================================================================
# 1. self와 생성자 
# =========================================================================
class Smartphone:
    # 1. 생성자 정의: 객체가 만들어질 때 브랜드와 배터리 잔량을 초기화
    def __init__(self, brand, battery=100):
        # self.속성명 = 매개변수
        self.model = model          # 인스턴스 속성 # 객체 고유의 모델 저장
        self.battery = battery      # 인스턴스 속성 # 객체 고유의 배터리 잔량 저장

    # 2. 인스턴스 메서드 정의: 메서드 첫 번째 인자로 self 전달
    def use(self, amount):
        if self.battery >= amount:
            self.battery -= amount
            print(f"[{self.brand}] {amount}% 사용 완료. (남은 배터리: {self.battery}%)")
        else:
            print(f"[{self.brand}] 배터리가 부족합니다!")

    def info(self):
        print(f"기기: {self.brand} | 배터리: {self.battery}%")
        
    def charge(self, amount: int):
        self.battery = min(100, self.battery + amount)
        print(f"[{self.model}] {amount}% 충전 완료. (현재: {self.battery}%)") 
        
	def __str__(self):
        return f"스마트폰 모델: {self.model}, 배터리: {self.battery}%"   
        
# 객체 생성 (Smartphone의 __init__이 자동 호출됨)
phone_a = Smartphone("Galaxy", 80)
phone_b = Smartphone("iPhone", 100)

# 각각의 메서드 호출
phone_a.use(30)
phone_b.use(50)

# 상태 확인
phone_a.info()
phone_b.info()

# charge 메서드 호출
phone_a.charge(10)


# __str__ 동작 확인
print(phone_a)


# is vs == 비교
print(phone_a == phone_b)  # False (별도의 __eq__를 정의하지 않으면 파이썬 기본은 id 비교)
print(phone_a is phone_b)  # False (서로 다른 메모리 주소에 할당됨)
































