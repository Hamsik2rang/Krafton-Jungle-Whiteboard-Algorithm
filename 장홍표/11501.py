'''
### 주식 ###
1. 문제의 시간 제한은?
5초
2. 문제의 최대 N값은?(항상 N이 아닐 수도 있으며, 여러 개일 수도 있음)
1,000,000
3. 1, 2를 바탕으로 이 문제에서 허용하는 최대 시간 복잡도는?
N / logN
4. 3을 바탕으로 문제를 읽었을 때 사용할 수 있는 알고리즘은?
?
5. 왜 4라고 생각했는가?
문제에 맞추어 반복수행작업을 해야 함
'''
import sys; input = sys.stdin.readline
import copy
from collections import deque

T = int(input().strip())

for _ in range(T):
    day = int(input().strip())
    checklist = [0 for _ in range(day)]
    money = 0
    stock = list(map(int, input().strip().split()))
    # stock = (주가1) (주가2) (주가3) (주가4) (주가5)...
    # cklst =    0       0      0       0      0   ...
    # 주가 최댓값 구함. 그전 주식은 전부 구매. ->  반복