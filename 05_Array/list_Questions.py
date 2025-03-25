# p.102 
# 문제 1) 배열 정렬하기

# 정수 배열을 정렬해서 반환하는 solution() 함수 완성

def solution(lst):
    lst_2 = sorted(lst)
    return lst_2

lst = [6, 3, 5, 2]

print(solution(lst))

## 메소드 sort는 기존의 lst를 변환시킴
## 내장 함수 sorted는 기존을 함수를 변환시키지 않고 리스트 객체 반환

## 버블 정렬은 O(N^2)
def bubble(lst):
    n = len(lst)
    for i in range(n):
        for j in range(n - i - 1):
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
    
    return lst

lst = [6, 3, 5, 2]

print(bubble(lst))

# 문제 2) 배열 제어하기

# Q. 정수 배열을 입력 받은 후, 배열의 중복값을 제거하고 
# 배열 데이터를 내림차순으로 정렬해서 반환하는 solution() 함수 구현

# KeyWord : 중복값 제거(set()), 내림차순 정렬(sort(False))

# 리스트 입력 lst = list(map(int, input().split()))

lst = [4, 2, 2, 1, 3, 4]

def solution(lst):
    lst = list(set(lst)) # O(N)
    lst.sort(key=None, reverse=True) # O(NlogN)
    return lst

print(solution(lst))

# 복잡도 : O(NlogN)

# set()이 해시 알고리즘으로 중복값을 제거하므로 O(N) 보장.

# 문제 3)

# Q. 정수 배열이 주어짐. 서로 다른 인덱스에 있는 2개의 수를 뽑아 더해 만들 수 있는 모든 수를
# 배열에 오름 차순으로 담아 반환하는 solution 함수

# Keyword : (0 ~ n)에서 2개 조합 <- O(N^2)

number = [2, 1, 3, 4, 1]
n = len(number)
lst = []

for i in range(n - 1):
    for j in range(i + 1, n):
        lst.append(number[i] + number[j])  #O(N^2)

lst = sorted(list(set(lst))) #O(N^2logN^2)

print(lst)

# 문제 4)

# Q. 수포자는 수학을 포기한 사람들의 줄임말입니다. 수포자 삼인방은 모의고사에 수학 문제를 
# 전부 찍으려 합니다. 수포자는 1번 문제부터 마지막 문제까지 다음과 같이 찍습니다.

# 1번 문제부터 마지막 문제까지 정답이 순서대로 저장된 배열 answers 가 주어졌을 때
# 가장 많은 문제를 맞힌 사람이 누구인지 배열에 담아 반환하는 solution() 

# Keyword: 두 배열간 일치 여부 판단. zip(), 
#          answer의 길이에 따라 first, second, third의 길이 변화


# 내가 짠 코드

answer = [1, 2, 3, 4, 5, 6, 7, 8]


def func(lst, answer):
    n = len(answer)
    m = len(lst)
    k = n // m
    j = n % m
    lst = lst * k + lst[:j] 
    return lst


def func_2(lst, answer):
    score = 0
    for i, j in zip(lst, answer):
        if i == j:
            score += 1

    return score

def get_max_indices(scores):
    max_score = max(scores)
    return [i + 1 for i, score in enumerate(scores) if score == max_score]


def solution(answer):
    value = [[1, 2, 3, 4, 5], 
             [2 ,1, 2, 3, 2, 4, 2, 5], 
             [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]]

    scores = [0] * 3

    for i in range(3):
        lst = func(value[i], answer)
        scores[i] = func_2(lst, answer)
    
    lst_2 = get_max_indices(scores)

    return lst_2

print(solution(answer))



# 정답 코드

def solution(answer):
    pattern = [[1, 2, 3, 4, 5], 
             [2 ,1, 2, 3, 2, 4, 2, 5], 
             [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]]
    














