
# intellisence 에서 indent 줄보기 보정을 안해줘서 for 문 안에 for을 넣은 걸 못봐서 1시간을 날렸다. 
# 난 프로그래머스가 정말 싫어... 인텔리센스 돌려줘............ 살려줘.... 
# 이런 원시적인 이유로 디버깅을 못하는건 억울하다고 생각해...


def solution(fees, records):
    answer = []
    
    defaultTime = fees[0]
    defaultFee = fees[1]
    unitTime = fees[2]
    unitFee = fees[3]
    endofDay = 23 * 60 + 59     # 23:59 in minutes
    
    # 차량 입출고표 carNum : [마지막 기록시간, 총 이용시간, 입출고상태]
    cars = {}
    carList = []
    
    # 차량 입출고표 계산
    for line in records : 
        # line = "05:34 5961 IN"
        time, carNum, inout = line.split(' ')
        carNum = int(carNum)
        
        hour, minute = list(map(int, time.split(':')))
        lastSeen = hour * 60 + minute
        if inout == "OUT" : 
            # 반드시 cars에 등록이 되어있어야한다 
            
            # 총 이용시간 계산 
            cars[carNum][1] += lastSeen - cars[carNum][0]
            cars[carNum][2] = inout
            # 마지막 기록시간 업데이트
            cars[carNum][0] = lastSeen
        else : # "IN"
            if carNum in carList : 
                # 마지막 기록시간 업데이트
                cars[carNum][0] = lastSeen
                cars[carNum][2] = inout
            else : 
                carList.append(carNum)
                cars[carNum] = [lastSeen, 0, inout]
        
    carList.sort()
        
    for carNum in carList : 
        finalTime = cars[carNum][1]
        if cars[carNum][2] == "IN" : # 출차 내역이 없는 차량
            finalTime += endofDay - cars[carNum][0]

        if 0 < finalTime <= defaultTime : 
            answer.append(defaultFee)
            
        else : 
            fee = defaultFee + int((finalTime - defaultTime) / unitTime + 0.9999999) * unitFee
            answer.append(fee)
            
            
        
        
    return answer
