from cmath import e
import sys, math
sys.stdin=open("input.txt","r")
input=sys.stdin.readline

# def if_Sprime(number):
#     #자리수 알아낸후
#     #하나씩 매칭?
#     return 

def is_prime_number(n):
    array=[True]*(10**n)
    array[1]=False
        
    for i in range(2, 10**n):
        if array[i]:
            j=2
            while i*j <10**n:
                array[i*j]=False
                j+=1

            k=10**(n-1)
            while k>0:
                if not array[i//k]:
                    array[i]=False
                k//=10

    return [i for i in range(10**(n-1),10**n) if array[i]]
 
n=int(input())            
print(*is_prime_number(n), sep="\n")
