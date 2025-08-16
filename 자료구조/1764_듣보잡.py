import sys

input = sys.stdin.readline

N, M = map(int, input().split())

N_NAMES = {input().strip() for _ in range(N)}
M_NAMES = {input().strip() for _ in range(M)}

N_M_NAMES = sorted(N_NAMES & M_NAMES)

print(len(N_M_NAMES))
print("\n".join(N_M_NAMES))