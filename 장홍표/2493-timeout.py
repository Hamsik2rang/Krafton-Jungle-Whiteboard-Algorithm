'''
1. 문제의 시간 제한은?
    1.5초
2. 문제의 최대 N값은?
    500,000
3. 1, 2를 바탕으로 이 문제에서 허용하는 최대 시간 복잡도는?
    O(N)
4. 3을 바탕으로 문제를 읽었을 때 사용할 수 있는 알고리즘은?
    모르겠음 이분탐색? 빠른 자료구조?
5. 왜 4라고 생각했는가?
    논리과정대로 뒤에서 부터 가장 가까운 탐색을 하면,
    500000^2의 시간이 소요
    가장 높은숫자를 return하는것도 안됨
'''


import sys
input = sys.stdin.readline
#시간복잡도 500k * 100000k

input()
tops = list(map(int, input().strip().split()))
receiveList = [0 for _ in range(len(tops))]

for i in range(len(tops)):
    for j in range(len(tops[:i])):
        if(tops[i]>=max(tops[:i])):
            break
        tmp = tops[:i]
        if(tmp[-(j+1)]>tops[i]):
            receiveList[i] = tops.index(tmp[-(j+1)])+1
            break

for i in range(len(receiveList)):
    print(receiveList[i], end=' ')