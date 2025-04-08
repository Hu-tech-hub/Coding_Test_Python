# 문제 8. 괄호 짝 맞추기

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

# 문제 10. 괄호 회전하기

# 특정 값이 바로 앞의(최근의) 값과 '관계성'이 존재할 때, Stack을 사용해야 함.
# 이 문제에서는 앞서 말한 괄호 짝 맞추기를 응용한 문제임.
# 문자열을 회전을 시켜서 올바른 괄호인지 확인한 후 x 번의 회전 동안 몇 번 올바른 괄호가 되는지 확인하는 것이 관건.

# 앞선 문제에서는 단순히 가장 첫 문자부터 append 되었다면 이 문제에서는 회전을 고려해서 append.

def solution(s):
    score = 0
    for i in range(len(s)):
        lst = s[i:] + s[:i]
        stack = []
        top = -1

        for c in lst:
            if c in ('(', '{', '['):
                stack.append(c)
                top += 1
            elif top >= 0:
                if ( c == ')' and stack[top] == '(' ) or ( c == '}' and stack[top] == '{' ) or ( c == ']' and stack[top] == '[' ):
                    stack.pop()
                    top -= 1
            else: 
                stack.append(c)
                break

        if not stack:
            score += 1

    return score

## 정답

## 문제 12 주식 가격

## Q. 초 단위로 기록된 가격이 담긴 배열 Price가 매개변수로 주어질 때, 가격이 떨어지지 않는 기간은 몇 초인지 반환하도록 solution() 함수를 완성하세요.

## +. price의 각 가격은 1 이상 10000 이하인 자연수이다. 길이는 2이상 10000 이하이다.
# 
prices = list(map(int, input().split()))

def solution(prices):
    top = -1
    stack = []
    return_lst = [0] * len(prices)

    for i in range(len(prices)):
        while True:
            if not stack:
                stack.append(i)
                top += 1
                break
            elif prices[top] > prices[i]:
                return_lst[stack[top]] = i - stack[top]
                stack.pop()
                top -= 1
            else:
                stack.append(i)
                top += 1
                break

    for i in stack:
        return_lst[i] = len(prices) - i - 1
    
    return return_lst


print(solution(prices)) 

## 문제 13 


board = [[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]]
moves = [1,5,3,5,1,2,1,4]
score = 0

n = len(board)
m = len(board[0])
stack = []
result = []

for j in range(m):
    lst = [board[i][j] for i in range(n -1, -1, -1) if board[i][j] != 0]
    stack.append(lst)

print(stack)

moves = [i - 1 for i in moves]

for i in moves:
    if not stack[i]:
        continue
    elif len(result) != 0:
        if stack[i][-1] == result[-1]:
            result.pop()
            score += 2
            stack[i].pop()
        else:
            result.append(stack[i][-1])
            stack[i].pop()
    else:
        result.append(stack[i][-1])
        stack[i].pop()


print(result, score)





    
