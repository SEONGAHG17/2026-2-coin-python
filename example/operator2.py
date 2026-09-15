# is / is not
# 이터러블이 아닌 일반 숫자, None 등에서도 사용 가능
a = None
print(a is None)  # True

x = 10
y = 10
print(x is y)     # True (파이썬 내부 최적화로 소형 정수는 같은 메모리를 공유함)

"""
파이썬은 불변 객체(Immutable)인 정수 중에서도, 
프로그램에서 가장 자주 쓰이는 -5부터 256까지의 정수를 메모리에 미리 만들어 둡니다. 
이를 정수 인터닝(Integer Interning)이라고 합니다.

이유: 
0, 1, 10 같은 숫자는 루프(반복문)나 인덱싱 등에서 수없이 사용됩니다. 
이 숫자가 필요할 때마다 매번 메모리를 새로 할당하고 해제하면 컴퓨터에 큰 부담(오버헤드)이 됩니다.

불변 객체이기에 가능한 일: 
정수는 값이 절대 변하지 않는 '불변' 객체입니다. 
어떤 변수가 10을 가리키고 있든, 
그 변수를 통해 10이라는 값 자체를 11로 오염시킬 수 없습니다. 

따라서 안심하고 여러 변수가 같은 메모리 주소를 공유(재사용)해도 문제가 발생하지 않습니다.
"""

a = 256
b = 256
print(a is b)  # True (미리 만들어진 동일한 메모리 공유)

x = 257
y = 257
print(x is y)  # False (256을 넘어가면 필요할 때마다 새로 만듦)



# 리스트는 값이 같아도 별도의 메모리 공간에 생성됨
list_a = [1, 2, 3]
list_b = [1, 2, 3]
list_c = list_a

print(list_a == list_b)  # True  (값이 같으므로)
print(list_a is list_b)  # False (메모리 주소가 다르므로)
print(list_a is list_c)  # True  (같은 메모리 주소를 가리키므로)

print(list_a is not list_b) # True (서로 다른 객체가 맞으므로)


# in / not in 
# __contains__ 메서드가 구현된 객체에서만 가능 
# 일반 숫자(int, float)나 불리언(bool) 자료형에서는 사용할 수 없다 >> 타입에러 발생
# 문자열 및 리스트에서 확인
message = "Hello World"
fruits = ["apple", "banana", "cherry"]

print("Hello" in message)     # True
print("grape" in fruits)      # False
print("grape" not in fruits)  # True (포함되어 있지 않으므로)


# 증감연산자 
    # 파이썬에는 증감연산자가 없다
    # 타 언어에 존재
"""
public class Main {
    public static void main(String[] args) {
        
        // 1. 기본적인 증감
        int count = 10;
        count++; // count = count + 1; 과 같음
        System.out.println("기본 증가: " + count); // 11

        count--; // count = count - 1; 과 같음
        System.out.println("기본 감소: " + count); // 10

        System.out.println("------------------");

        // 2. 전위(Prefix) vs 후위(Postfix) 연산자의 차이
        int a = 5;
        int b = 5;

        // 후위 연산자 (b++): 현재 값을 먼저 대입하고, 나중에 변수 값을 1 증가시킴
        int resultPost = b++; 
        System.out.println("후위 연산 결과 -> resultPost: " + resultPost + ", b: " + b);
        // 출력: resultPost: 5, b: 6

        // 전위 연산자 (++a): 변수 값을 먼저 1 증가시키고, 그 결과를 대입함
        int resultPre = ++a; 
        System.out.println("전위 연산 결과 -> resultPre: " + resultPre + ", a: " + a);
        // 출력: resultPre: 6, a: 6
    }
}

"""

# 컨테이너 자료형 예제
# 


# 오름차순 / 내림차순 정렬
    # 리스트 메서드 .sort()

# 1. 숫자 오름차순 정렬 (기본값)
numbers = [3, 1, 4, 5, 2]
numbers.sort()
print(numbers)  # [1, 2, 3, 4, 5]

# 2. 내림차순으로 바꾸고 싶을 때 (reverse=True)
numbers.sort(reverse=True)
print(numbers)  # [5, 4, 3, 2, 1]

"""
원본을 직접 수정합니다 (In-place): 
새로운 정렬 리스트를 만드는 게 아니라, 
기존 리스트의 메모리 공간 안에서 순서만 뒤바꿉니다.

None을 반환합니다: 
원본을 바꾸고 끝나기 때문에, 
result = numbers.sort() 처럼 변수에 담으면 result에는 아무것도 담기지 않습니다.



"""



# 파이썬의 .sort()와 sorted()의 가장 핵심적인 차이는 
# "원본 리스트를 직접 수정하느냐(가변), 원본은 두고 새 리스트를 만드느냐(불변)"에 있습니다.
# .sort()는 오직 리스트에서만 쓸 수 있지만, 
# sorted()는 튜플, 문자열, 딕셔너리 같은 모든 이터러블(Iterable) 자료형에 사용할 수 있습니다. 
# 결과물은 무조건 리스트로 변환되어 나옵니다.

numbers = [3, 1, 4, 5, 2]

# 정렬된 새 리스트를 반환하므로 반드시 변수에 담아 사용합니다.
new_list = sorted(numbers)

print(numbers)   #  <- 원본은 안전하게 그대로 유지됨
print(new_list)  #  <- 정렬된 새 리스트가 생성됨

# 튜플 정렬하기 (튜플은 불변 객체라 .sort() 자체가 없음)
my_tuple = (5, 2, 4)
result_list = sorted(my_tuple)
print(result_list)  #  (리스트로 반환됨)

# 문자열 정렬하기
my_str = "python"
print(sorted(my_str))  # ['h', 'n', 'o', 'p', 't', 'y']


"""
.sort()는 가변 자료형 중에서도 오직 리스트(list)에서만 사용할 수 있는 메서드입니다.


딕셔너리는 순서가 아니라 'Key(키)'를 가지고 'Value(값)'를 찾는 자료형입니다.
 파이썬 3.7부터는 입력한 순서가 유지되긴 하지만, 
 리스트처럼 
인덱스([0], [1])로 접근하는 구조가 아니므로 내부를 직접 섞는 .sort() 메서드를 제공하지 않습니다.

세트는 수학의 '집합'을 구현한 자료형입니다. 
애초에 "순서가 없는(Unordered) 자료형"이기 때문에, 정렬이라는 개념 자체가 성립하지 않습니다. 
메모리 내부에서 해시 함수에 의해 무작위로 위치가 결정됩니다.


"""

# 1. 세트(set) 정렬하기
my_set = {3, 1, 4, 2}
# my_set.sort() -> ❌ 에러 발생 (AttributeError)

result = sorted(my_set)
print(result)  #  (정렬된 '리스트'로 반환됨)


# 2. 딕셔너리(dict) 정렬하기
my_dict = {"c": 30, "a": 10, "b": 20}

# 기본적으로 Key를 기준으로 오름차순 정렬하여 Key 리스트를 반환
print(sorted(my_dict))  # ['a', 'b', 'c']
