import datetime

# 1. 현재 날짜와 시간 가져오기 (메서드 호출 -> () 필요)
now = datetime.datetime.now()
print("현재 전체 시간:", now)

# 2. 특정 날짜/시간 단위 확인하기 (속성 접근 -> () 불필요)
print("연도:", now.year)
print("월:", now.month)
print("일:", now.day)

# 3. 날짜만 간단히 가져오기
today = datetime.date.today()
print("오늘 날짜:", today)

# 4. 날짜/시간 값 변경하기 (replace 메서드)
changed_date = now.replace(year=2030, month=1)
print("변경된 시간:", changed_date)


import time

# 1. 프로그램 실행 일시 정지 (sleep)
print("3초 동안 대기합니다...")
time.sleep(3)  # 실수 단위(예: 0.5)도 가능
print("대기 종료!")

# 2. 현재 시스템 시간을 시간 객체(struct_time)로 가져오기
current = time.localtime()

# 3. 시간 데이터를 원하는 문자열 형식으로 출력하기 (strftime)
# %Y: 4자리 연도, %m: 2자리 월, %d: 2자리 일, %H: 시간, %M: 분, %S: 초
formatted_time = time.strftime("%Y-%m-%d %H:%M:%S", current)
print("포맷팅된 시간:", formatted_time)


import math

# 1. 거듭제곱 (x의 y승, 결과는 float)
print("3의 3제곱:", math.pow(3, 3))        # 27.0

# 2. 절대값 반환 (float 반환)
print("-9.9의 절대값:", math.fabs(-9.9))    # 9.9

# 3. 올림과 내림
print("2.1 올림:", math.ceil(2.1))          # 3
print("2.1 내림:", math.floor(2.1))         # 2
print("-2.1 올림:", math.ceil(-2.1))        # -2 (음수 올림 주의)

# 4. 로그 계산 (math.log(진수, 밑))
print("밑이 10인 log(100):", math.log(100, 10))  # 2.0

import random

# 1. 0.0 이상 1.0 미만의 실수 난수
print("실수 난수:", random.random())

# 2. 정수 난수 (끝값 포함 여부 주의)
print("1 이상 10 미만 정수:", random.randrange(1, 10))  # 10 미포함
print("1 이상 10 이하 정수:", random.randint(1, 10))    # 10 포함

# 3. 시퀀스(리스트) 조작
fruits = ["사과", "바나나", "포도", "딸기", "오렌지"]

# 원소 1개 랜덤 선택
print("랜덤 선택 1개:", random.choice(fruits))

# 중복 없이 k개 랜덤 추출
print("랜덤 추출 3개:", random.sample(fruits, 3))

# 원본 리스트 순서 무작위로 섞기 (반환값 없음, 원본 변경)
random.shuffle(fruits)
print("순서 섞인 리스트:", fruits)

import sys

# 1. 파이썬 설치 경로 및 버전 정보 확인
print("파이썬 설치 위치:", sys.prefix)
print("파이썬 버전:", sys.version)

# 2. 모듈을 검색하는 경로 목록 (리스트 형태로 출력)
print("모듈 검색 경로(sys.path):")
for path in sys.path:
    print(path)

# [연계 실습] 파일 커서 제어 (seek 메서드)
# whence: 0(파일 시작 기준), 1(현재 위치 기준), 2(파일 끝 기준)
with open("test.txt", "w+") as f:
    f.write("HelloWorld")
    
    # 파일 시작 위치(0)에서 5바이트 뒤로 이동
    f.seek(5, 0)
    print("5바이트 이동 후 읽은 내용:", f.read())  # 'World' 출력
    
    import os

# 1. 현재 작업 디렉터리(Current Working Directory) 확인
current_dir = os.getcwd()
print("현재 실행 폴더:", current_dir)

# 2. 현재 폴더에 있는 파일 및 폴더 목록 조회
file_list = os.listdir(".")
print("폴더 내 목록:", file_list)

# 3. 새로운 폴더 생성 및 삭제
folder_name = "practice_folder"
if not os.path.exists(folder_name):
    os.mkdir(folder_name)
    print(f"'{folder_name}' 폴더가 생성되었습니다.")

# 4. 운영체제 맞춤형 안전한 파일 경로 결합 (os.path.join)
# Windows는 '\', Mac/Linux는 '/'로 자동 처리해 줌
safe_path = os.path.join(current_dir, folder_name, "data.txt")
print("안전한 경로 생성:", safe_path)

# 5. 생성했던 빈 폴더 삭제
if os.path.exists(folder_name):
    os.rmdir(folder_name)
    print(f"'{folder_name}' 폴더가 삭제되었습니다.")
    
    