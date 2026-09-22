"""
================================================================================
파이썬 파일 입출력(File I/O) 단계별 실습
================================================================================
  STEP 1. 파일 새로 만들기 ('w' 모드) -> 탐색기에서 파일 생성 확인
  STEP 2. 만든 파일 읽어오기 ('r' 모드 3가지 방식: read, readline, readlines)
  STEP 3. 없는 파일 읽기 시도 -> FileNotFoundError 예외 처리 연결
  STEP 4. 기존 내용 뒤에 덧붙이기 ('a' 모드 vs 'w' 모드 덮어쓰기 주의점)
  STEP 5. close() 자동화: with open(...) as 문으로 전환
================================================================================
"""

# ==============================================================================
# STEP 1. 파일 새로 만들기 ('w' 모드: Write)
# ==============================================================================
# - 파일 사용 3단계: 1) 열기(open) -> 2) 사용 -> 3) 닫기(close)
# - open(파일 경로, 모드, encoding="utf-8")
# - 'w' 모드는 파일이 없으면 새로 만들어주고, 있으면 덮어씁니다.
# - .write() 메서드는 자동으로 줄바꿈이 되지 않으므로 끝에 '\n'을 직접 붙여야 합니다.

print("=" * 60)
print("[STEP 1] 'w' 모드로 파일 새로 만들기")
print("=" * 60)

# 1. 파일 열기
f = open("sample.txt", "w", encoding="utf-8")

# 2. 내용 쓰기
f.write("안녕하세요! 파이썬 파일 처리 첫 시간입니다.\n")
f.write("두 번째 줄: 데이터를 파일에 영구 보관합니다.\n")
f.write("세 번째 줄: .write()는 자동 줄바꿈이 안 되니 \\n이 필수입니다.\n")

# 3. 파일 닫기 (시스템 자원 반환)
f.close()

print(">> 'sample.txt' 파일이 생성되었습니다! 탐색기/폴더를 확인해 보세요.\n")
input("엔터를 누르면 다음 단계(읽기 모드)로 넘어갑니다...")


# ==============================================================================
# STEP 2. 파일 읽어오기 ('r' 모드: Read)
# ==============================================================================
# [강의 포인트]
# - 자료에 나오는 세 가지 읽기 메서드 직접 비교:
#   1) .read()      : 파일 전체를 하나의 통 문자열(str)로 읽기
#   2) .readline()  : 한 줄씩 가져오기 (줄바꿈 문자 '\n' 포함)
#   3) .readlines() : 모든 줄을 리스트(list[str])로 한 번에 가져오기

print("\n" + "=" * 60)
print("[STEP 2] 'r' 모드로 파일 읽기 (3가지 메서드 비교)")
print("=" * 60)

# 1) .read() 전체 읽기
print("--- [1] .read() 전체 읽기 ---")
f = open("lecture_sample.txt", "r", encoding="utf-8")
content = f.read()
print(content)
f.close()

# 2) .readline() 한 줄씩 읽기
print("--- [2] .readline() 한 줄씩 읽기 ---")
f = open("lecture_sample.txt", "r", encoding="utf-8")
line1 = f.readline()
line2 = f.readline()
print("첫 번째 읽은 줄:", line1.strip()) # .strip()으로 끝의 \n 정리
print("두 번째 읽은 줄:", line2.strip())
f.close()

# 3) .readlines() 전체 줄을 리스트로 읽기
print("\n--- [3] .readlines() 리스트로 읽기 ---")
f = open("lecture_sample.txt", "r", encoding="utf-8")
lines = f.readlines()
print("반환된 타입:", type(lines))
print("리스트 내용:", lines)
for idx, line in enumerate(lines, start=1):
    print(f"  {idx}행: {line.strip()}")
f.close()

print()
input("엔터를 누르면 다음 단계(예외 처리 연결)로 넘어갑니다...")


