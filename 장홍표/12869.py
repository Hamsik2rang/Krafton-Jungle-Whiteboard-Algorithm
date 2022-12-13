import sys
input = sys.stdin.readline

N = int(input().strip())
HPs = list(map(int, input().strip().split()))
counter = 0

if(N == 1):
    print(int(HPs[0]/9))
elif(N == 2):
    while((HPs[0] > 0) or (HPs[1] > 0)):
        if(HPs[0]>HPs[1]):
            HPs[0] -= 9
            HPs[1] -= 3
            counter += 1
        elif(HPs[0]<=HPs[1]):
            HPs[1] -= 9
            HPs[0] -= 3
            counter += 1
    print(counter)
else: #N==3
    pass