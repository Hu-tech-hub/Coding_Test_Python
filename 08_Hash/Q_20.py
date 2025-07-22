# 시간복잡도 분석:
# participant.remove(i)는 리스트에서 i를 찾고 삭제하므로 O(n)입니다.
# completion의 길이가 m이라면, 전체 복잡도는 O(m * n)입니다.
# (n: participant 길이, m: completion 길이. 보통 m = n-1)
# 즉, 이 코드는 O(n^2)입니다.

def solution(participant, completion):
    for i in completion:
        participant.remove(i)  # O(n) 연산이므로 전체 O(n^2)
    return participant[0]

participant = ["leo", "kiki", "eden"]
completion = ["eden", "kiki"]

print(solution(participant, completion))

# 딕셔너리를 사용하여 시간목잡도 개선
def solution_hash(participant, completion):
    d = {}
    for p in participant:
        d[p] = d.get(p, 0) + 1
    for c in completion:
        d[c] -= 1
    for k, v in d.items():
        if v > 0:
            return k

# 테스트
participant = ["leo", "kiki", "eden"]
completion = ["eden", "kiki"]
print(solution_hash(participant, completion))

