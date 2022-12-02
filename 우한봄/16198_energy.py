"""
문제 : [백준]16198-에너지 모으기

무게가 주어진 에너지 구슬을 이용해서 일련의 법칙으로 에너지를 모을 때, 
모을 수 있는 에너지 양의 최대값을 구하는 문제
<에너지 모음 법칙>
1. 에너지 구슬 하나를 고른다. 고른 에너지 구슬의 번호를 x라 한다. 단,
첫번째와 마지막 에너지 구슬을 고를 수 없다.
2. x번째 에너지 구슬을 제거한다.
3. W_(x-1) x W_(x+1)의 에너지를 모을 수 있다.
4. n을 1 감소시키고, 에너지 구슬을 1번부터 n번까지로 다시 번호를 매긴다.

[입력]
1. 구슬 갯수 N (3<=n<=10)
2. 에너지 구슬의 무게들

"""
import sys
sys.setrecursionlimit(10**5)
input=sys.stdin.readline

n=int(input())
energy=list(map(int,input().split()))
max_eng=0

def dfs(s): # 내 노드, list, 몇번쨰 idx인지 
    global max_eng
    
    # print(energy)
    if len(energy)==2:
        if s>max_eng:
            max_eng=s
            return 
    else:
        for i in range(1,len(energy)-1):
            score=energy[i-1]*energy[i+1]
            temp=energy[i]
            del energy[i]
            dfs(s+score)
            energy.insert(i, temp)
    
dfs(0)  
print(max_eng)


# 1 2 3 4
# 2x4+ 1X4


# 100 2 1 3 100
# 100x1+ 100x3+ 100x100

# 2 2 7 6 90 5 9
# 5번 연산 가능
# 90x9+ 90*7+ 90*2+ 2*90 + 2*9
