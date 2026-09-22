# ==============================================================================
# PART 1. 예외 처리 집중 연습 (문제 1 ~ 5)
# ==============================================================================

# 문제 1. 정수 변환 안전기 (ValueError 다루기)
# [상황] 사용자로부터 문자열을 입력받아 숫자로 바꾸려 합니다.
# 숫자로 바꿀 수 없는 문자열("백원", "abc" 등)이 들어오면 에러 대신 기본값 -1을 반환하세요.
def safe_string_to_int(text: str) -> int:
    # TODO: try - except ValueError 구문을 사용하세요.
    pass


# 문제 2. 0으로 나누기 방어 (ZeroDivisionError 다루기)
# [상황] 피자를 N명이서 똑같이 나누어 먹으려고 합니다.
# 사람 수(people)가 0명인 경우 에러 대신 0.0을 반환하세요.
# 정상인 경우 pizza_slices / people 결과를 반환합니다.
def divide_pizza(pizza_slices: int, people: int) -> float:
    # TODO: try - except ZeroDivisionError 구문을 사용하세요.
    pass


# 문제 3. 리스트 안전 조회 (IndexError 다루기)
# [상황] 요일 리스트(["월", "화", "수", "목", "금", "토", "일"])에서
# 사용자가 입력한 번호(index)의 요일을 꺼내옵니다.
# 범위를 벗어난 번호(예: 10, -8 등)를 넣으면 "잘못된 번호"를 반환하세요.
def get_day_of_week(index: int) -> str:
    days = ["월", "화", "수", "목", "금", "토", "일"]
    # TODO: try - except IndexError 구문을 사용하세요.
    pass


# 문제 4. 딕셔너리 키 조회 (KeyError 다루기)
# [상황] 과일 가격표 딕셔너리에서 특정 과일(fruit)의 가격을 조회합니다.
# 가격표에 없는 과일을 조회할 경우 에러 대신 "미등록 상품"을 반환하세요.
# (딕셔너리의 .get() 대신, try - except KeyError 문법을 직접 써보세요)
def get_fruit_price(price_table: dict, fruit: str):
    # TODO: try - except KeyError 구문을 사용하세요.
    pass


# 문제 5. 나이 검증기 (raise ValueError 활용하기)
# [상황] 놀이공원 회원가입 함수입니다.
# 전달받은 age가 0 미만이거나 150을 초과하면 잘못된 입력이므로
# 직접 ValueError("올바른 나이가 아닙니다")를 발생(raise)시키세요.
# 정상 범위라면 age를 그대로 반환합니다.
def validate_age(age: int) -> int:
    # TODO: if 조건문과 raise ValueError를 사용하세요.
    pass



# ==============================================================================
# PART 2. 파일 입출력 집중 연습 (문제 6 ~ 10)
# ==============================================================================

# 문제 6. 파일에 인사말 쓰기 ('w' 모드)
# [상황] name을 입력받아, file_path 파일에 "안녕하세요, {name}님!\n" 한 줄을 쓰세요.
# (기존 파일이 있으면 덮어씁니다. encoding="utf-8" 사용)
def write_greeting(file_path: str, name: str) -> None:
    # TODO: with open(..., "w", ...) 구문을 사용하세요.
    pass


# 문제 7. 파일 내용 전부 읽어오기 ('r' 모드)
# [상황] file_path에 있는 텍스트 파일을 열어 내용 전체를 하나의 문자열로 반환하세요.
# 단, 파일이 존재하지 않는 경우 FileNotFoundError를 처리하여 빈 문자열("")을 반환하세요.
def read_entire_file(file_path: str) -> str:
    # TODO: with open(..., "r", ...) 및 try-except를 사용하세요.
    pass


# 문제 8. 방명록 이어 쓰기 ('a' 모드)
# [상황] 기존 방명록 파일(file_path)의 맨 뒤에 새로운 메시지(message)를 덧붙입니다.
# 새 줄이 되도록 message 뒤에 줄바꿈("\n")을 붙여서 파일에 추가하세요.
def append_guestbook(file_path: str, message: str) -> None:
    # TODO: with open(..., "a", ...) 구문을 사용하세요.
    pass


# 문제 9. 파일의 줄 수 세기 (한 줄씩 읽기)
# [상황] 텍스트 파일(file_path)이 총 몇 줄로 이루어져 있는지 줄 수를 세어 반환하세요.
# 파일이 없으면 0을 반환합니다.
def count_file_lines(file_path: str) -> int:
    # TODO: with open 구문과 for line in f 반복문을 사용하세요.
    pass


# 문제 10. 파일에서 한 줄씩 꺼내주는 제네레이터 (yield)
# [상황] 파일(file_path)의 각 줄을 하나씩 꺼내면서,
# 양쪽 공백이나 줄바꿈을 제거(strip())한 문자열을 yield 하세요.
# 파일이 없으면 아무것도 yield 하지 않고 종료합니다.
def stream_file_lines(file_path: str):
    # TODO: yield를 사용하는 제네레이터 함수로 작성하세요.
    pass