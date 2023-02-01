# 전부 통과 BUT 테스트1 무한루프 

def trans_num(n, k) : 
    ntransform = ""
    
    if k == 10 : 
        return str(n)
    
    while n >= k : 
        ntransform = str(n % k) + ntransform
        n = n // k
    ntransform = str(n % k) + ntransform    
    return ntransform   # string

def isprime(numStr) : 
    num = int(numStr)
    
    prime = [2, 3, 5, 7]
    
    if num in prime : 
        # 한자리수 소수
        return True
    elif num % 2 == 0 or num == 1: 
        # prime must not be even 
        return False 
    else : 
        for x in range(3, num // 2) : 
            if num % x == 0 : 
                return False
    # if all pass, then prime number
    return True

def solution(n, k):
    answer = -1
    # returns string
    ntransform = trans_num(n, k)
    
    count = 0
    
    # split()을 쓰면 되는 일이었다. 나는 바보다.
    nList = ntransform.split('0')
    
    for i in nList : 
        if i == "" : 
            continue
        elif isprime(i) : 
            count += 1
    
   
    answer = count
    return answer





    # front = 0
    # back = 0
    # count = 0
    # while back != len(ntransform) : 
    #     if back == len(ntransform) - 1 : 
    #         # last 
    #         newN = ntransform[front:]
    #         if len(newN) < 1 : 
    #             back += 1
    #             continue
    #         elif isprime(newN) : 
    #             count += 1
                
    #         front = back + 1
    #     elif ntransform[back + 1] == "0" : 
    #         newN = ntransform[front:back + 1]

    #         if len(newN) < 1 : 
    #             back += 1
    #             continue
    #         elif isprime(newN) : 
    #             count += 1
                
    #         front = back + 1
    #     back += 1

