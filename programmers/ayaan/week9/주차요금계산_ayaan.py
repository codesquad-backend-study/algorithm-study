def solution(fees, records):
    answer = []
    
    in_time = {}
    parking_time = {}
    
    for record in records:
        data = record.split()
        if data[2] == "IN":
            in_time[data[1]] = data[0]
        else:
            IN = in_time[data[1]]
            OUT = data[0]
            if data[1] in parking_time:
                parking_time[data[1]] += calTime(IN, OUT)
            else:
                parking_time[data[1]] = calTime(IN, OUT)
            del in_time[data[1]]
    for car, time in in_time.items():
            if car in parking_time:
                parking_time[car] += calTime(time, "23:59")
            else:
                parking_time[car] = calTime(time, "23:59")
    
    parking_time = sorted(parking_time.items(), key=lambda x : int(x[0]))
    
    for car, time in parking_time:
        fee = fees[1]
        if time > fees[0]:
            if (time - fees[0]) % fees[2] == 0:
                fee += (time - fees[0]) // fees[2] * fees[3]
            else:
                fee += ((time - fees[0]) // fees[2] + 1) * fees[3]
            
        answer.append(fee)
    return answer

def calTime(IN, OUT):
    in_split = IN.split(":")
    out_split = OUT.split(":")
    return (int(out_split[0]) * 60 + int(out_split[1])) - (int(in_split[0]) * 60 + int(in_split[1]))


# solution([180, 5000, 10, 600], ["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"])
solution([1, 461, 1, 10], ["00:00 1234 IN"])