import sys
input = sys.stdin.readline
import itertools

N = input()
array = list(map(int, input().strip().split()))
chklist = [0 for _ in range(sum(array)+2)]
nCr = []

for i in range(1, len(array)+1):
    nCr.extend(itertools.combinations(array,i))
    #배열 뒤에 ,찍히는 이유?

for i in nCr:
    chklist[sum(i)] = 1
    
for i in range(1,len(chklist)):
    if(chklist[i]==1):
        pass
    else:
        print(i)
        break