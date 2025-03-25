#문제 07 방문 길이

## 게임 케릭터를 4가지 명령어를 통해 움직이려 합니다. 명령어는 다음과 같습니다.

## U : 위쪽으로 한 칸 이동
## D : 아래쪽으로 한 칸 이동
## L : 왼쪽으로 한 칸 이동
## R : 오른쪽으로 한 칸 이동

## 캐릭터는 좌표평면의 (0, 0)에서 시작합니다. 좌표 평면의 경계는 왼쪽 위(-5, 5)에서 오른쪽 아래(5, -5)까지입니다.

## 이때 우리는 게임 케릭터가 지나간 길 중 캐릭터가 처음 걸어본 길의 길이를 구하려고 합니다. 예를 들어 위의 예시에서 게임 케릭터가


dirs = input()

position = (0, 0)  # 시작 위치
visited = set()  # 방문한 길을 저장할 집합

for dir in dirs:
    # dir = dirs[i]
    if dir == 'U':
        x, y = 0, 1
        visited_position = position 
        position = (position[0], position[1] + 1)
        if position[1] > 5:
            continue
        
        visited.add((visited_position, position))
        visited.add((position, visited_position))
    elif dir == 'D':
        x, y = 0, -1
        visited_position = position
        position = (position[0], position[1] - 1)
        if position[1] < -5:
            continue
        
        visited.add((visited_position, position))
        visited.add((position, visited_position))
    elif dir == 'L':
        x, y = -1, 0
        visited_position = position
        position = (position[0] - 1, position[1])
        if position[0] < -5:
            continue
        
        visited.add((visited_position, position))
        visited.add((position, visited_position))
    elif dir == 'R':
        x, y = 1, 0
        visited_position = position
        position = (position[0] + 1, position[1])
        if position[0] > 5:
            continue
        
        visited.add((visited_position, position))
        visited.add((position, visited_position))

print(len(visited) // 2)  # 길이의 절반을 반환 (양방향으로 저장했으므로)