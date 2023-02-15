from collections import deque

def solution(n, info):
    answer = []
    biggest = 0
    answer = [-1]
    #(now, total, left, arrow, appeachTotal)
    queue = deque([(0,0,n,[],0)])

    while(queue):
        now, total, left, arrow, appeachTotal = queue.popleft()
        if now==11:
            dif = total-appeachTotal
            if appeachTotal>=total:
                continue

            if biggest==0 or biggest<dif:
                if(left>0):
                    arrow[-1] = left
                biggest = dif
                answer = arrow
            elif biggest==dif:
                if(left>0):
                    arrow[-1] = left
                for i in range(0,11)[::-1]:
                    if arrow[i]>answer[i] :
                        answer = arrow
                        break
                    elif answer[i]>arrow[i]:
                        break
            continue

        appeach = info[now]
        if(appeach>0):
            queue.append((now+1, total, left, arrow + [0], appeachTotal+10-now))
        else:
            queue.append((now+1, total, left, arrow + [0], appeachTotal))
        if left>0 and left>appeach:
            queue.append((now+1, total+10-now, left-appeach-1, arrow + [appeach+1], appeachTotal))
        
    return answer