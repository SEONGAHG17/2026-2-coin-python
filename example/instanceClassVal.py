class Account:
    # [클래스 변수] 모든 계좌가 공유하는 은행명과 기본 이자율
    bank_name = "우리은행"
    interest_rate = 0.02

    def __init__(self, owner, balance):
        # [인스턴스 변수] 각 계좌마다 독립적인 소유주와 잔액
        self.owner = owner
        self.balance = balance


# 1. 인스턴스 변수의 독립성 확인
acc1 = Account("John Doe", 1000)
acc2 = Account("Jane Doe", 2000)

acc1.balance += 500  # 철수 계좌만 500원 입금

print(f"{acc1.owner} 잔액: {acc1.balance}")  # 1500 (John 잔액만 증가)
print(f"{acc2.owner} 잔액: {acc2.balance}")  # 2000 (Jane 잔액은 그대로 유지)

# 2. 클래스 변수의 공유 확인
print(acc1.bank_name)  # 우리은행
print(acc2.bank_name)  # 우리은행
print(Account.bank_name)  # 우리은행


##############################################################

"""
잘못된 변경 : 인승턴스로 덮어쓰기

인스턴스 변수로 착각해 객체.클래스변수 = 새값을 대입하면, 클래스 변수가 바뀌는 것이 아니라 
해당 인스턴스에 동일한 이름의 '새로운 인스턴스 변수'가 생성되어 클래스 변수를 가려버립니다(Shadowing).
"""
# 잘못된 예시: acc1을 통해 변경 시도
acc1.interest_rate = 0.05

# 결과 확인
print(acc1.interest_rate)     # 0.05 (acc1의 고유 인스턴스 변수가 생성되어 읽음)
print(acc2.interest_rate)     # 0.02 (클래스 변수 원본은 그대로 0.02)
print(Account.interest_rate)  # 0.02 (클래스 변수 원본 변경 실패)


"""
올바른 변경 : 클래스 이름으로 직접 수정 

모든 객체에 공유된 클래스 변수를 변경하려면 클래스명.변수명을 수정
"""
# 올바른 예시: 클래스명으로 직접 변경
Account.interest_rate = 0.035

# 결과 확인: 모든 인스턴스에 즉시 반영됨
print(acc2.interest_rate)     # 0.035
print(Account.interest_rate)  # 0.035



