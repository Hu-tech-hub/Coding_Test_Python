# 문제 15
# 요세푸스 문제 
# 난이도 : 2
# 문제 설명:
# 1부터 n까지의 숫자가 원형으로 연결되어 있다. 
# k번째 사람을 제거하는 과정을 반복하여 마지막 남은 사람을 찾는 문제이다.

from collections import deque

def solution(n, k): # n은 사람의 수, k는 제거할 사람의 번호 <- O(n*k)
    queue = deque(range(1, n + 1))  # 1부터 n까지의 숫자를 큐에 넣는다.

    while len(queue) > 1:
        for _ in range(k - 1):
            queue.append(queue.popleft())  # k-1번 앞의 사람을 뒤로 보낸다.
        queue.popleft()  # k번째 사람을 제거한다.

    return queue[0]  # 마지막 남은 사람을 반환한다.

print(solution(7, 3))  # 4

#문제 16 기능 개발
# 난이도 : 2

def solution(progresses, speeds):
    queue = deque()
    answer = []
    val = 0
    for progress, speed in zip(progresses, speeds):
        progress = 100 - progress
        if progress % speed == 0:
            queue.append(progress // speed)
        else:
            queue.append(progress // speed + 1)
    while queue:
        i = queue.popleft()
        val = 1

        if not queue:
            answer.append(val)
            break
        
        while queue and queue[0] <= i:
            queue.popleft()
            val += 1
        
        answer.append(val)

    return answer

print(solution([93, 30, 55], [1, 30, 5]))  # [2, 1]
print(solution([95, 90, 99, 99, 80, 99], [1, 1, 1, 1, 1, 1])) # [1, 3, 2]
print(solution([99, 1, 1], [1, 1, 1])) # [1, 2]
print(solution([99, 99, 99], [1, 1, 1])) # [3]

# 문제 17 
# 카드 뭉치
# 난이도 : 2

def solution(cards1, cards2, goal):
    queue1 = deque(cards1)
    queue2 = deque(cards2)

    for i in goal:
      
        if queue1 and i == queue1[0]:
            queue1.popleft()
        elif queue2 and i == queue2[0]:
            queue2.popleft()
        else:
            return "No"
        
    return "Yes"

print(solution(["i", "drink", "water"], ["want", "to"], ["i", "want", "to", "drink", "water"]))  # Yes
print(solution(["i", "water", "drink"], ["want", "to"], ["i", "want", "to", "drink", "water"]))  # No


from collections import deque

def solution(record):
    ID_table = {}
    queue = deque()
    answer = []
    
    for i in record:
        record_lst = i.split()
        command = record_lst[0]
        ID = record_lst[1]
        if command == 'Enter':
            ID_table[ID] = record_lst[2]
            queue.append([ID, command])
        elif command == 'Leave':
            queue.append([ID, command])
        elif command == 'Change':
            print(ID, record_lst[2])
            ID_table[ID] = record_lst[2]
    
    print(ID_table)

    for i in queue:
        name = ID_table.get(i[0])
        command = i[1]
        if command == 'Enter':
            explain = name + '님이 들어왔습니다.'
            answer.append(explain)
        elif command == 'Leave':
            explain = name + '님이 나갔습니다.'
            answer.append(explain)
    
    return answer

print(solution(["Enter uid1234 Muzi", "Enter uid4567 Prodo", "Leave uid1234", "Enter uid1234 Muzi", "Change uid4567 Ryan"]))