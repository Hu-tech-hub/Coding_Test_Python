# 🌱 New Concepts (새로 학습한 개념)

---

### 1. Python의 `Counter` 클래스
- **개념**: 리스트나 문자열 내에서 요소의 빈도를 세는 데 유용
- **예시**
```python
from collections import Counter

arr = ['a', 'b', 'a', 'c', 'b']
counter = Counter(arr)
print(counter)  # Counter({'a': 2, 'b': 2, 'c': 1})
```