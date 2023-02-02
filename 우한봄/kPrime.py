def turnN(n, q):
    rev_base = ''

    while n > 0:
        n, mod = divmod(n, q)
        rev_base += str(mod)

    return rev_base[::-1] 

def primeNumberSieve(n):
    a=[0 for _ in range(n*10)]
    for i in range(2,n*10):
        a[i] = i;
    
    for i in range(2,n*10):
        if a[i]==0:
            continue
        for j in range(i*2, n*10,i):
            a[j] = 0;

    return a

def solution(n, k):
    nstring=turnN(n,k)
    primeArr=primeNumberSieve(n)
    
    primeLst=[]
    prime=''
    for s in nstring:
        if s=="0":
            if prime=='':
                continue
            primeLst.append(prime)
            prime=''
        else:
            prime+=s
    primeLst.append(prime)
    
    cnt=0
    for p in primeLst:
        if primeArr[int(p)]!=0:
            cnt+=1
    
    return cnt

