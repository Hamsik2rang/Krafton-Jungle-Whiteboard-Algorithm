import sys
input = sys.stdin.readline
# N < 500,000

from collections import deque

N = int(input().strip())
cards = deque(i for i in range(1,N+1))

while(len(cards)!=1):
    cards.popleft()
    cards.append(cards.popleft())
    
print(cards[0])