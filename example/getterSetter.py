"""
왜 필요한가?
"""
class Person:
    def __init__(self, age):
        self.age = age

p = Person(25)
p.age = -10  # 말도 안 되는 값이 들어가도 검증할 방법이 없음 (무결성 깨짐)


"""
전통적인 getter / setter (의 불편함)
	- 자바 스타일
    - 함수를 따로 파서 해결하는 거
"""

class Person:
    def __init__(self, age):
        self._age = age

    def get_age(self):
        return self._age

    def set_age(self, value):
        if value < 0:
            raise ValueError("나이는 음수가 될 수 없습니다.")
        self._age = value

p = Person(25)
p.set_age(30)       # 함수 호출 문법이라 번거로움
print(p.get_age())  # 매번 get_age()를 붙여야 함

"""
@preperty 해결책 : 문법은 변수처럼, 동작은 함수처럼 진행

getter : 메서드 위에 @prpperty 를 붙임 
setter : @<메서드 이름>.setter 를 붙임
"""

class Person:
    def __init__(self, age):
        # self._age는 실제 값을 숨겨둘 내부 변수 (관례상 밑줄 하나 사용)
        self.age = age  # 인스턴스 생성 시에도 아래의 setter 로직이 실행됨

    # 1. Getter: p.age 로 값을 읽으려 할 때 자동 호출
    @property
    def age(self):
        return self._age

    # 2. Setter: p.age = 값 으로 값을 대입하려 할 때 자동 호출
    @age.setter
    def age(self, value):
        if value < 0:
            raise ValueError("나이는 음수가 될 수 없습니다.")
        if value > 150:
            raise ValueError("비정상적인 나이입니다.")
        self._age = value
        
        
p = Person(25)

# 1. 값 읽기 (Getter 동작)
# p.age() 가 아니라 p.age 로 접근하지만 내부적으로 age() 메서드가 실행됨
print(p.age)  # 출력: 25

# 2. 올바른 값 수정 (Setter 동작)
p.age = 30
print(p.age)  # 출력: 30

# 3. 비정상적인 값 대입 시도 (검증 로직 발동)
try:
    p.age = -5  # Setter 내부의 조건문에 걸림
except ValueError as e:
    print(e)    # 출력: 나이는 음수가 될 수 없습니다.








