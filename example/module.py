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