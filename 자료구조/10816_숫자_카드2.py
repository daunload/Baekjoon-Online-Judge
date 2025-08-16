import sys
from collections import Counter

input = sys.stdin.readline

N = int(input())

n_cards = list(map(int, input().split()))

M = int(input())
m_cards = list(map(int, input().split()))

card_count = Counter(n_cards)

result = [card_count[card] for card in m_cards]

print(*result)