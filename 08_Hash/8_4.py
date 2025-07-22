def solution(arr, target):
    # 평가:
    # - 시간 복잡도 O(n + k)로 잘 풀었음. (n: arr 길이, k: arr 값의 범위)
    # - arr의 각 원소를 해시(set)에 저장하고, 각 원소에 대해 (target - 원소)가 해시 테이블에 있는지 확인하는 방식은 효율적임.
    # - 자기 자신과의 합을 허용하지 않으려면, 탐색 시 해당 원소를 잠시 해시에서 빼는 방식도 적절함.
    # - dict.fromkeys와 pop을 활용한 점도 좋으나, keys를 1부터 arr[-1]까지 생성하는 부분은 arr에 0이나 음수가 있을 때 문제가 될 수 있음.
    # - set(arr)로 바로 해시를 만드는 것이 더 안전함.
    # - 전체적으로 시간 복잡도와 해시 활용 모두 적절하게 잘 구현함.

    n = len(arr)
    keys = list(range(1, arr[-1] + 1))
    d = dict.fromkeys(keys, 0)
    for i in arr:
      d[i] = 1
    while n:
      A = target - arr[n-1]
      d.pop(arr[n-1])
      if d.get(A):
        return True
      d[arr[n-1]] = 1
      n -= 1
    return False

arr = [2, 3, 5, 9]
target = 10

print(solution(arr, target))

# ===== 정답지 =====
# 조건: arr은 양의 정수로 이루어진 오름차순 리스트, target은 정수
# 합이 target인 두 수가 arr에 있는지 찾고 있으면 True, 없으면 False 반환

# set의 in 연산은 평균적으로 O(1)입니다. 
# 따라서 arr을 n번 반복하면서 set에서 in 연산을 해도 전체 시간복잡도는 O(n)입니다.
# (최악의 경우 해시 충돌이 많으면 O(n^2)까지 갈 수 있지만, 일반적으로는 O(n)으로 간주합니다.)
def solution_answer(arr, target):
    s = set(arr)
    for num in arr:
        s.remove(num)  # O(1)
        if (target - num) in s:  # O(1)
            return True
        s.add(num)  # O(1)
    return False

# 예시 테스트
arr = [2, 3, 5, 9]
target = 10
print(solution_answer(arr, target))  # True

# === 정답지 ====
def solution(arr, target):
  # 해시 테이블 초기화. arr에서 target 이하의 값만 취급함.
  hash_table = [0] * (target + 1)
  
  # 해시 테이블에 값을 추가함. 존재하면 1, 없으면 0
  for i in arr:
    if i <= target:
      hash_table[i] = 1
  
  for i in arr:
    # 예외 처리 (자기 자신과의 합을 허용하지 않음)
    if hash_table[target - i] == i:
      continue
    
    # 예외 처리 target보다 같거나 큰 값을 처리하지 않음
    if i >= target:
      continue
    
    if hash_table[target - i] == 1:
      return True
    
  return False