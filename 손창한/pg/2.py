import math


def solution(fees, records):
    records = list(record.split() for record in records)
    records.sort(key=lambda x: x[1])

    # set dict
    cars_set = set(record[1] for record in records)
    cars_dict = dict()
    for number in cars_set:
        cars_dict[number] = 0

    # cal minutes
    for time, number, stat in records:
        # hr:mn -> mns
        time = int(time[:2]) * 60 + int(time[3:])
        # -IN or +OUT
        flg = -1 if stat == "IN" else 1
        cars_dict[number] += flg * time

    # calculate parking fee
    def_time, def_fee, unit_time, unit_fee = fees
    answer = []
    for number in sorted(list(cars_set)):
        park_time = cars_dict[number]
        if park_time <= 0:
            park_time += 23 * 60 + 59
        cal_time = park_time - def_time if park_time > def_time else 0
        answer.append(def_fee + math.ceil(cal_time / unit_time) * unit_fee)

    return answer


fees = [1, 461, 1, 10]
records = ["00:00 1234 IN"]
print(solution(fees, records))