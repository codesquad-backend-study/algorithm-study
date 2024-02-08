from typing import List


def solution(s: str) -> List[int]:
    answer: List[int] = []
    count_hash = {}

    s = s.replace('{', '').replace('}', '')
    tmp = list(map(int, s.split(',')))
    for num in tmp:
        if num in count_hash:
            count_hash[num] += 1
            continue

        count_hash[num] = 1

    # count_hash[x] 즉 hash map의 value를 기준으로 높은 것부터 정렬
    # 왜냐하면 튜플이란 그 숫자가 많이 존재하는 것부터 나열되니
    answer = sorted(count_hash, key=lambda x: count_hash[x], reverse=True)

    return answer
