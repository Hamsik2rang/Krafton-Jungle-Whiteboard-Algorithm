def solution(n, k):
    tmp = ''
    answer = 0

    while n > k:
        tmp += str(n % k)
        n = n//k
    tmp += str(n)

    tmp = tmp[::-1]
    nums = tmp.split('0')
    nums = list(filter(None, nums))

    for num in nums:
        num = int(num)
        if isPrime(num): answer += 1

    return answer


def isPrime(n):
    if n == 1:
        return False
    else:
        for i in range(2, int(n**0.5)+1):
            if n % i == 0:
                return False
        return True
