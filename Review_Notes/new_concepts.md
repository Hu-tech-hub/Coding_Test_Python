# 🌱 New Concepts (새로 학습한 개념)

---

## 1. Python의 `Counter` 클래스
- **개념**: 리스트나 문자열 내에서 요소의 빈도를 세는 데 유용
- **예시**
```python
from collections import Counter

arr = ['a', 'b', 'a', 'c', 'b']
counter = Counter(arr)
print(counter)  # Counter({'a': 2, 'b': 2, 'c': 1})
```

---

## 2. Python의 `*`와 `**` 연산자
- **개념**: 패킹(Packing)과 언패킹(Unpacking)에 사용됨
- **예시**
```python
# 패킹: 여러 값을 하나로 묶음
def pack(*args, **kwargs):
    print(args)    # 튜플 형태로 패킹
    print(kwargs)  # 딕셔너리 형태로 패킹

pack(1, 2, 3, a=4, b=5)
# 결과: (1, 2, 3), {'a': 4, 'b': 5}

# 언패킹: 묶인 값을 풀어서 전달
def add(a, b, c):
    return a + b + c
nums = [1, 2, 3]
print(add(*nums))  # 6

# 변수 대입에서 패킹
a, *b, c = [1, 2, 3, 4]
print(b)  # [2, 3]

# 리스트 병합에서 언패킹
list1 = [1, 2]
list2 = [3, 4]
merged = [*list1, *list2]
print(merged)  # [1, 2, 3, 4]
```