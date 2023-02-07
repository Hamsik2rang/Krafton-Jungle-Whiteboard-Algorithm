def solution(fees, records):
    baseTime = fees[0]
    baseCost = fees[1]
    cumulativeTime = fees[2]
    cumulativeCost = fees[3]
    timeDict = {}
    feeDict = {}
    answer = ''
    
    for record in records:
        info = record.split(' ')
        time = 0
        if (info[2] == "IN" and info[1] not in timeDict):
            timeDict[info[1]] = info[0]
        elif (info[2] == "OUT"):
            time += (int(info[0].split(':')[0]) - int(timeDict[info[1]].split(':')[0])) * 60
            time += int(info[0].split(':')[1]) - int(timeDict[info[1]].split(':')[0])
            if (info[1] not in feeDict):
                feeDict[info[1]] = time
            else:
                feeDict[info[1]] = feeDict[info[1]] + time
            
    return feeDict
