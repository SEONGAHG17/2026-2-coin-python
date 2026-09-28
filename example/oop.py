"""
=============================================================================
[파이썬 객체지향 프로그래밍(OOP) 교육 예시 코드 모음집]
교재 슬라이드 구성에 맞춘 단계별 예제 및 최종 통합 실습 코드
=============================================================================
"""

# =============================================================================
# [1단계] 슬라이드 1~3: 클래스(Class)와 인스턴스(Instance), 속성과 메서드
# - 클래스: 고양이 설계도
# - 속성: name, color
# - 메서드: meow(), run(), walk(), sleep()
# =============================================================================

print("\n" + "=" * 60)
print("[1단계] 클래스 정의와 인스턴스 생성 및 메서드 호출")
print("=" * 60)

class SimpleCat:
    # 메서드 정의 (동작이나 행위)
    def meow(self):
        print("야옹~ 하고 웁니다.")

    def run(self):
        print("우다다 달립니다!")

    def walk(self):
        print("살금살금 걸어갑니다.")

    def sleep(self):
        print("쿨쿨 잠을 잡니다.")


# 인스턴스 생성 (설계도로부터 메모리에 실체 객체 생성)
cat1 = SimpleCat()

# 속성(변수)을 외부에서 동적으로 부여해보기
cat1.name = "024"
cat1.color = "white"

print(f"고양이 이름: {cat1.name}, 색상: {cat1.color}")
cat1.meow()
cat1.sleep()


# =============================================================================
# [2단계] 슬라이드 4~6: 생성자(__init__), self, 그리고 인스턴스 변수
# - __init__: 객체 생성 시 자동 호출되어 초기값을 설정해주는 초기화 메서드
# - self: 생성/호출된 바로 '자기 자신' 인스턴스를 가리키는 기준 변수
# - 슬라이드 예시: '휴지'(white) 인스턴스 & '먼지'(gray) 인스턴스
# =============================================================================

print("\n" + "=" * 60)
print("[2단계] __init__ 생성자와 self를 통한 고양이 인스턴스 생성")
print("=" * 60)

class Cat:
    # 생성자: 인스턴스 생성 시 자동으로 호출됨
    def __init__(self, name, color):
        # self.변수명 : 인스턴스 변수 (각 객체마다 독립적으로 갖는 속성)
        self.name = name
        self.color = color

    def meow(self):
        # 메서드 내부에서 self를 통해 자신의 속성에 접근 가능
        print(f"[{self.name}] 야옹~ (털색: {self.color})")

    def sleep(self):
        print(f"[{self.name}] 쿨쿨 잠을 잡니다.")


# 슬라이드에 등장하는 '휴지'와 '먼지' 인스턴스 생성
cat_hyuji = Cat("휴지", "white")
cat_meonji = Cat("먼지", "gray")

# 각각의 인스턴스는 독립적인 인스턴스 변수를 유지함
print(f"휴지 정보 -> 이름: {cat_hyuji.name}, 색상: {cat_hyuji.color}")
print(f"먼지 정보 -> 이름: {cat_meonji.name}, 색상: {cat_meonji.color}")

cat_hyuji.meow()
cat_meonji.meow()


# =============================================================================
# [3단계] 슬라이드 7~8: 던더 메서드 (Dunder Method) - __str__()
# - __str__: 객체를 print()하거나 str() 함수로 감쌀 때 호출되는 문자열화 메서드
# =============================================================================

print("\n" + "=" * 60)
print("[3단계] 던더 메서드 __str__() 구현")
print("=" * 60)

class PrintableCat:
    def __init__(self, name, color):
        self.name = name
        self.color = color

    # 사람이 읽기 편한 설명 문자열(str)을 반환해야 함
    def __str__(self):
        return f"<Cat 인스턴스: 이름={self.name}, 털색={self.color}>"


hyuji = PrintableCat("휴지", "white")
# print() 함수에 객체를 바로 넘기면 내부적으로 __str__()이 자동 호출됨
print("객체 출력 결과:", hyuji)
print("str() 변환 결과:", str(hyuji))


# =============================================================================
# [4단계] 슬라이드 9~11: 캡슐화(Encapsulation)와 Getter / Setter
# - 속성을 외부에서 함부로 조작(예: age = -5)하지 못하도록 보호
# - private 변수: _age(관례적 보호) 또는 __age(이름 장식으로 직접 접근 차단)
# - getter / setter 메서드를 통해 유효성 검사 후 안전하게 접근
# =============================================================================

print("\n" + "=" * 60)
print("[4단계] 캡슐화 및 Getter / Setter")
print("=" * 60)

