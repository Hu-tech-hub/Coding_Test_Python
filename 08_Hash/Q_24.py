# 시간복잡도 분석:
# - id_list의 길이를 n, report의 길이를 m이라고 하자.
# - report_dic 생성: report를 한 번 순회 (O(m)), 각 split, set 변환 포함
#   - set 변환이 중복 제거에 O(r) (r: 각 유저별 신고자 수, 최악 O(m)), 전체 O(m^2) 가능
#   - 하지만 report는 중복 신고가 있을 수 있으므로, set을 한 번만 쓰는 게 더 효율적임
# - result_dic 초기화: O(n)
# - report_dic 순회: O(nk) (최악 O(n^2)), 각 신고자에 대해 카운트 증가
# - 최종적으로 result_dic.values(): O(n)
# => 전체 시간복잡도: O(m^2) (set 변환이 루프 안에 있음), 공간복잡도: O(n + m)

def solution(id_list, report, k):
    # report의 중복을 제거하여 한 번만 처리
    report_set = set(report)  # O(m)
    report_dic = {}
    for r in report_set:      # O(m)
        A, B = r.split()
        if B not in report_dic:
            report_dic[B] = []
        report_dic[B].append(A)
    # report_dic: {신고당한ID: [신고자ID, ...]}
    # report_dic 생성: O(m)
    # 각 유저별 신고자 수 확인 및 메일 발송 카운트
    result_dic = dict.fromkeys(id_list, 0)  # O(n)
    for id in report_dic:
        if len(report_dic[id]) >= k:
            for reporter in report_dic[id]:
                result_dic[reporter] += 1   # O(nk) (최악 O(n^2))
    # 결과 반환: id_list 순서대로
    result = [result_dic[user] for user in id_list]  # O(n)
    return result

# 테스트
print(solution(
    ["muzi", "frodo", "apeach", "neo"],
    ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"],
    2
))

# 시간복잡도 요약:
# - report의 중복 제거: O(m)
# - report_dic 생성: O(m)
# - 신고자 카운트: O(nk) (최악 O(n^2))
# - 전체: O(m + n^2) (m: 신고 수, n: 유저 수)
      