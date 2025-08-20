import sys
from collections import deque

input = sys.stdin.readline

N = int(input())

_deque = deque([])
result = []

for i in range(N):
    text = input().split()
    command = text[0]

    if command == 'push_front':
        _deque.appendleft(text[1])
    elif command == 'push_back':
        _deque.append(text[1])
    elif command == 'pop_front':
        result.append(-1 if len(_deque) == 0 else _deque.popleft())
    elif command == 'pop_back':
        result.append(-1 if len(_deque) == 0 else _deque.pop())
    elif command == 'size':
        result.append(len(_deque))
    elif command == 'empty':
        result.append('1' if len(_deque) == 0 else '0')
    elif command == 'front':
        result.append(-1 if len(_deque) == 0 else _deque[0])
    elif command == 'back':
        result.append(-1 if len(_deque) == 0 else _deque[-1])

for i in result:
    print(i)