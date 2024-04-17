# 각 음식을 섭취하는데 일정 시간이 소요됨 => food_times
# 회전판은 1초마다 움직인다.
## 남은 음식 중 다음으로 섭취해야 할 가장 가까운 번호로 이동한다.
## K+1 초에 몇 번 음식부터 섭취해야 하는가?

import heapq


def solution(food_times, k):
    heap = []

    for idx, time in enumerate(food_times):
        heapq.heappush(heap, (time, idx))

    rest_cnt = len(food_times)
    prev_time = 0
    while heap:
        time, _ = heap[0]
        if k >= (time - prev_time) * rest_cnt:  # 가장 작은 시간만큼 바퀴를 돌 수있는 경우
            heapq.heappop(heap)
            k -= (time - prev_time) * rest_cnt
            prev_time = time
            rest_cnt -= 1
        else:  # 돌 수 없는 경우
            heap.sort(key=lambda x: x[1])
            idx = k % len(heap)
            return heap[idx][1] + 1

    return -1
