def permutation(arr, r):
    # 정렬된 출력을 위해 오름차순 정렬
    arr = sorted(arr)
    # 그 index에 값을 썼는지 저장하는 배열
    # 모든 순열을 하나씩 만들고 출력해야 함 -> 즉, 중복값이 저장되면 안 됨
    used = [0 for _ in range(len(arr))]

    # 실제 순열을 만들 함수
    def generate(chosen, used):
        # chosen: 순열의 원소를 저장하는 배열
        # 이 배열에 값을 하나씩 추가 -> 그 개수가 r이 되는 순간 하나의 순열이 만들어졌다는 의미
        if len(chosen) == r:
            print(chosen)
            return

        # 핵심 로직
        # 모든 순열은 arr index의 0부터 i - 1번째 값으로 시작 -> 반복문 필요
        for i in range(len(arr)):
            # 해당 변수가 쓰이지 않았으면 (중복값이 저장되지 안 되기 때문)
            if not used[i]:
                # 순열의 원소를 추가
                chosen.append(arr[i])
                # 사용됐다는 표시인 1로 저장
                used[i] = 1

                # 재귀 반복
                generate(chosen, used)
                # 0으로 다시 초기화
                used[i] = 0

                # 하나가 만들어졌으니 없애주기
                chosen.pop()

    generate([], used)


print(permutation('PER', 2))
print(permutation([1, 2, 3, 4], 3))