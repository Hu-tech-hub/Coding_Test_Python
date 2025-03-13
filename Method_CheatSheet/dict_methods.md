# 딕셔너리

## 딕셔너리 기본 사용법

```python
# 딕셔너리 생성
my_dict = {'name': 'Alice', 'age': 25, 'city': 'New York'}

# 값 조회
print(my_dict['name'])  # Alice

# 값 추가 및 수정
my_dict['age'] = 26     # 값 수정
my_dict['job'] = 'Engineer'  # 값 추가

# 값 삭제
del my_dict['city']     # 특정 키 삭제

# 키 존재 여부 확인
print('name' in my_dict)  # True

# 딕셔너리 출력
print(my_dict)
# {'name': 'Alice', 'age': 26, 'job': 'Engineer'}
```

## 딕셔너리 메소드 총 정리

### 1. **`clear()`**
   - 딕셔너리의 모든 항목을 제거합니다.
   ```python
   d = {'a': 1, 'b': 2}
   d.clear()  # 결과: {}
   ```

### 2. **`copy()`**
   - 딕셔너리의 얕은 복사본을 반환합니다.
   ```python
   d = {'a': 1, 'b': 2}
   d_copy = d.copy()
   ```

### 3. **`get()`**
   - 주어진 키의 값을 반환하고, 키가 없으면 기본값을 반환합니다.
   ```python
   d = {'a': 1, 'b': 2}
   print(d.get('a'))       # 결과: 1
   print(d.get('c', 0))    # 결과: 0
   ```

### 4. **`items()`**
   - 딕셔너리의 (키, 값) 쌍을 반환합니다.
   ```python
   d = {'a': 1, 'b': 2}
   print(list(d.items()))  # 결과: [('a', 1), ('b', 2)]
   ```

### 5. **`keys()`**
   - 딕셔너리의 모든 키를 반환합니다.
   ```python
   d = {'a': 1, 'b': 2}
   print(list(d.keys()))   # 결과: ['a', 'b']
   ```

### 6. **`values()`**
   - 딕셔너리의 모든 값을 반환합니다.
   ```python
   d = {'a': 1, 'b': 2}
   print(list(d.values())) # 결과: [1, 2]
   ```

### 7. **`pop()`**
   - 주어진 키의 값을 반환하고, 그 항목을 삭제합니다.
   ```python
   d = {'a': 1, 'b': 2}
   print(d.pop('a'))       # 결과: 1
   print(d)                # 결과: {'b': 2}
   ```

### 8. **`popitem()`**
   - 마지막 (키, 값) 쌍을 반환하고 삭제합니다.
   ```python
   d = {'a': 1, 'b': 2}
   print(d.popitem())      # 결과: ('b', 2)
   ```

### 9. **`setdefault()`**
   - 주어진 키가 없으면 키를 추가하고 기본값을 설정합니다.
   ```python
   d = {'a': 1}
   d.setdefault('b', 2)
   print(d)                # 결과: {'a': 1, 'b': 2}
   ```

### 10. **`update()`**
   - 다른 딕셔너리의 항목을 추가하거나 덮어씁니다.
   ```python
   d = {'a': 1}
   d.update({'b': 2, 'c': 3})
   print(d)                # 결과: {'a': 1, 'b': 2, 'c': 3}
   ```

### 11. **`fromkeys()`**
   - 주어진 키 목록으로 새 딕셔너리를 생성하고 값을 설정합니다.
   ```python
   keys = ['a', 'b', 'c']
   d = dict.fromkeys(keys, 0)
   print(d)                # 결과: {'a': 0, 'b': 0, 'c': 0}
   ```

### 12. **`len()`**
   - 딕셔너리의 항목 개수를 반환합니다.
   ```python
   d = {'a': 1, 'b': 2}
   print(len(d))           # 결과: 2
   ```

### 13. **`in` 연산자**
   - 딕셔너리에 특정 키가 존재하는지 확인합니다.
   ```python
   d = {'a': 1, 'b': 2}
   print('a' in d)         # 결과: True
   print('c' in d)         # 결과: False
   ```

