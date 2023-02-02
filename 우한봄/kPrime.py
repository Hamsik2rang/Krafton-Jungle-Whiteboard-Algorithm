def turnN(n, q):
    rev_base = ''

    while n > 0:
        n, mod = divmod(n, q)
        rev_base += str(mod)

    return rev_base[::-1] 

def isPrime(n):
    if n==1:
        return False
    else:
        for i in range(2, int(n**0.5)+1):
            if n%i==0:
                return False
        return True

def solution(n, k):
    nstring=turnN(n,k)
    
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
        if isPrime(int(p)):
            cnt+=1
    
    return cnt

