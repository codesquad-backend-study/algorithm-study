# math.ceil() -> 파이썬에서의 올림 함수
import math


# 누적 주차 시간(분) -> parking_m을 넣으면 주차 요금 리턴하는 함수
def calculate_fee(parking_m, basic_t, basic_fee, unit_t, unit_fee):
    return basic_fee + math.ceil((parking_m - basic_t) / unit_t) * unit_fee


def solution(fees, records):
    answer = []
    dict_in_out = {}
    dict_m = {}
    dict_fee = {}

    # 이 문제에서 시간은 모두 (분)으로 바꿀 거임
    # 00:00부터 23:59까지의 시간(분)
    max_m = 24 * 60 - 1
    basic_t, basic_fee, unit_t, unit_fee = int(fees[0]), int(fees[1]), int(fees[2]), int(fees[3])

    for record in records:
        tmp_t, car_num, in_out = record.split()
        # 차량이 입차되거나 출차된 시각 -> (분)으로 저장
        tmp_h, tmp_m = tmp_t.split(':')
        m = (int(tmp_h) * 60 + int(tmp_m))
        # OUT일 경우에는 그 차량의 주차 시각 차이를 계산
        if in_out == 'OUT':
            diff_m = m - dict_m[car_num]
            # 만약 dict_fee[car_num]이 존재하면 value 값을 더해줘야지 -> 그래야 나중에 차 번호로 정렬할 수 있음
            if car_num in dict_fee:
                dict_fee[car_num] = calculate_fee(diff_m, basic_t, basic_fee, unit_t, unit_fee) + dict_fee[car_num]
            else:
                dict_fee[car_num] = calculate_fee(diff_m, basic_t, basic_fee, unit_t, unit_fee)
        # IN인 경우에는 현재 시간 저장
        else:
            dict_m[car_num] = m

        # IN OUT 정보 저장
        dict_in_out[car_num] = in_out

    # 만약, value 값이 OUT인 차량이 있으면 그 key값을 찾고
    # max_m을 이용하여 23:59분까지 출차된 걸로 계산하면 됨

    print(dict_m)
    print(dict_fee)
    print(dict_in_out)
    return answer


# result: [14600, 34400, 5000]
print(solution([180, 5000, 10, 600],
               ["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN",
                "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"]))
