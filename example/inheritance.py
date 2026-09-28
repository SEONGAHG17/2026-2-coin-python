# 1. 부모 클래스 선언
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(f"{self.name}이(가) 소리를 냅니다.")

# 2. 자식 클래스 선언 (부모 클래스를 괄호에 명시)
class Dog(Animal): # 자식 클래스 정의 시 클래스 명 뒤 괄호에 부모 클래스 이름 전달
    def __init__(self, name, breed):
        # 부모 클래스의 생성자 호출
        super().__init__(name) # 상속 시 가장 중요한 점!!
        # 자식클래스에서 부모의 초기화 로직 호출하기!
        # line 50 참고
        
        # 자식 클래스만의 고유 속성 추가
        self.breed = breed

    # 메서드 오버라이딩 (부모 메서드 재정의)
    def speak(self):
        print(f"{self.name}({self.breed})이(가) 멍멍 짖습니다.")

    # 자식 클래스만의 고유 메서드
    def fetch(self):
        print(f"{self.name}이(가) 공을 물어옵니다.")
        

###################################################################
# 객체 생성 및 실행
###################################################################
        
# 자식 클래스로 객체 생성
my_dog = Dog("초코", "푸들")

# 부모에게 물려받아 재정의한 메서드 호출
my_dog.speak()  # 출력: 초코(푸들)이(가) 멍멍 짖습니다.

# 자식 클래스 고유 메서드 호출
my_dog.fetch()  # 출력: 초코이(가) 공을 물어옵니다.




##################################################################
##################################################################
##################################################################
##################################################################
##################################################################

"""
부모의 생성자를 부르지 않으면 생기는 문제! 

자식 클래스가 자체적으로 생성자를 정의하면 부모의 생성자를 자동으로 대신 불러주지 않고 덮어씀 (오버라이딩)
부모의 초기화 로직을 명시적으로 호출하지 않으면 부모의 속성이 아예 생성되지 않아 에러 발생 


* 오버라이딩
	상속 관계에서 부모 클래스로부터 물려받은 메서드를 자식 클래스에서 자신에 맞게 다시 정의해 덮어쓰는 것  


자식이 직접 self.name = name 하지 않고 부모를 부르는 이유! 
사실 자식이 저걸 해도 변수는 생김.
그럼에도 부모의 생성자를 호출하는 이유는 3가지

1. 코드 중복 제거
2. 초기화 검증 및 비즈니스 로직 유지
3. 유지보수성 : 단일 책임 
"""

class Parent:
    def __init__(self, name):
        self.name = name  # 부모가 세팅하는 속성

class Child(Parent):
    def __init__(self, name, age):
        # super().__init__(name) 을 누락한 경우!
        self.age = age

c = Child("철수", 10)

print(c.age)   # 10 (출력 정상)
print(c.name)  #  AttributeError: 'Child' object has no attribute 'name'






# 올바른 구현형태
class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
        self.fuel = 100  # 기본 연료 세팅 같은 공통 초기화

class ElectricCar(Vehicle):
    def __init__(self, brand, model, battery_capacity):
        # 1. 부모의 초기화 로직에 기본 속성 세팅을 위임
        super().__init__(brand, model)
        
        # 2. 자식만의 고유 속성만 직접 초기화
        self.battery_capacity = battery_capacity

tesla = ElectricCar("Tesla", "Model 3", "75kWh")
print(tesla.brand)             # Tesla (부모 로직 덕분에 정상 사용 가능)
print(tesla.fuel)              # 100
print(tesla.battery_capacity)  # 75kWh


