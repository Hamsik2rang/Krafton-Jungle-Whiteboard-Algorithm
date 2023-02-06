import math

def solution(fees, records):
    parking = dict()
    stack = dict()
    
    for record in records:
        time, car, cmd = record.split()
        hour, minute = time.split(":")
        minutes = int(hour) * 60 + int(minute) # 시간 -> 분 환산

        if cmd == 'IN':
            parking[car] = minutes
        elif cmd == 'OUT':
            try:
                stack[car] += minutes - parking[car]
            except:
                stack[car] = minutes - parking[car]
            del parking[car] # 출차 차량 삭제
    
    # 출차 기록 없는 차 23:59 출차 처리
    for car, minute in parking.items():
        try:
            stack[car] += 23*60+59 - minute
        except:
            stack[car] = 23*60+59 - minute
        
    return [get_fee(time, fees) for car, time in sorted(list(stack.items()), key=lambda x: x[0])]

def get_fee(minutes, fees):
    return fees[1] + math.ceil(max(0, (minutes - fees[0])) / fees[2]) * fees[3]
