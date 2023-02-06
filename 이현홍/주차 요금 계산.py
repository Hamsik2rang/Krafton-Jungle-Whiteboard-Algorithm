def solution(fees, records):
    answer = []
    L = len(records)
    for idx in range(L):
        records[idx] = records[idx].split()
    records.sort(key=lambda x:x[1])
    time_dic = {key:0 for key in sorted(set(map(lambda x:x[1], records)))}
    
    idx = 0
    while idx < L:
        number = records[idx][1]
        h, m = map(int, records[idx][0].split(":"))
        start = h*60 + m
        end = 24*60 -1
        if idx == L-1 or records[idx+1][1] != records[idx][1]:
            idx += 1
        else:
            h, m = map(int, records[idx+1][0].split(":"))
            end = h*60 + m
            idx += 2
        time_dic[number] += end-start
    for key in sorted(time_dic.keys()):
        pay = fees[1]
        residue = max(0, time_dic[key] - fees[0])
        pay += residue // fees[2] * fees[3]
        if residue%fees[2]: pay += fees[3]
        answer.append(pay)
    return answer