class ProtectedCat:
    def __init__(self, name, color, age):
        self.name = name
        self.color = color
        # 언더스코어 2개(__)를 붙여 비공개(private) 멤버로 선언
        self.__age = age

    # Getter: 안전하게 속성 값을 조회
    def get_age(self):
        return self.__age

    # Setter: 유효성 검증을 거쳐 안전하게 속성 값을 변경
    def set_age(self, new_age):
        if new_age < 0:
            print(f"[경고] 나이는 음수가 될 수 없습니다! 입력값({new_age}) 반영 거부.")
        else:
            self.__age = new_age
            print(f"[{self.name}] 나이가 {self.__age}살로 변경되었습니다.")


cat_hj = ProtectedCat("휴지", "white", 2)

# Getter로 조회
print(f"휴지의 현재 나이: {cat_hj.get_age()}살")

# 잘못된 데이터 대입 시도 (Setter의 방어 로직 동작)
cat_hj.set_age(-5)

# 올바른 데이터 대입
cat_hj.set_age(3)
print(f"휴지의 수정된 나이: {cat_hj.get_age()}살")


# =============================================================================
# [5단계] 슬라이드 12~15: 상속(Inheritance)과 super()
# - 부모 클래스: Person (일반적인 성질: name, age, gender)
# - 자식 클래스: Student (구체적인 성질: student_id, department, gpa, professor)
# - super(): 부모 클래스의 메서드와 생성자를 호출할 때 사용 (self 불필요)
# =============================================================================

print("\n" + "=" * 60)
print("[5단계] 상속(Inheritance)과 super() 활용")
print("=" * 60)

# 부모(슈퍼) 클래스
class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def introduce(self):
        print(f"안녕하세요, 저는 {self.name}({self.age}세, {self.gender})입니다.")


# 자식(서브) 클래스
class Student(Person):
    def __init__(self, name, age, gender, student_id, department, gpa, professor):
        # super()를 사용하여 부모 클래스의 __init__ 호출 (self 생략)
        super().__init__(name, age, gender)
        # 자식 클래스만의 고유 속성 정의
        self.student_id = student_id
        self.department = department
        self.gpa = gpa
        self.professor = professor

    def study(self):
        print(f"[{self.name} 학생] {self.department} 전공 공부 중 (지도교수: {self.professor})")


# 자식 클래스 인스턴스 생성
student1 = Student(
    name="김철수",
    age=21,
    gender="남성",
    student_id="20261234",
    department="컴퓨터공학과",
    gpa=4.2,
    professor="이교수님"
)

# 부모로부터 물려받은 메서드 호출
student1.introduce()
# 자식 고유의 메서드 호출
student1.study()


# =============================================================================
# [6단계] 슬라이드 16~17: isinstance()와 issubclass()
# - isinstance(객체, 클래스): 객체가 해당 클래스(또는 부모 클래스)의 인스턴스인지 판별
# - issubclass(클래스1, 클래스2): 클래스1이 클래스2의 자식 클래스인지 판별
# =============================================================================

print("\n" + "=" * 60)
print("[6단계] isinstance() 및 issubclass() 관계 검사")
print("=" * 60)

class Employee(Person):
    pass

class Manager(Employee):
    pass


p = Person("홍길동", 40, "남성")
s = Student("이영희", 22, "여성", "20265678", "인공지능학과", 4.0, "박교수님")

# isinstance 검사
print(f"isinstance(s, Student): {isinstance(s, Student)}")  # True
print(f"isinstance(s, Person) : {isinstance(s, Person)}")   # True (상속 관계이므로 부모 타입도 참)
print(f"isinstance(p, Student): {isinstance(p, Student)}")  # False

# issubclass 검사
print(f"issubclass(Student, Person) : {issubclass(Student, Person)}")   # True
print(f"issubclass(Manager, Person) : {issubclass(Manager, Person)}")   # True (간접 상속)
print(f"issubclass(Person, Student) : {issubclass(Person, Student)}")   # False


# =============================================================================
# [7단계] 슬라이드 18~20: 클래스 변수 vs 인스턴스 변수
# - 클래스 변수: 클래스 블록 내부, 메서드 외부에 정의되며 모든 인스턴스가 '공유'
# - 인스턴스 변수: self.변수명으로 정의되며 각 객체마다 '독립' 보유
# - 주의: 클래스 변수를 수정할 때는 반드시 '클래스명.변수명 = 값'으로 접근해야 함
# =============================================================================

print("\n" + "=" * 60)
print("[7단계] 클래스 변수 vs 인스턴스 변수")
print("=" * 60)

