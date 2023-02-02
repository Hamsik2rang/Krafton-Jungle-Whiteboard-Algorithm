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
    # k의 n제곱이 num보다 커질 때, 그 전의 k값 (k^(n-1))을 num에서 빼고, n-1자릿수에 +1
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

        
'''
코드리뷰

1. 파이썬의 경우 진수변환은 다음과 같이 한대요
https://velog.io/@code_angler/%ED%8C%8C%EC%9D%B4%EC%8D%AC-%EC%A7%84%EC%88%98%EB%B3%80%ED%99%982%EC%A7%84%EB%B2%95-3%EC%A7%84%EB%B2%95-5%EC%A7%84%EB%B2%95-10%EC%A7%84%EB%B2%95n%EC%A7%84%EB%B2%95

2. 이 문제의 경우 에라토스테네스까지 쓸 필요는 없고 소수 판별 함수를 따로 작성해서 매번 돌려도 아마 통과가 될 것 같습니다.
N까지 통으로 검사하는 방법 말고, N의 제곱근까지만 검사하는 방식으로만 최적화해서 소수 판별하면 될 것 같아요

'''
        
