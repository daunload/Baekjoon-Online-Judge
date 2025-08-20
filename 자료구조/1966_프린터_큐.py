import sys
from collections import deque

input = sys.stdin.readline

N = int(input())

queue = deque([])

for _ in range(N):
    amount, position = map(int, input().split())

    documents = list(map(int, input().split()))

    queue = deque([(index, docs) for index, docs in enumerate(documents)])
    count = 0

    while documents:
        cur = queue.popleft()
        if any(cur[1] < q[1] for q in queue):
            queue.append(cur)
        else:
            count += 1
            if cur[0] == position:
                print(count)
                break