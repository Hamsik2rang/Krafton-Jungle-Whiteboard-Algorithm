#	memory: 30840	time: 1612
import sys

# 소수 검사 함수
def prime(num):
    flag = True
    for i in range(2, num):
        if num % i == 0:
            flag = False
            break
    return flag


for tc in range(int(sys.stdin.readline())):
    origin, target = map(int, sys.stdin.readline().split())

    Q = [0] * 10001
    visit = [1] * 10001
    front = -1
    rear = 0
    Q[rear] = (origin, 0)
    flag = True
    while front < rear:
        front += 1
        number, count = Q[front]
        if number == target:
            print(count)
            flag = False
            break
        else:
            news = []
            for i in range(10):
                if i != 0:
                    news.append(1000 * i + number % 1000)
                news.append(1000 * (number // 1000) + 100 * i + number % 100)       # 하나의 수를 바꿔서 넣을 수 있는 수 전부 집어넣기
                news.append(100 * (number // 100) + 10 * i + number % 10)
                news.append(10 * (number // 10) + i)
            for new in news:
                if visit[new] and prime(new):     # 소수 판별 및 중복된 수 거르기
                    visit[new] = 0
                    rear += 1
                    Q[rear] = (new, count + 1)
    if flag:
        print(-1)
