def polynomial_hash(string):
  hash = 0
  p = 31
  m = 1000000007
  for i in range(len(string)):
    hash = (hash * p + ord(string[i])) % m
  return hash

def solution(string_list, query_list):
  lst = []
  string_hash_list = [polynomial_hash(i) for i in string_list]
  for i in query_list:
    hash = polynomial_hash(i)
    if hash in string_hash_list:
      lst.append(True)
    else:
      lst.append(False)
  return lst

string_list = ["apple", "banana", "cherry"]
query_list = ["apple", "banana", "cherry", "date"]

print(solution(string_list, query_list))
