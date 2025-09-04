import sys
import heapq

input = sys.stdin.readline

N = int(input())

heap = []
stack = []
for _ in range(N):
    x = int(input())

    if x == 0:
        if not heap:
            stack.append(0)
        else: stack.append(heapq.heappop(heap) * -1)
    else:
        heapq.heappush(heap,  x * -1)

for _ in stack:
    print(_)