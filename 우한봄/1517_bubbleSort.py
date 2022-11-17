from os import popen
import sys

n=int(sys.stdin.readline())
arr=list(map(int, sys.stdin.readline().split()))

cnt=0
def mergeSort(l,r):
    global cnt
    
    if l<r: # 0 2/ 0 1
        mid=(l+r)//2 # 1 / 0
        mergeSort(l,mid) # 0 1 / 0 0
        mergeSort(mid+1,r) # 2 2
        
        a=l #0
        b=mid+1 #2
        tmp=[]
        while a<=mid and b<=r: # 0<=1 2<=2
            if arr[a] <= arr[b]:  
                tmp.append(arr[a])
                a+=1
            else: # 3>=2
                tmp.append(arr[b]) #[2]
                b+=1 # 2
                cnt+=(mid-a+1) # 1
        
        if a<=mid: # 0<=0
            tmp=tmp+arr[a:mid+1] #[2]+[3]
        if b<=r: # 2<=1 x
            tmp=tmp+arr[b:r+1]
            
        for i in range(len(tmp)):
            arr[l+i]=tmp[i] #arr[0]=2, arr[1]=3

mergeSort(0,n-1)
print(cnt)
    
    

#1. 병합 정렬 -> 모두 나눈다
#2. 합쳐 올라가는 과정에서 왼쪽이 오른쪽보다 크다면 cnt+=인덱스차이값

7 9 1 3
