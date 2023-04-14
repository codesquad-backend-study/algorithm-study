def combination(arr, r):
    # 정렬된 출력을 위해 오름차순 정렬
    arr = sorted(arr)

    # 실제 조합을 만들 함수
    def generate(chosen):
        # chosen: 조합의 원소를 저장하는 배열
        # 이 배열에 값을 하나씩 추가 -> 그 원소 개수가 r개가 되는 순간 하나의 조합이 만들어졌다는 의미
        if len(chosen) == r:
            print(chosen)
            return

        # 반복문의 시작(start)을 chosen의 "마지막 값 그 다음"으로 함
        if chosen:
            start = arr.index(chosen[-1]) + 1
        # chosen이 비어있으면 start가 0 즉, 0부터 시작
        else:
            start = 0

        # 핵심 로직
        # 조합은 순열과 달리 순서를 고려하지 않음 -> 즉, "제한"이 꼭 필요
        for i in range(start, len(arr)):
            # 조합의 원소 추가
            chosen.append(arr[i])

            # 재귀 반복
            generate(chosen)

            # 하나가 만들어졌으니 없애주기
            chosen.pop()

    generate([])


print(combination('QWERT', 3))
print(combination([1, 2, 3, 4, 5], 3))