# ==============================================================================
# STEP 3. 없는 파일 읽기와 예외 처리 (FileNotFoundError)
# ==============================================================================
# - 'w' 모드는 파일이 없으면 만들어주지만, 'r' 모드는 파일이 없으면 즉시 에러 발생!
# - 앞서 배운 try - except 문법과 FileNotFoundError 내장 예외를 연결하여 설명

print("\n" + "=" * 60)
print("[STEP 3] 없는 파일 접근 시 예외 처리 (FileNotFoundError)")
print("=" * 60)

target_file = "non_existent_data.txt"

try:
    f = open(target_file, "r", encoding="utf-8")
    data = f.read()
    f.close()
except FileNotFoundError:
    print(f"[예외 감지] '{target_file}' 파일이 컴퓨터에 존재하지 않습니다!")
    print(">> 프로그램이 다운되지 않고 안전하게 예외 블록을 통과했습니다.")

print()
input("엔터를 누르면 다음 단계(이어 쓰기 모드)로 넘어갑니다...")


# ==============================================================================
# STEP 4. 내용 덧붙이기 ('a' 모드: Append)
# ==============================================================================
# - 만약 기존 파일이 있는 상태에서 'w' 모드로 열면 기존 데이터가 다 날아감(덮어쓰기)!
# - 기존 내용을 보존하면서 뒤에 이어 붙이려면 'a' 모드를 써야 함

print("\n" + "=" * 60)
print("[STEP 4] 'a' 모드로 방명록 이어 쓰기")
print("=" * 60)

# 'a' 모드로 파일 열기
f = open("sample.txt", "a", encoding="utf-8")
f.write("네 번째 줄: 'a' 모드로 새 내용을 덧붙였습니다.\n")
f.close()

# 덧붙여진 결과 확인
f = open("sample.txt", "r", encoding="utf-8")
print(f.read())
f.close()

input("엔터를 누르면 다음 단계(with open 문법)로 넘어갑니다...")


# ==============================================================================
# STEP 5. 자원 관리 자동화: with open(...) as 문
# ==============================================================================
# - 매번 open() 하고 close()를 적는 건 번거롭고, 실수로 까먹기 쉽다.
# - 중간에 에러가 나면 close()가 호출되지 않는 문제 발생.
# - 'with ... as ...' 문을 쓰면 블록이 끝날 때 파이썬이 알아서 f.close()를 실행해 줌!
# - 자료 32페이지 예제: with open("hello.txt", "w") as f:

print("\n" + "=" * 60)
print("[STEP 5] with 문을 사용한 안전하고 깔끔한 파일 처리")
print("=" * 60)


with open("sample_hello.txt", "w", encoding="utf-8") as f:
    f.write("hello World!\n")
    f.write("with 문을 사용하면 close()를 직접 쓰지 않아도 됩니다.\n")

print(">> 'sample_hello.txt' 작성 완료 (f.close() 자동 수행됨)")

# with 문으로 읽기
print("\n--- 'sample_hello.txt' 내용 읽기 ---")
with open("sample_hello.txt", "r", encoding="utf-8") as f:
    for line in f:
        print("내용:", line.strip())

"""
절대경로로 만들기
"""

# 주소 지정해서 파일 생성하기
path = 'C:/Users/sah/Desktop/2602-python/dayclass/fileFolder'
file_name = 'my_note.txt'

# 폴더 경로와 파일 이름을 합쳐 전체 파일 경로 생성
full_path = path + '/' + file_name


# 2. 지정한 위치에 파일 생성 및 내용 쓰기 ('w' 모드)
with open(full_path, "w", encoding="utf-8") as f:
    f.write("지정된 폴더에 성공적으로 저장된 파일입니다.\n")
    f.write("두 번째 줄 내용도 잘 들어갔습니다.\n")

print(f">> 파일 생성 완료: {full_path}")


# 3. 같은 위치의 파일 열어서 내용 읽기 ('r' 모드)
print("\n--- 파일 내용 읽기 결과 ---")
with open(full_path, "r", encoding="utf-8") as f:
    content = f.read()
    print(content)


print("\n" + "=" * 60)
print("파일 입출력 실습 시연이 모두 끝났습니다!")
print("=" * 60)


