import math
from stringprep import in_table_a1
def String_to_minute(str_t):
    h=int(str_t[:2])
    m=int(str_t[3:])
    
    return h*60+m

def solution(fees, records):
    in_dir={}
    out_dir={}
    for r in records:
        time, car_num, c_type=r.split(" ")
        m_time=String_to_minute(time)
        if c_type=="IN":
            try:
                in_dir[car_num].append(m_time)
            except:
                in_dir[car_num]=[]
                in_dir[car_num].append(m_time)
                
        if c_type=="OUT":
            try:
                out_dir[car_num].append(m_time)
            except:
                out_dir[car_num]=[]
                out_dir[car_num].append(m_time)
    
    car_lst=sorted(list(in_dir.keys()))
    answer=[]
    
    for car in car_lst:
        in_times=in_dir[car]
        try:
            out_times=out_dir[car]
        except:
            out_times=[]
        
        if len(in_times)!=len(out_times):
            out_times.append(String_to_minute("23:59"))
        
        park_time=0
        for i in range(len(in_times)):
            park_time+=out_times[i]-in_times[i]
        
        if park_time > fees[0]:
            fee=fees[1]+math.ceil((park_time-fees[0])/fees[2])*fees[3]
        else:
            fee=fees[1]
            
        answer.append(fee)
        
    
    return answer

fees=[1, 461, 1, 10]
records=["00:00 1234 IN"]
print(solution(fees,records))