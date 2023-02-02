def isPrime(x):
    if x < 2:
        return 0
    for i in range(2, int(x**.5)+1):
        if x%i == 0:
            return 0
    return 1

def toBase(n, b):
    ret = ''
    while n:
        ret = str(n%b) + ret
        n //= b
    return ret

def solution(n, k):
    a = toBase(n, k).split('0')
    answer = 0
    for x in a:
        if x:
            answer += isPrime(int(x))
    return answer

n, k = map(int, input().split())
print(solution(n, k))
