import sys
import heapq

input = sys.stdin.readline

N = int(input())

result = []
heap = []
for _ in range(N):
    x = int(input())
    if x == 0:
        if heap:
            result.append(heapq.heappop(heap))
        else:
            result.append(0)
    else:
        heapq.heappush(heap, x)

for value in result:
    print(value)