import sys
input = sys.stdin.readline

#변수 입력 
K, N = map(int, input().split())
listK = []
maxK = 0

# K개 랜선 길이 각각 입력 
# 최대값 받기 
for i in range(0, K) : 
    listK.append(int(input()))

        
# start, end 설정 
start = 1
end = max(listK)

# 가능 불가능 판단 함수 
def check(cutLen : int) : 
    count = 0
    for lans in listK : 
        x = lans // cutLen  #cutLen으로 자르면 랜선 몇개가 나오나요?
        count += x
    if count >= N : 
        return True
    else : 
        return False

# start/end pointer 위치 바뀔 때까지 반복
while (start <= end) : 
    mid = (start + end) // 2
    
    if check(mid) : # 가능! >> 나누는 길이를 늘려봐야겠다 
        start = mid + 1
    else : # 불가능! >> 나누는 길이를 줄여야겠다 
        end = mid - 1

print((start + end)//2)