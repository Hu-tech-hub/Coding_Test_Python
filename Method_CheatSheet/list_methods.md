# 리스트

## 리스트 기본 사용법

```python
# 리스트 생성
my_list = [1, 2, 3, 4, 5]

# 값 조회
print(my_list[0])  # 1

# 값 추가
my_list.append(6)  # [1, 2, 3, 4, 5, 6]

# 값 수정
my_list[0] = 10    # [10, 2, 3, 4, 5, 6]

# 값 삭제
del my_list[1]     # [10, 3, 4, 5, 6]

# 리스트 출력
print(my_list)
```

## 리스트 고급 사용법

```python
# 리스트 컴프리헨션으로 새로운 리스트 생성
squares = [x**2 for x in range(5)]  # [0, 1, 4, 9, 16]

# 조건을 추가한 리스트 컴프리헨션
even_squares = [x**2 for x in range(10) if x % 2 == 0]  # [0, 4, 16, 36, 64]

# 중첩 리스트에서 값 추출하기
matrix = [[1, 2], [3, 4], [5, 6]]
flattened = [num for row in matrix for num in row]  # [1, 2, 3, 4, 5, 6]

# enumerate()를 사용한 인덱스와 값 처리
for idx, value in enumerate(my_list):
    print(idx, value)

# zip()으로 두 리스트 병합
list1 = [1, 2, 3]
list2 = ['a', 'b', 'c']
merged = list(zip(list1, list2))  # [(1, 'a'), (2, 'b'), (3, 'c')]

# 리스트를 문자열로 변환
chars = ['a', 'b', 'c']
string = ''.join(chars)  # 'abc'
```

## 리스트 메소드 총 정리

### 1. **`append()`**
   - 리스트의 끝에 요소를 추가합니다.
   ```python
   lst = [1, 2]
   lst.append(3)   # 결과: [1, 2, 3]
   ```

### 2. **`extend()`**
   - 리스트에 다른 리스트나 반복 가능한 객체를 추가합니다.
   ```python
   lst = [1, 2]
   lst.extend([3, 4])   # 결과: [1, 2, 3, 4]
   ```

### 3. **`insert()`**
   - 지정한 인덱스에 값을 삽입합니다.
   ```python
   lst = [1, 2, 3]
   lst.insert(1, 10)    # 결과: [1, 10, 2, 3]
   ```

### 4. **`remove()`**
   - 지정한 값을 찾아서 삭제합니다.
   ```python
   lst = [1, 2, 3]
   lst.remove(2)        # 결과: [1, 3]
   ```

### 5. **`pop()`**
   - 지정한 인덱스의 값을 반환하고 삭제합니다. 인덱스를 지정하지 않으면 마지막 요소를 삭제합니다.
   ```python
   lst = [1, 2, 3]
   print(lst.pop())     # 결과: 3
   print(lst)           # 결과: [1, 2]
   ```

### 6. **`clear()`**
   - 모든 요소를 제거합니다.
   ```python
   lst = [1, 2, 3]
   lst.clear()          # 결과: []
   ```

### 7. **`index()`**
   - 지정한 값의 첫 번째 인덱스를 반환합니다.
   ```python
   lst = [1, 2, 3]
   print(lst.index(2))  # 결과: 1
   ```

### 8. **`count()`**
   - 리스트에서 지정한 값의 개수를 반환합니다.
   ```python
   lst = [1, 2, 2, 3]
   print(lst.count(2))  # 결과: 2
   ```

### 9. **`sort()`**
   - 리스트를 오름차순으로 정렬합니다.
   ```python
   lst = [3, 1, 2]
   lst.sort()           # 결과: [1, 2, 3]
   ```

### 10. **`reverse()`**
   - 리스트의 순서를 뒤집습니다.
   ```python
   lst = [1, 2, 3]
   lst.reverse()        # 결과: [3, 2, 1]
   ```

### 11. **`copy()`**
   - 리스트의 얕은 복사본을 반환합니다.
   ```python
   lst = [1, 2, 3]
   new_lst = lst.copy()
   ```

### 12. **`len()`**
   - 리스트의 요소 개수를 반환합니다.
   ```python
   lst = [1, 2, 3]
   print(len(lst))      # 결과: 3
   ```

### 13. **`in` 연산자**
   - 리스트에 특정 값이 존재하는지 확인합니다.
   ```python
   lst = [1, 2, 3]
   print(2 in lst)      # 결과: True
   print(5 in lst)      # 결과: False
   ```

