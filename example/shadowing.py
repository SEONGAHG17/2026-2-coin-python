"""
클래스/인스턴스 변수에서의 섀도잉
"""
class Robot:
    country = "Korea"  # [클래스 변수]

r1 = Robot()
r2 = Robot()

# 1. 처음에는 둘 다 클래스 변수를 참조
print(r1.country)  # Korea
print(r2.country)  # Korea

# 2. r1을 통해 값을 변경하려고 시도 (대입 연산자 사용)
r1.country = "USA" 
# -> 클래스 변수가 바뀌는 게 아니라, r1 전용 인스턴스 변수 'country'가 새로 생성됨!

# 3. 섀도잉 발생
print(r1.country)        # USA   (r1의 인스턴스 변수가 클래스 변수를 가림)
print(r2.country)        # Korea (여전히 클래스 변수를 참조)
print(Robot.country)     # Korea (실제 클래스 변수는 전혀 바뀌지 않음)

# 4. r1의 인스턴스 변수를 삭제하면 다시 클래스 변수가 드러남
del r1.country
print(r1.country)        # Korea (가려졌던 클래스 변수가 다시 보임)


"""
일반 스코프(함수/전역)에서의 변수 섀도잉
"""
x = 100  # 전역 변수(Outer Scope)

def print_value():
    x = 10  # 함수 내부의 지역 변수(Inner Scope)가 바깥의 x를 가림(Shadowing)
    print("함수 내부:", x)

print_value()        # 출력: 함수 내부: 10
print("바깥 전역:", x)  # 출력: 바깥 전역: 100 (전역 변수는 그대로 유지)