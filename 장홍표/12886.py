import sys
input = sys.stdin.readline

log = []

stones = list(map(int, input().strip().split()))
odd = 0
answer = -1

if(not sum(stones)%3):
    if(stones[0]%2 and stones[1]%2 and stones[2]%2):
        if(stones[0] == stones[1] == stones[2]):
            answer = 1
        else:
            answer = 0
    elif():
        pass
else:
    answer = 0

print(answer)