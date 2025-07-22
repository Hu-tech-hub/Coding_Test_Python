# 시간복잡도 분석:
# - want의 길이를 n, discount의 길이를 m이라고 하자.
# - want_dict, dic 초기화: O(n)
# - 첫 10일치 dic 채우기: O(10)
# - 슬라이딩 윈도우 루프: (m-10)번 반복
#   - 각 반복마다 dic에서 상품 1개 빼고, 1개 더함: O(1)
#   - dic == want_dict 비교: O(n) (딕셔너리 크기 n)
#   => 전체 루프 복잡도: O((m-10) * n)
# - 최종 시간복잡도: O(n + m*n)

# 슬라이딩 윈도우에서 매번 윈도우 범위의 모든 값을 새로 세는 방식은, 윈도우 크기가 k일 때 각 이동마다 O(k) 시간이 듭니다.
# 하지만 앞에서 빠지는 값 1개, 뒤에서 새로 들어오는 값 1개만 갱신하면 O(1)만에 윈도우 상태를 업데이트할 수 있습니다.
# 즉, 슬라이딩 윈도우에서 "앞 뒤를 빼고 더하는 방식"이 "매번 새로 세는 방식"보다 훨씬 효율적입니다.

def solution(want, number, discount):
    dic = {}
    want_dict = {}
    for i in range(len(want)):
        want_dict[want[i]] = number[i]
        
    # 첫 10일치 상품 개수 세기
    for i in range(10):
        if discount[i] in want_dict:
            dic[discount[i]] = dic.get(discount[i], 0) + 1

    n = 1 if dic == want_dict else 0

    # 슬라이딩 윈도우: 앞에서 빠지는 상품 1개, 뒤에서 들어오는 상품 1개만 갱신
    for i in range(len(discount) - 10):
        if discount[i] in want_dict:
            dic[discount[i]] -= 1
        if discount[i + 10] in want_dict:
            dic[discount[i + 10]] = dic.get(discount[i + 10], 0) + 1
        if dic == want_dict:
            n += 1

    return n


print(solution(
  ["apple"],
  [10],
  ["banana", "banana", "banana", "banana", "banana", "banana", "banana", "banana", "banana", "banana"]
  ))
        
  
    

  



