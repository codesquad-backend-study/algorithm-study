import math


def calculate_rate(car_records: list, fees: list):
    basic_time = fees[0]
    basic_rate = fees[1]
    unit_time = fees[2]
    unit_rate = fees[3]

    arrival_times = [car_records[0] * 60 + car_records[1] for idx, car_records in enumerate(car_records) if
                     idx % 2 == 0]
    departure_times = [car_records[0] * 60 + car_records[1] for idx, car_records in enumerate(car_records) if
                       idx % 2 == 1]

    summation_times = 0
    for i in range(len(arrival_times)):
        summation_times += departure_times[i] - arrival_times[i]

    additional_time = summation_times - basic_time if summation_times > basic_time else 0

    rate = basic_rate + math.ceil(additional_time / unit_time) * unit_rate

    return rate


def solution(fees, records):
    car_entrance_checker = {}
    cars = {}
    bills = {}

    for each in records:
        time, car_number, state = each.split()
        time = tuple(map(int, time.split(":")))

        if state == 'IN':
            car_entrance_checker[car_number] = 1
            if car_number not in cars:
                cars[car_number] = []
            cars[car_number].append(time)
        elif state == 'OUT':
            cars[car_number].append(time)
            del car_entrance_checker[car_number]

    for car_number in car_entrance_checker.keys():
        cars[car_number].append((23, 59))

    for car_number, records in cars.items():
        bills[car_number] = calculate_rate(records, fees)

    ans = []
    for car_number in sorted(bills.keys()):
        ans.append(bills[car_number])

    return ans
