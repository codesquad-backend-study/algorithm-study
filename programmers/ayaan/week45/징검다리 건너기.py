def solution(stones, k):
    answer = 0

    start = 0
    end = max(stones)

    while start <= end:
        mid = (start + end) // 2
        # skip = 건너뛰는 횟수
        skip = 0
        for val in stones:
            # 밟을 수 없으면 건너뛰는 횟수 증가
            if val <= mid:
                skip += 1
                # 건너뛰는 횟수가 k면 건널 수 없다.
                if skip >= k:
                    break
            else:
                skip = 0

        # 건널 수 없으면 사람 수를 줄인다
        if skip >= k:
            end = mid - 1
        # 건널 수 있으면 사람 수를 늘린다.
        else:
            start = mid + 1
            answer = mid + 1

    return answer
