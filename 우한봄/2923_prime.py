import sys, math
sys.stdin=open("input.txt","r")
input=sys.stdin.readline

def is_prime_number(a):
    if(a<2):
        return False
    for i in range(2, int(math.sqrt(a))+1):
        if (a%i==0):
            return False
    return True

def dfs(num):
    if len(str(num))==n:
        print(num)
    else:
        for i in range(10):
            temp=num*10+i
            if is_prime_number(temp):
                dfs(temp)
 
n=int(input())            
for i in [2,3,5,7]:
    dfs(i)
