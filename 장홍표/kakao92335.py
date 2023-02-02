def solution(n, k):
    num = int(n)  # 숫자변환
    numlist = list(set(map(str, str(num).split("0"))))
    answer = -1
    return numlist
    # 숫자분리하는 방법, split으로 쓰면 공백제거 어떻게해?
    # 소수찾는 방법 -> 에라토스테네스의 체 (반복해서 쓰고싶지 않은데..)
    # 최대 소수 판별값 -> 1000000의 3진수 -> 10진수로 변환
    # 진수변환은 어떻게해?


def Transcimal(num, k):  # num을 k진수로 변환
    #k의 n제곱이 num보다 커질 때, 그 전의 k값 (k^(n-1))을 num에서 빼고, n-1자릿수에 +1                                                                                      
    ktmp = k
    ret = 0
    while num != 0:
        if num - ktmp > ktmp:
            pass
        elif num - ktmp == ktmp:
            pass
        else:
            pass
        # 몇개로 나눠야되지?
