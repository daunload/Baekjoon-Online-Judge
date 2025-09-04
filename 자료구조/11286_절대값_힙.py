import sys
import heapq

input = sys.stdin.readline

N = int(input())

heap = []
result = []

for _ in range(N):
    x = int(input())
    
    if x == 0:
        if not heap:
            result.append(0)
        else: result.append(heapq.heappop(heap)[1])
    else:
        heapq.heappush(heap, (abs(x), x))

for v in result:
    print(v)