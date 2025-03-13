# 세트 (Set)

## 세트 기본 사용법

```python
# 세트 생성
my_set = {1, 2, 3, 4, 5}

# 값 추가
my_set.add(6)  # {1, 2, 3, 4, 5, 6}

# 값 삭제
my_set.remove(3)  # {1, 2, 4, 5, 6}

# 값 존재 여부 확인
print(2 in my_set)  # True
print(3 in my_set)  # False

# 세트 출력
print(my_set)
```

## 세트 고급 사용법

```python
# 두 세트의 합집합
set1 = {1, 2, 3}
set2 = {3, 4, 5}
print(set1.union(set2))  # {1, 2, 3, 4, 5}

# 두 세트의 교집합
print(set1.intersection(set2))  # {3}

# 두 세트의 차집합
print(set1.difference(set2))  # {1, 2}

# 두 세트의 대칭 차집합
print(set1.symmetric_difference(set2))  # {1, 2, 4, 5}

# 세트 컴프리헨션
squared = {x**2 for x in range(5)}  # {0, 1, 4, 9, 16}

# 세트 복사
new_set = set1.copy()

# 조건에 따른 필터링
filtered_set = {x for x in set1 if x % 2 == 0}  # {2}
```

## 세트 메소드 총 정리

### 1. **`add()`**
   - 세트에 요소를 추가합니다.
   ```python
   s = {1, 2}
   s.add(3)  # 결과: {1, 2, 3}
   ```

### 2. **`update()`**
   - 여러 요소를 추가합니다.
   ```python
   s = {1, 2}
   s.update([3, 4])  # 결과: {1, 2, 3, 4}
   ```

### 3. **`remove()`**
   - 특정 요소를 제거합니다. 요소가 없으면 오류 발생.
   ```python
   s = {1, 2, 3}
   s.remove(2)  # 결과: {1, 3}
   ```

### 4. **`discard()`**
   - 특정 요소를 제거합니다. 요소가 없어도 오류가 발생하지 않습니다.
   ```python
   s = {1, 2, 3}
   s.discard(4)  # 결과: {1, 2, 3}
   ```

### 5. **`pop()`**
   - 임의의 요소를 제거하고 반환합니다.
   ```python
   s = {1, 2, 3}
   print(s.pop())  # 결과: 1 (임의의 값)
   ```

### 6. **`clear()`**
   - 모든 요소를 제거합니다.
   ```python
   s = {1, 2, 3}
   s.clear()  # 결과: set()
   ```

### 7. **`union()`**
   - 두 세트의 합집합을 반환합니다.
   ```python
   s1 = {1, 2}
   s2 = {2, 3}
   print(s1.union(s2))  # 결과: {1, 2, 3}
   ```

### 8. **`intersection()`**
   - 두 세트의 교집합을 반환합니다.
   ```python
   s1 = {1, 2}
   s2 = {2, 3}
   print(s1.intersection(s2))  # 결과: {2}
   ```

### 9. **`difference()`**
   - 차집합을 반환합니다.
   ```python
   s1 = {1, 2}
   s2 = {2, 3}
   print(s1.difference(s2))  # 결과: {1}
   ```

### 10. **`symmetric_difference()`**
   - 대칭 차집합을 반환합니다.
   ```python
   s1 = {1, 2}
   s2 = {2, 3}
   print(s1.symmetric_difference(s2))  # 결과: {1, 3}
   ```

### 11. **`issubset()`**
   - 부분 집합인지 확인합니다.
   ```python
   s1 = {1, 2}
   s2 = {1, 2, 3}
   print(s1.issubset(s2))  # 결과: True
   ```

### 12. **`issuperset()`**
   - 상위 집합인지 확인합니다.
   ```python
   s1 = {1, 2, 3}
   s2 = {1, 2}
   print(s1.issuperset(s2))  # 결과: True
   ```

### 13. **`copy()`**
   - 세트의 얕은 복사본을 반환합니다.
   ```python
   s = {1, 2, 3}
   new_s = s.copy()
   ```

### 14. **`len()`**
   - 세트의 요소 개수를 반환합니다.
   ```python
   s = {1, 2, 3}
   print(len(s))  # 결과: 3
   ```

### 15. **`in` 연산자**
   - 세트에 특정 값이 존재하는지 확인합니다.
   ```python
   s = {1, 2, 3}
   print(2 in s)  # 결과: True
   print(4 in s)  # 결과: False
   ```

