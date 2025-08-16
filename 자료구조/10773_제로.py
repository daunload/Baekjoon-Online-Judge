import sys
input = sys.stdin.readline

K = int(input())

arr = []

for _ in range(K):
    n = int(input())
    
    if n == 0:
        arr.pop()
    else:
        arr.append(n)
    
result = 0
for n in arr:
    result += n
print(result)