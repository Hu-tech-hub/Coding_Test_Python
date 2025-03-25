#Q8. 괄호 짝 맞추기

# 소괄호는 작을 맞춘 열린 괄호 '(' 와 닫힌 괄호 ')'로 구성합니다. 문제에서는 열린 괄호나 닫힌 괄호가 마구 뒤섞인 문자열을 줍니다.
# 이때 소괄호가 정상으로 열고 닫혔는지 판별하는 solution을 작성하세요.
# 예를 들어, "(()())"는 정상으로 열고 닫혔지만, "(()"는 정상으로 열고 닫히지 않았습니다.


def solution(s):
    stack = []
    for char in s:
        if char == '(':
            stack.append(char)
        elif char == ')':
            if not stack:
                return False
            stack.pop()
    return len(stack) == 0

print(solution("(()())"))  # True

# 문제 10

    