---
tags: [에러, 파이썬, 런타임에러]
에러타입: IndexError
---

# IndexError: list index out of range

```
IndexError: list index out of range
```

**없는 위치의 원소를 꺼내려 했다.** 길이 3인 리스트에서 `lst[3]` 또는 빈 리스트에서 `lst[0]`.

## 언제 발생하나

### 1. `and` / `or` 의 순서를 잘못 둠 (가장 흔함)

```python
if lst[0] == x and lst:      # 터짐: lst[0] 을 먼저 평가
if lst and lst[0] == x:      # 안전: lst 가 거짓이면 오른쪽은 평가조차 안 함
```

파이썬은 **단락 평가(short-circuit)** 를 한다. `A and B` 는 A가 거짓이면 B를 아예 계산하지 않고, `A or B` 는 A가 참이면 B를 계산하지 않는다.
그래서 **범위 검사는 반드시 왼쪽**, 인덱스 접근은 오른쪽.

실제 사례: [[카드뭉치]]

### 2. 반복 도중 리스트를 줄임

```python
for i in range(len(lst)):
    if 조건:
        lst.pop(i)      # len 은 줄어드는데 range 는 처음 길이 그대로
```
→ 새 리스트를 만들거나 (`[x for x in lst if not 조건]`), 뒤에서부터 순회 (`reversed(range(len(lst)))`).

### 3. `<=` 와 `<` 혼동

```python
for i in range(len(lst) + 1):   # 마지막 바퀴에서 lst[len(lst)] 접근
while i <= len(lst):
```
파이썬 인덱스는 `0` 부터 `len-1` 까지다.

### 4. 입력 파싱 결과가 예상과 다름

```python
a, b = input().split()          # 값이 1개면 ValueError
parts = line.split(",")
parts[1]                        # 구분자가 없으면 IndexError
```

### 5. 이중 리스트에서 행/열 헷갈림

```python
board[y][x]   # 세로 먼저, 가로 나중
board[x][y]   # 정사각형이 아니면 여기서 터짐
```

## 디버깅 순서

1. 트레이스백의 **맨 아래 줄 번호**를 본다. 그 줄의 `[]` 가 범인이다.
2. 그 줄 직전에 `print(len(lst), i)` 를 찍어 실제 값을 확인한다.
3. 인덱스가 어디서 커졌는지 / 리스트가 어디서 줄었는지 거슬러 올라간다.

## 예방 습관

- 인덱스 접근 앞에는 **항상** 존재 검사를 왼쪽에 둔다: `if lst and lst[0] ...`
- 빈 리스트, 원소 1개, 한쪽만 소진되는 입력을 테스트 케이스에 넣는다
- 인덱스 대신 순회로 바꿀 수 있는지 본다: `for x in lst` 는 IndexError 가 원천적으로 안 난다
- 꼭 인덱스로 접근해야 하면 [[투 포인터]] 처럼 **경계 검사를 조건에 포함**시킨다

## 연결된 노트

- 발생한 문제: [[카드뭉치]]
- 개념: [[앞에서 빼야 할 때]] · [[두 뭉치 순서대로 꺼내기]]
