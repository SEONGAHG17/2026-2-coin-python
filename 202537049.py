# 1번 문항 : 2번
기본키
	- 널값을 허용하지 않는다
    - 자동으로 외래키가 생성되는 것은 아니다
    	- 외래키는 타 테이블에서 참조할 때 직접 정의해야한다
    - 기본키 외 여러개의 유니크 제약조건을 추가로 정의 가능하다
    

기본키는 테이블 내 각 행을 고유하기 식별하는 식별자로, 중복 불가와 널 값 불가의 제약을 지닌다
테이블 당 1개만 지정할 수 있다

# 2번 문항 : 2번
- 데이터 검색속도 향상 : 인덱스의 장점
- select문의 조회 성능 향상 : 인덱스의 장점
- 데이터 분포도, 잘못된 쿼리 조건, 잦은 변경 작업에 따라 인덱스가 오히려 오버해드를 유발할 가능성 내재.
  항상 모든 쿼리의 성능 향상을 보장하지 않는다

인덱스는 데이터 검색속도를 높이기 위해 정렬된 구조이다
그러나 추가, 업데이터, 삭제 작업 시 인덱스 트리도 재구성되야 해 쓰기 성능이 저하되고 추가 공간이 필요하다

# 3번 문항 : 2번
- with read only : 뷰를 통한 작업 자체를 완전히 금지하는 옵션
뷰를 생성할 때 인덱스가 자동으로 생성되지 않는다
시퀸스는 with check opinion과 관련이 없다

with check opinion : 뷰를 정의할 때 지정한 where조건 절을 만족하는 데이터만 뷰를 통해 삽입 또는 갱신 할 수 있도록 강제하는 옵션

# 4번 문항 : 2번
PUBLIC SYNONYM : 모든 사용자가 공유해 접근 가능한 별명
PRIVATE SYNONYM : 특정 사용자만 접근 가능한 것

원본 테이블이 상제되어도 SYNONYM 객체 자체가 자동으로 삭제되지 않는다. 무효화 상태로 남게 됨

# 5번 문항 : 2번 
- 테이블 : 실제 데이터를 행과 열 형태로 저장하는 가장 기본적인 저장단위
- 뷰 : 가상의 논리적 테이블. 
- 시노님 : 객체에 접근하기 위한 대체 별칭
- 인덱스 : 데이터 조회하는 속도 향상을 위해 사용됨 


# 6번 문항 : 1번
- 시퀸스의 cache 옵션은 시퀸스 값을 메모리에 저장해 성능을 향상시킨다
- 시퀸스의 정의 자체는 딕셔너리에 저장되나, cache옵셔ㄴ은 영구저장이 아닌 메모리에 번호를 미리 올리는 방식
- 시퀸스 값을 함호화 하는 방식은 제공하지 않는다

# 7번 문항 : 2번
파티션 : 테이블에 있는 특정 컬럼 값을 기준으로 데이터를 분할해 저장해 놓은 것
파티션 테이블을 만드는 목적 : 대용량의 테이블의 경우 데이터 조회 시 효율성과 성능을 높이기 위한 것

# 8번 문항 : 3번
- 특정 열에 고유한 값 보장 : 유니크키, 기본키의 제약조건이다
- 참조 무결성 유지 : 외래키의 제약 조건

CHECK 제약 조건 : 열에 입력될 수 있는 값의 허용범위, 특정 논리 조건을 정의해 유효하지 않은 데이터의 유입을 방지하는 것

# 9번 문항
CREATE TABLE emp (
    emp_id NUMBER PRIMARY KEY,
    emp_name VARCHAR2(50) NOT NULL,
    dept_id NUMBER,
    salary NUMBER CHECK (salary >= 0)
);

# 10번문항
CREATE TABLE dept (
    dept_id NUMBER PRIMARY KEY,
    dept_name VARCHAR2(50) NOT NULL
);

# 11번문항
ALTER TABLE emp
ADD CONSTRAINT fk_emp_dept FOREIGN KEY (dept_id)
REFERENCES dept (dept_id);

# 12번문항
ALTER TABLE emp
ADD CONSTRAINT uk_emp_name UNIQUE (emp_name);

# 13번문항
CREATE SEQUENCE emp_seq
START WITH 1
INCREMENT BY 1;

# 14번문항
ALTER SEQUENCE emp_seq
INCREMENT BY 2
MAXVALUE 1000
CYCLE;

# 15번문항
CREATE INDEX idx_emp_comp ON emp (emp_id, emp_name);

# 16번문항
CREATE PUBLIC SYNONYM emps FOR employees;

# 17번문항
CREATE TABLE emp_backup AS
SELECT * FROM employees;

# 18번문항
CREATE VIEW high_salary_view AS
SELECT *
FROM employees
WHERE salary >= 12000
WITH CHECK OPTION;











