# 문자열 (String)

## 문자열 기본 사용법

```python
# 문자열 생성
my_str = "Hello, World!"

# 문자열 인덱싱
print(my_str[0])  # H

# 문자열 슬라이싱
print(my_str[0:5])  # Hello

# 문자열 길이
print(len(my_str))  # 13

# 문자열 덧셈 (합치기)
new_str = my_str + " How are you?"
print(new_str)  # Hello, World! How are you?

# 문자열 반복
print(my_str * 2)  # Hello, World!Hello, World!

# 문자열 포함 여부 확인
print("Hello" in my_str)  # True
```

## 문자열 고급 사용법

```python
# 문자열 포맷팅
name = "Alice"
age = 30
print(f"My name is {name} and I am {age} years old.")

# 문자열 분할
sentence = "Python is fun"
print(sentence.split())  # ['Python', 'is', 'fun']

# 문자열 대소문자 변환
print(my_str.lower())  # hello, world!
print(my_str.upper())  # HELLO, WORLD!

# 문자열 공백 제거
text = "   hello   "
print(text.strip())  # hello

# 문자열 교체
print(my_str.replace("World", "Python"))  # Hello, Python!

# 문자열 정렬
print(my_str.center(20, '-'))  # ---Hello, World!---

# 문자열 반복과 합치기
chars = ['a', 'b', 'c']
print("-".join(chars))  # a-b-c

# 문자열 역순 출력
print(my_str[::-1])  # !dlroW ,olleH
```

## 문자열 메소드 총 정리

### 1. **`lower()`**
   - 문자열을 소문자로 변환합니다.
   ```python
   s = "HELLO"
   print(s.lower())  # 결과: hello
   ```

### 2. **`upper()`**
   - 문자열을 대문자로 변환합니다.
   ```python
   s = "hello"
   print(s.upper())  # 결과: HELLO
   ```

### 3. **`strip()`**
   - 문자열의 양쪽 공백을 제거합니다.
   ```python
   s = "   hello   "
   print(s.strip())  # 결과: hello
   ```

### 4. **`replace()`**
   - 문자열의 특정 부분을 교체합니다.
   ```python
   s = "Hello, World!"
   print(s.replace("World", "Python"))  # 결과: Hello, Python!
   ```

### 5. **`split()`**
   - 문자열을 지정한 구분자로 나눕니다.
   ```python
   s = "a,b,c"
   print(s.split(","))  # 결과: ['a', 'b', 'c']
   ```

### 6. **`join()`**
   - 반복 가능한 객체의 요소들을 구분자로 연결합니다.
   ```python
   chars = ['a', 'b', 'c']
   print("-".join(chars))  # 결과: a-b-c
   ```

### 7. **`find()`**
   - 문자열에서 지정한 값의 첫 번째 인덱스를 반환합니다. 값이 없으면 -1을 반환합니다.
   ```python
   s = "hello"
   print(s.find("e"))  # 결과: 1
   ```

### 8. **`count()`**
   - 문자열에서 지정한 값의 개수를 반환합니다.
   ```python
   s = "hello hello"
   print(s.count("hello"))  # 결과: 2
   ```

### 9. **`startswith()`**
   - 문자열이 지정한 접두사로 시작하는지 확인합니다.
   ```python
   s = "hello"
   print(s.startswith("he"))  # 결과: True
   ```

### 10. **`endswith()`**
   - 문자열이 지정한 접미사로 끝나는지 확인합니다.
   ```python
   s = "hello"
   print(s.endswith("lo"))  # 결과: True
   ```

### 11. **`isalpha()`**
   - 문자열이 알파벳 문자로만 이루어져 있는지 확인합니다.
   ```python
   s = "hello"
   print(s.isalpha())  # 결과: True
   ```

### 12. **`isdigit()`**
   - 문자열이 숫자로만 이루어져 있는지 확인합니다.
   ```python
   s = "123"
   print(s.isdigit())  # 결과: True
   ```

### 13. **`isalnum()`**
   - 문자열이 알파벳 문자와 숫자로만 이루어져 있는지 확인합니다.
   ```python
   s = "abc123"
   print(s.isalnum())  # 결과: True
   ```

### 14. **`len()`**
   - 문자열의 길이를 반환합니다.
   ```python
   s = "hello"
   print(len(s))  # 결과: 5
   ```

### 15. **`in` 연산자**
   - 문자열에 특정 값이 존재하는지 확인합니다.
   ```python
   s = "hello"
   print("he" in s)  # 결과: True
   print("hi" in s)  # 결과: False
   ```

