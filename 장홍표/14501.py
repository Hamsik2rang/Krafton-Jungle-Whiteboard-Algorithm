import sys
input = sys.stdin.readline
#퇴사이전 최대보수

N = int(input())
#퇴사일(Max 15)
dp = [0 for _ in range(N)] 
#해당 일까지 최대 비용 (dp)
