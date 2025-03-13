# itertools

## itertools 기본 사용법

```python
import itertools

# 반복 가능한 객체에서 순열 생성
perms = list(itertools.permutations([1, 2, 3]))
print(perms)  # [(1, 2, 3), (1, 3, 2), (2, 1, 3), (2, 3, 1), (3, 1, 2), (3, 2, 1)]

# 반복 가능한 객체에서 조합 생성
combs = list(itertools.combinations([1, 2, 3], 2))
print(combs)  # [(1, 2), (1, 3), (2, 3)]

# 중복을 허용한 조합 생성
combs_with_replacement = list(itertools.combinations_with_replacement([1, 2, 3], 2))
print(combs_with_replacement)  # [(1, 1), (1, 2), (1, 3), (2, 2), (2, 3), (3, 3)]

# 곱집합 생성
products = list(itertools.product([1, 2], ['a', 'b']))
print(products)  # [(1, 'a'), (1, 'b'), (2, 'a'), (2, 'b')]
```

## itertools 고급 사용법

```python
# 무한히 반복되는 카운터 생성
counter = itertools.count(10, 2)
print(next(counter))  # 10
print(next(counter))  # 12

# 특정 값만 필터링
filtered = list(itertools.filterfalse(lambda x: x % 2 == 0, range(10)))
print(filtered)  # [1, 3, 5, 7, 9]

# 누적 합 계산
accumulated = list(itertools.accumulate([1, 2, 3, 4]))
print(accumulated)  # [1, 3, 6, 10]

# 여러 반복 가능한 객체를 체인으로 연결
chained = list(itertools.chain([1, 2], [3, 4]))
print(chained)  # [1, 2, 3, 4]

# 그룹화
data = [('a', 1), ('a', 2), ('b', 3)]
for key, group in itertools.groupby(data, key=lambda x: x[0]):
    print(key, list(group))
# a [('a', 1), ('a', 2)]
# b [('b', 3)]
```

## itertools 메소드 총 정리

### 1. **`count()`**
   - 시작 값부터 일정한 간격으로 무한히 증가하는 값을 생성합니다.
   ```python
   from itertools import count
   for i in count(5, 2):
       if i > 10:
           break
       print(i)  # 결과: 5, 7, 9
   ```

### 2. **`cycle()`**
   - 주어진 iterable을 무한히 반복합니다.
   ```python
   from itertools import cycle
   count = 0
   for item in cycle(['A', 'B', 'C']):
       print(item)
       count += 1
       if count == 5:
           break
   ```

### 3. **`repeat()`**
   - 지정한 값을 반복적으로 생성합니다.
   ```python
   from itertools import repeat
   for item in repeat(10, 3):
       print(item)  # 결과: 10, 10, 10
   ```

### 4. **`chain()`**
   - 여러 iterable을 연결하여 하나로 만듭니다.
   ```python
   from itertools import chain
   print(list(chain([1, 2], [3, 4])))  # 결과: [1, 2, 3, 4]
   ```

### 5. **`compress()`**
   - 데이터와 선택기를 사용하여 참인 값만 선택합니다.
   ```python
   from itertools import compress
   data = ['a', 'b', 'c']
   selectors = [1, 0, 1]
   print(list(compress(data, selectors)))  # 결과: ['a', 'c']
   ```

### 6. **`dropwhile()`**
   - 조건이 참인 동안은 건너뛰고, 그 이후부터 반환합니다.
   ```python
   from itertools import dropwhile
   print(list(dropwhile(lambda x: x < 3, [1, 2, 3, 4])))  # 결과: [3, 4]
   ```

### 7. **`takewhile()`**
   - 조건이 참인 동안만 반환합니다.
   ```python
   from itertools import takewhile
   print(list(takewhile(lambda x: x < 3, [1, 2, 3, 4])))  # 결과: [1, 2]
   ```

### 8. **`filterfalse()`**
   - 조건이 거짓인 값만 반환합니다.
   ```python
   from itertools import filterfalse
   print(list(filterfalse(lambda x: x % 2, range(5))))  # 결과: [0, 2, 4]
   ```

### 9. **`accumulate()`**
   - 누적 값을 반환합니다.
   ```python
   from itertools import accumulate
   print(list(accumulate([1, 2, 3, 4])))  # 결과: [1, 3, 6, 10]
   ```

### 10. **`product()`**
   - 데카르트 곱을 반환합니다.
   ```python
   from itertools import product
   print(list(product([1, 2], ['a', 'b'])))  # 결과: [(1, 'a'), (1, 'b'), (2, 'a'), (2, 'b')]
   ```

### 11. **`permutations()`**
   - 주어진 길이의 순열을 반환합니다.
   ```python
   from itertools import permutations
   print(list(permutations([1, 2, 3], 2)))  # 결과: [(1, 2), (1, 3), (2, 1), (2, 3), (3, 1), (3, 2)]
   ```

### 12. **`combinations()`**
   - 주어진 길이의 조합을 반환합니다.
   ```python
   from itertools import combinations
   print(list(combinations([1, 2, 3], 2)))  # 결과: [(1, 2), (1, 3), (2, 3)]
   ```

### 13. **`combinations_with_replacement()`**
   - 중복을 허용한 조합을 반환합니다.
   ```python
   from itertools import combinations_with_replacement
   print(list(combinations_with_replacement([1, 2, 3], 2)))  # 결과: [(1, 1), (1, 2), (1, 3), (2, 2), (2, 3), (3, 3)]
   ```

### 14. **`groupby()`**
   - 연속된 동일한 값을 그룹으로 묶습니다.
   ```python
   from itertools import groupby
   data = [('a', 1), ('a', 2), ('b', 3)]
   for key, group in groupby(data, lambda x: x[0]):
       print(key, list(group))
   ```

