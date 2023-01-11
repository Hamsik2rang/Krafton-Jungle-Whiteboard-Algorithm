'''
1. 문제의 시간 제한은?
1초

2. 문제의 최대 N값은?(항상 N이 아닐 수도 있으며, 여러 개일 수도 있음)
k : 100000
L : 500000

3. 1, 2를 바탕으로 이 문제에서 허용하는 최대 시간 복잡도는?
??

4. 3을 바탕으로 문제를 읽었을 때 사용할 수 있는 알고리즘은?
딕셔너리 구현 문제

5. 왜 4라고 생각했는가?
리스트로 구현하면 시간초과가 뜸

'''

import sys
input = sys.stdin.readline

max, cnt = map(int, input().split())
wait = {}

for _ in range(cnt):
    new = input().strip()
    wait[new] = _

list = sorted(wait.items(), key = (lambda x:x[1]))

for i in range(max):
    if i==len(list):break
    print(list[i][0])