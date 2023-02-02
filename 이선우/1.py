convertNum = ''
numList = []

def convert(n,k):
    global convertNum
    if n >= k:
        convert(n // k, k)
    convertNum += str(n % k)
    return

def isPrime(num):
    if num == 1:
        return False
    for n in range(2, num):
        if num % n == 0:
            return False
    return True

def solution(n, k):
    answer = 0
    convert(n, k)
    numList = convertNum.split('0')
    for n in numList:
        if n != '':
            if isPrime(int(n)):
                answer += 1
    return answer
