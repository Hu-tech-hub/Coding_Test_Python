## 2. list comprehension을 활용하여 1 ~ 100까지 수 중, 3과 9의 공배수인 수만 리스트에 담기도록 구현하라.

lst = [i for i in range(1, 101) if i % 9 == 0]

print(lst)


# 번외

# 두 숫자를 입력받아 공배수를 구하는 코드
def find_common_multiples(a, b):
    lcm = (a * b) // gcd(a, b)  # 최소공배수 구하기 : 두 수의 곱 / 최소공약수
    return [i for i in range(lcm, 101, lcm)]

# 최대공약수(GCD) 구하는 함수 : 유클리드 호제법
def gcd(x, y):
    while y:
        x, y = y, x % y
    return x

# 사용자로부터 입력받기
num1 = int(input())
num2 = int(input())

# 공배수 찾기
common_multiples = find_common_multiples(num1, num2)

print(f"{common_multiples}")

