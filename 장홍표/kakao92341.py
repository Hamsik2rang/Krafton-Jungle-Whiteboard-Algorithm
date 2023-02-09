# 시간은 24시간을 분으로 계산 (24*60분 = 1440분 ->1일)
fees = [180, 5000, 10, 600]
records = [
    "05:34 5961 IN",
    "06:00 0000 IN",
    "06:34 0000 OUT",
    "07:59 5961 OUT",
    "07:59 0148 IN",
    "18:59 0000 IN",
    "19:09 0148 OUT",
    "22:59 5961 IN",
    "23:00 5961 OUT",
]

carlist = {}
feelist = []


def solution(fees, records):
    basetime, basefee, cnttime, cntfee = fees

    parktime = 0

    timestr = "00:00"
    carnum = "0000"
    status = "IN"

    for i in range(len(records)):
        timestr, carnum, status = records[i].split(" ")
        parktime = (int)(timestr[:2]) * 60 + (int)(timestr[3:])
        print(parktime)
        if status == "IN":
            carlist[carnum] = parktime
        else:
            feelist.append(parktime - carlist.get(carnum))


# answer = []
# return answer


solution(fees, records)


print(carlist)
print(feelist)
