# DB 캐시를 적용할 때 캐시 크기에 따른 실행시간 측정 프로그램을 작성
# LRU: 가장 오랫동안 참조되지 않은 페이지를 교체
# 단점: 프로세스가 주기억장치에 접근할 때마다 참조된 페이지에 대한 시간을 기록해야 함 -> 큰 오버헤드가 발생
from collections import deque


def solution(cacheSize, cities):
    time_answer = 0

    # 실행시간 상수 선언
    CACHE_HIT = 1  # 캐시가 이미 존재할 경우
    CACHE_MISS = 5  # 캐시가 없을 경우

    # (list의 크기 == 캐시 크기) -> 제한은 deque로 가능
    deq = deque(maxlen=cacheSize)

    # 캐시 크기(cacheSize)에 따른 실행 시간 계산
    for city in cities:
        # 가장 오랫동안 참조되지 않은 페이지를 교체한다는 조건 적용 (if문)

        # 큐처럼 왼쪽에서 쭉 밀어주는 형태로 더해줌 (존재하지 않으면)
        deq.appendleft(city)

        # 그 후 pop(right)를 하면 됨
        if deq.pop() == city:  # 큐의 가장 오른쪽에 있는 게(가장 오래 된) city와 같으면
            time_answer += CACHE_HIT
        else:
            time_answer += CACHE_MISS

    return time_answer


print(solution(3, ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "Jeju", "Pangyo", "Seoul", "NewYork", "LA"]))
print(solution(3, ["Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul"]))
print(solution(2,
               ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "SanFrancisco", "Seoul", "Rome", "Paris", "Jeju", "NewYork",
                "Rome"]
               ))
