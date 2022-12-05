'''
백트래킹으로 모든 경우 탐색
'''
import sys
input = sys.stdin.readline

n = int(input())

w_list = list(map(int, input().split()))
maxEnergy = 0

def backTrack(list, energy):
    global maxEnergy
    if len(list)<3:
        maxEnergy = max(energy, maxEnergy)
        return
    
    for i in range(2, len(list)):
        new = list[i] * list[i-2]
        popped = list.pop(i-1)
        backTrack(list, energy+new)
        list.insert(i-1, popped)

backTrack(w_list, 0)
print(maxEnergy)