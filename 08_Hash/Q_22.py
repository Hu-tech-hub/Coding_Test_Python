def solution(record):
  answer = []
  dic = {}
  
  for i in record:
    if i.split()[0] != "Leave":
      dic[i.split()[1]] = i.split()[2]
      
  for i in record:
    if i.split()[0] == "Enter":
      answer.append(dic[i.split()[1]] + "님이 들어왔습니다.")
    elif i.split()[0] == "Leave":
      answer.append(dic[i.split()[1]] + "님이 나갔습니다.")
  
  return answer

print(solution(["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]))