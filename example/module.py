import random

# 1. 시드 고정: 매번 실행해도 결과가 동일함을 확인
random.seed(42)

# 2. 가상 학생 10명의 성적 데이터 생성
student_ids = list(range(101, 111))
scores = [random.randint(40, 100) for _ in range(10)]
print("학생 ID:", student_ids)
print("초기 점수:", scores)

# 3. 비복원 추출: 장학생 3명 무작위 선발
selected_students = random.sample(student_ids, k=3)
print("장학생 후보 (중복 없음):", selected_students)

# 4. 데이터 셔플링 (In-place 수정)
data_pairs = list(zip(student_ids, scores))
random.shuffle(data_pairs)
print("셔플된 데이터 (상위 3개):", data_pairs[:3])




import math

# 1. 머신러닝의 대표 활성화 함수 '시그모이드(Sigmoid)' 직접 구현해보기
# 수식: 1 / (1 + e^(-z))
def sigmoid(z):
    return 1.0 / (1.0 + math.exp(-z))

# 2. 두 데이터 포인트 간의 유클리드 거리(Euclidean Distance) 계산
# 점 A(1, 2), 점 B(4, 6) 사이의 직선 거리
point_a = (1.0, 2.0)
point_b = (4.0, 6.0)

dist = math.sqrt(math.pow(point_a[0] - point_b[0], 2) + math.pow(point_a[1] - point_b[1], 2))
print(f"점 A와 점 B 사이의 거리: {dist:.2f}")

# 3. 로짓(z)에 따른 확률 출력 확인
test_z = 2.5
prob = sigmoid(test_z)
print(f"z={test_z}일 때 시그모이드 확률값: {prob:.4f}")

# 4. 부동소수점 비교 안전장치
val = 0.1 + 0.2
print("0.1 + 0.2 == 0.3 비교:", val == 0.3)                  # False
print("math.isclose()로 비교:", math.isclose(val, 0.3))      # True


import os

# 1. 현재 작업 경로 확인 (디버깅의 시작점)
current_dir = os.getcwd()
print("현재 실행 경로:", current_dir)

# 2. 운영체제에 안전한 하위 폴더 및 파일 경로 합성
data_dir = os.path.join(current_dir, "ml_dataset")
sample_file = os.path.join(data_dir, "sample.txt")

# 3. 폴더가 없을 경우 자동 생성 (머신러닝 전처리 파이프라인 필수 패턴)
if not os.path.exists(data_dir):
    os.makedirs(data_dir, exist_ok=True)
    print(f"'{data_dir}' 폴더를 새로 생성했습니다.")

# 4. 파일 쓰기 및 존재 여부 검사
with open(sample_file, "w", encoding="utf-8") as f:
    f.write("feature1,feature2,label\n1.2,3.4,0\n5.6,7.8,1\n")

if os.path.exists(sample_file):
    print(f"파일 확인 성공: {os.path.basename(sample_file)}")

# 5. 폴더 내 파일 목록 탐색 및 필터링 (.txt 확장자만 찾기)
entries = os.listdir(data_dir)
txt_files = [f for f in entries if f.endswith(".txt")]
print("ml_dataset 폴더 내 텍스트 파일 목록:", txt_files)