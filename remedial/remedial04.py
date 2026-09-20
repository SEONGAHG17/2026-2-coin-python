# =====================================================================
# 예외 처리(Exception Handling) 및 파일 입출력(File I/O)
# =====================================================================

# ---------------------------------------------------------------------
# 1. Error vs Exception
# ---------------------------------------------------------------------
"""
 - Error (에러): 문법(Syntax) 오류 등으로 인해 코드 실행 자체가 불가능한 오류
 - Exception (예외): 문법은 올바르나, 런타임(실행 도중)에 예측하지 못한
   상황(0으로 나누기, 없는 파일 열기 등)을 만나 프로그램이 비정상 종료되는 현상
"""
# ---------------------------------------------------------------------
# 2. try - except - else - finally
# ---------------------------------------------------------------------
# - try: 예외 발생 가능성이 있는 코드를 실행
# - except [예외종류] as e: 예외 발생 시 대체 실행할 코드 (e로 에러 내용 확인 가능)
# - else: try 블록에서 예외가 발생하지 않았을 때만 실행
# - finally: 예외 발생 여부와 상관없이 무조건 마지막에 실행 (자원 정리 등)

def safe_divide(x, y):
    print(f">> 계산 시작: {x} / {y}")
    try:
        result = x / y
    except ZeroDivisionError as e:
        print("except 블록: 0으로 나눌 수 없습니다! (오류 원인:", e, ")")
        return None
    except TypeError:
        print("except 블록: 숫자 데이터만 나눗셈이 가능합니다!")
        return None
    else:
        print("else 블록: 계산 성공! 결과 =", result)
        return result
    finally:
        print("finally 블록: 연산 시도가 종료되었습니다.\n")

# 정상 실행
safe_divide(100, 10)
# 예외 발생 (ZeroDivisionError)
safe_divide(100, 0)


# ---------------------------------------------------------------------
# 3. raise (강제 예외 발생)
# ---------------------------------------------------------------------
# 개발자가 의도적으로 특정 조건에서 내장 예외나 에러를 발생시키는 키워드
# 주요 내장 예외:
# - ValueError: 잘못된 값 전달
# - TypeError: 자료형 불일치
# - IndexError: 리스트 인덱스 범위 초과
# - KeyError: 딕셔너리에 없는 키 접근

def check_permission(user_role):
    valid_roles = ["admin", "student", "guest"]
    if user_role not in valid_roles:
        raise ValueError(f"유효하지 않은 역할입니다: {user_role}")
    print(f"{user_role} 권한 확인 완료.")

try:
    check_permission("hacker")
except ValueError as e:
    print("[raise 예외 포착]:", e)
print()


# ---------------------------------------------------------------------
# 4. 파일 입출력 및 open() / close()
# ---------------------------------------------------------------------
# 파일 처리 기본 3단계: 1. 열기(open) -> 2. 작업(read/write) -> 3. 닫기(close)
#
# 주요 파일 모드[cite: 2]:
# - 'r': 읽기 전용 (파일이 없으면 FileNotFoundError)
# - 'w': 쓰기 전용 (파일이 없으면 생성, 이미 있으면 덮어씀)
# - 'a': 추가 모드 (기존 내용 뒤에 이어 쓰기)
# - 'x': 배타적 생성 (파일이 이미 있으면 FileExistsError)

# open과 close를 직접 사용하는 전통적인 방식
f = open("manual_example.txt", "w", encoding="utf-8")
f.write("Hello Computer Science!\n")
f.write("Welcome to Python Programming.\n")
f.close()


# ---------------------------------------------------------------------
# 5. with 문 (Context Manager)
# ---------------------------------------------------------------------
# with 블록을 사용하면 블록을 벗어나는 순간 자동으로 f.close()가 호출됨
# 예외가 발생하더라도 안전하게 파일 자원이 시스템에 반환됨

# 파일 쓰기 (write)
with open("student_data.txt", "w", encoding="utf-8") as file:
    file.write("Jane Doe,85\n")
    file.write("John Smith,92\n")
    file.write("Alice Brown,78\n")

# 파일 읽기 메서드 비교:
# 1) read(): 파일 전체를 하나의 문자열로 반환
# 2) readline(): 한 줄씩 문자열로 반환
# 3) readlines(): 모든 줄을 읽어 각 줄이 요소인 리스트로 반환
with open("student_data.txt", "r", encoding="utf-8") as file:
    lines = file.readlines()
    print("[with문으로 파일 읽기]")
    for line in lines:
        print("한 줄 읽기:", line.strip())