class ShelterCat:
    # 클래스 변수: 모든 고양이 객체가 공유하는 쉼터의 총 고양이 수
    total_cats = 0

    def __init__(self, name, color):
        # 인스턴스 변수: 각 고양이마다 다른 고유 데이터
        self.name = name
        self.color = color

        # 인스턴스가 새로 생성될 때마다 클래스 변수 1 증가
        ShelterCat.total_cats += 1


cat_a = ShelterCat("휴지", "white")
print(f"'{cat_a.name}' 입소 후 총 고양이 수: {ShelterCat.total_cats}")

cat_b = ShelterCat("먼지", "gray")
print(f"'{cat_b.name}' 입소 후 총 고양이 수: {ShelterCat.total_cats}")

# 주의점 시연: 인스턴스를 통한 대입 시 클래스 변수가 수정되지 않고 덮어써짐
cat_a.total_cats = 999  # cat_a 인스턴스 변수로 새로 생성되어 버림!
print("--- 잘못된 수정 시도 후 ---")
print(f"cat_a.total_cats (인스턴스 변수로 덮어써짐) : {cat_a.total_cats}")
print(f"cat_b.total_cats (여전히 클래스 변수 참조)   : {cat_b.total_cats}")
print(f"ShelterCat.total_cats (실제 원본 클래스 변수): {ShelterCat.total_cats}")


# =============================================================================
# [최종 종합 실습] 슬라이드 범위 내 모든 개념을 통합한 예시 코드
# - 클래스 변수 & 인스턴스 변수
# - 생성자(__init__) & self
# - 던더 메서드(__str__)
# - 캡슐화 & Getter/Setter
# - 상속(Person -> Student) & super()
# - isinstance() & issubclass() 검증
# =============================================================================

print("\n" + "=" * 60)
print("[최종 종합 예제] 슬라이드 내 모든 핵심 개념 통합 데모")
print("=" * 60)

class Person:
    # [클래스 변수] 전체 등록된 사람 수
    population = 0

    def __init__(self, name, age, gender):
        # [인스턴스 변수]
        self.name = name
        self.gender = gender
        # [캡슐화] private 변수
        self.__age = age

        Person.population += 1

    # [Getter / Setter]
    def get_age(self):
        return self.__age

    def set_age(self, age):
        if age < 0:
            print(f"[{self.name}] 나이는 0세 이상이어야 합니다.")
        else:
            self.__age = age

    # [던더 메서드 __str__]
    def __str__(self):
        return f"[Person] 이름: {self.name}, 성별: {self.gender}, 나이: {self.__age}세"

    def introduce(self):
        print(f"안녕하세요! 저는 {self.name}이며 {self.__age}살입니다.")


class Student(Person):
    # [클래스 변수] 재학 중인 학생 수
    student_count = 0

    def __init__(self, name, age, gender, student_id, department, gpa, professor):
        # [super()] 부모 클래스의 생성자 호출
        super().__init__(name, age, gender)
        # 자식 클래스 전용 인스턴스 변수
        self.student_id = student_id
        self.department = department
        self.gpa = gpa
        self.professor = professor

        Student.student_count += 1

    # [던더 메서드 오버라이딩]
    def __str__(self):
        return (f"[Student] 학번: {self.student_id}, 이름: {self.name}, "
                f"학과: {self.department}, 학점: {self.gpa}, 지도교수: {self.professor}")

    def study(self):
        print(f"'{self.name}' 학생이 {self.professor} 교수님의 {self.department} 과제를 수행합니다.")


# --- 종합 실행 테스트 ---

# 1. 인스턴스 생성
s1 = Student("김민수", 20, "남성", "20260001", "소프트웨어학과", 4.3, "박교수")
s2 = Student("이지은", 22, "여성", "20260002", "데이터사이언스학과", 4.5, "최교수")

# 2. 클래스 변수 공유 확인
print(f"총 인구수(Person.population): {Person.population}명")
print(f"총 학생수(Student.student_count): {Student.student_count}명")

# 3. __str__ 호출 및 출력
print(s1)
print(s2)

# 4. 부모 메서드 및 자식 메서드 호출
s1.introduce()
s1.study()

# 5. 캡슐화 테스트 (Getter & Setter)
print(f"s1 원래 나이: {s1.get_age()}세")
s1.set_age(-3)   # 유효성 검사 실패
s1.set_age(21)   # 정상 수정
print(f"s1 변경된 나이: {s1.get_age()}세")

# 6. isinstance 및 issubclass 검증
print(f"s1은 Student의 인스턴스인가? {isinstance(s1, Student)}")
print(f"s1은 Person의 인스턴스인가?  {isinstance(s1, Person)}")
print(f"Student는 Person의 자식 클래스인가? {issubclass(Student, Person)}")