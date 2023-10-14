# 트럭에는 택배상자를 cap 개 실을 수 있다.
# 트럭이 각 집에 배달, 빈 상자를 수거
# 집 마다 배달 및 수거 상자 개수가 정해짐
# 모든 배달과 수거를 마친 최소 이동거리
# 원하는 개수만큼 배달 및 수거

def solution(cap, n, deliveries, pickups):
    move = 0

    if sum(deliveries) == sum(pickups) == 0:
        return 0

    while True:
        need = 0
        retrieve = 0
        for i in range(n - 1, -1, -1):
            if deliveries[i] + need > cap or pickups[i] + retrieve > cap:
                deliveries[i] -= cap - need
                pickups[i] -= cap - retrieve

                move += n * 2
                n -= (n - 1) - i
                break

            if i == 0:
                move += n * 2
                return move

            need += deliveries[i]
            retrieve += pickups[i]
