# 1. 
# 2. 
# 3. 
# 4. 
# 5. 
# 6. 
# 7. 
# 8. 
# 9. 
# 10. 



# 문제 1.

lst = [10, 20, 30, 40, 50]

lst.insert(2, 25) # 시간복잡도 : O(n)

lst.pop(2) # 시간 복잡도 O(n)

print(lst)

# 문제 2.

lst = [10, 20, 30, 40, 50]

lst = [ lst[i] for i in range(1, len(lst)) if i % 2 == 0]

# lst[i] = O(1) , 반복문 -> O(n)
print(lst)

# 문제 3.

lst = [1, 2, 3, 4, 5]

lst.reverse() # O(n)

lst = [i * 2 for i in lst] # O(n)

print(lst)

# 문제 4.

lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

lst = [ value for value in lst if value % 2 == 0 ] #O(n)

lst.extend([11, 12, 13]) # O(3)

print(lst)

# 문제 5

lst = [3, 1, 4, 1, 5, 9, 2, 6, 5]

lst.sort() #O(n)

print(lst)

