import sys

input = sys.stdin.readline

N = int(input()) # 상근이가 가지고 있는 숫자 카드의 개수
N_numbers = set(map(int, input().split())) # 숫자 카드에 적혀있는 정수
M = int(input()) #가지고 있어야할 숫자 카드의 개수
M_numbers = map(int, input().split()) # 가지고 있어야할 숫자

result = []
for num in M_numbers:
    result.append(1 if num in N_numbers else 0)

for i in result:
    print(i)