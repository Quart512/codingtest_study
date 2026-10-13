---
tags: [교과서, 파이썬문법]
---

# 반복문의 else

## 무엇인가

`while` 과 `for` 뒤에도 `else` 를 붙일 수 있다. **반복이 `break` 없이 끝났을 때만** 실행된다.

"끝까지 찾아봤는데 없었다" 를 적는 자리다.

```python
while 후보:
    if 찾았다:
        ...
        break          # 여기로 나가면 else 는 건너뛴다
    후보.pop()
else:
    ...                # break 를 한 번도 안 하고 끝났을 때만
```

`for` 도 똑같다.

```python
for x in lst:
    if x == target:
        print("있다")
        break
else:
    print("없다")
```

## 읽는 법

`if` 의 `else` 처럼 "아니면" 으로 읽으면 헷갈린다. **"break 안 했으면"** 으로 읽는다.

## 언제 실행되나

| 반복이 끝난 방식 | `else` |
|---|---|
| 조건이 거짓이 되었다 / 끝까지 다 돌았다 | 실행 |
| 처음부터 돌 것이 없었다 (빈 리스트) | 실행 |
| `break` 로 나갔다 | 건너뜀 |
| `return` 으로 함수를 나갔다 | 건너뜀 |

`continue` 는 영향이 없다. 반복을 끝내는 게 아니라 다음 바퀴로 넘어갈 뿐이다.

## 없으면 어떻게 쓰나

깃발 변수로 같은 일을 할 수 있다. `else` 는 이 변수를 없애 준다.

```python
found = False
for x in lst:
    if x == target:
        found = True
        break
if not found:
    print("없다")
```

## 주의할 점

- **들여쓰기 깊이가 뜻을 바꾼다.** `if` 와 같은 깊이면 `if` 의 짝, `while` 과 같은 깊이면 `while` 의 짝이다. 한 단계 잘못 들여도 에러 없이 다른 뜻이 된다

  ```python
  while 후보:
      if 찾았다:
          break
      else:              # if 의 짝: 이번 바퀴에 못 찾았을 때마다
          후보.pop()
  else:                  # while 의 짝: 끝까지 못 찾았을 때 한 번
      answer.append(-1)
  ```

- `break` 가 없는 반복문에 붙이면 **언제나 실행된다.** 그럴 거면 반복문 아래에 그냥 쓰면 된다
- 이중 반복에서 `break` 는 **안쪽 반복만** 끝낸다. `else` 도 자기가 붙은 반복문의 `break` 만 본다 → [[공원산책]]

## 연결된 노트

- 교과서: [[시간복잡도]]
- 관련 문제: [[뒤에있는큰수찾기]] · [[공원산책]]
