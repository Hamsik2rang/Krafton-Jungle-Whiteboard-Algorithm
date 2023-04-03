# 1회차
# 시간제한 1초 / 128MB
# 산성용액특성값 = 1 ~ 10^9
# 염기성용액특성값 = -1 ~ -10^9
# 주어진 용액을 2개섞어 가장 0에 가까운 용액 만들기
# 용액의 수 = 2 ~ 10^5
# combination을 사용시 => 10^12메모리, 사용금지
# for^2 사용시 => 시간초과, 사용금지

#이분탐색을 이용해 풀어보기
import sys
input = sys.stdin.readline

from math import inf

liquidArray = []

N = int(input().strip())
liquidArray = list(map(int, input().strip().split()))
liquidArray.sort()
minValue = [inf, inf, inf]

for i in range(N):
    target = -liquidArray[i]
    left = 0
    right = N-1
    mid = (left+right)//2
    while(left < right):
        mid = (left+right)//2
        if(liquidArray[mid] == target):
            pt = mid
            break
        elif(liquidArray[mid] < target):
            left = mid+1
        else:
            right = mid-1
    pt = mid
    
    if(pt != inf):
        if(pt != i):
            if(abs(liquidArray[i] + liquidArray[pt]) < minValue[2]):
                minValue = [liquidArray[i], liquidArray[pt], abs(liquidArray[i] + liquidArray[pt])]
        if(left != i):
            if(abs(liquidArray[i] + liquidArray[left]) < minValue[2]):        
                minValue = [liquidArray[i], liquidArray[left], abs(liquidArray[i] + liquidArray[left])] 
        if(right != i):
            if(abs(liquidArray[i] + liquidArray[right]) < minValue[2]):        
                minValue = [liquidArray[i], liquidArray[right], abs(liquidArray[i] + liquidArray[right])]

            
print(min(minValue[0], minValue[1]),max(minValue[0], minValue[1]), sep=' ') #오름차순출력!