#문제 14 표 편집

# 명령어에 따라 편집을 수행하는 프로그램을 작성하시오.
# 명령어는 다음과 같다.
# 1. U X : 커서를 위로 X칸 이동한다. (커서가 맨 위에 있으면 무시)
# 2. D X : 커서를 아래로 X칸 이동한다. (커서가 맨 아래에 있으면 무시)
# 3. C : 현재 커서에 있는 행을 삭제한다. 삭제된 행은 복구할 수 있도록 보관한다.
# 4. Z : 가장 최근에 삭제된 행을 복구한다. 복구할 수 있는 행이 없다면 무시한다.

# 문제 분석
# 1. 단순히 배열을 만들고 cmd에 있는 명령어 순서대로 수행하면서 최종 결과 확인. <- 시간 초과.
# 2. 인덱스만으로 연산한다. <- up, down은 인덱스만 이동하고, C는 삭제된 행을 스택에 저장한다. Z는 스택에서 pop하여 복구한다.

# 여기서 잠깐, 배열을 삭제하지 않고도 인덱스를 활용하여 삭제가 된 것 처럼 보이게 할 수 있다.
# 1. 삭제된 행을 스택에 저장한다.
# 2. up, down 인덱스를 
# 3. 삭제된 행을 표시할 배열의 인덱스에 해당하는 행을 삭제된 것으로 표시한다.

n = 5 # 그러니까 0 ~ 4 까지 5개라는 뜻 (n = len(표))
k = 4 # 커서의 위치. 인덱스 번호가 2라는 뜻
cmd = ["U2", "C", "D2", "C", "Z"] # 명령어를 저장할 리스트

up = [i -1 for i in range(n)] # 위로 이동할 수 있는 인덱스 번호를 저장한다.
down = [i + 1 for i in range(n)] # 아래로 이동할 수 있는 인덱스 번호를 저장한다.
delete = [] # 삭제된 행을 저장할 스택

for cmd_i in cmd:
  if cmd_i[0] == 'U':
    x = int(cmd_i[1])
    for _ in range(x):
      k = up[k]
  elif cmd_i[0] == 'D':
    x = int(cmd_i[1])
    for _ in range(x):
      k = down[k]
  elif cmd_i[0] == 'C':
    delete.append(k)
    # 삭제된 행을 스택에 저장한다.
    
