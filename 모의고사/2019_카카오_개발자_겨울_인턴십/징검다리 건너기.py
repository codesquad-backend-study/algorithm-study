def go_check(stones, n, k):
    skip = 1
    for stone in stones:
        if stone <= n:
            skip += 1
            if skip > k:
                return False
        else:
            skip = 1
    return True


def solution(stones, k):
    left = 0
    right = 200000000 + 10
    ans = 0
    while left <= right:
        mid = (left + right) // 2

        if go_check(stones, mid, k):
            ans = mid + 1
            left = mid + 1
        else:
            right = mid - 1

    return ans
