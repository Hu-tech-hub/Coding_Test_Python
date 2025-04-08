def solution(n, k, cm):
    # 각각의 행이 가리키는 위와 아래 인덱스를 설정 (링크드 리스트 방식)
    up = {i: i - 1 for i in range(n)}
    down = {i: i + 1 for i in range(n)}
    down[n - 1] = -1  # 마지막 노드의 아래는 존재하지 않음
    
    stack = []  # 삭제된 행을 기록하는 스택

    for command in cm:
        if command[0] == 'D':  # 아래로 이동
            num = int(command[1:])
            for _ in range(num):
                k = down[k]

        elif command[0] == 'U':  # 위로 이동
            num = int(command[1:])
            for _ in range(num):
                k = up[k]

        elif command == 'C':  # 삭제 명령어
            stack.append((k, up[k], down[k]))  # 현재 커서 위치와 연결 정보 저장

            if up[k] != -1:  # 삭제된 행의 위쪽 연결 갱신
                down[up[k]] = down[k]

            if down[k] != -1:  # 삭제된 행의 아래쪽 연결 갱신
                up[down[k]] = up[k]

            # 삭제 후 커서 위치 이동 (아래로 이동, 없으면 위로 이동)
            k = down[k] if down[k] != -1 else up[k]

        elif command == 'Z':  # 복구 명령어
            restore, prev, nxt = stack.pop()  # 스택에서 삭제된 행 정보 복구

            if prev != -1:  # 위쪽 노드의 아래를 복구된 행으로 설정
                down[prev] = restore

            if nxt != -1:  # 아래쪽 노드의 위를 복구된 행으로 설정
                up[nxt] = restore

    # 최종 결과 테이블 생성
    result = ['O'] * n

    print(stack)
    
    while stack:
        idx, _, _ = stack.pop()
        result[idx] = 'X'

    return ''.join(result)

n = 8
k = 2
cm = ['D2', 'C', 'U3', 'C', 'D4', 'C', 'U2', 'Z', 'Z']

print(solution(n, k, cm))