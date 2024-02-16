import collections


def find(gems):
    left = right = idx = 0

    needs = set(gems)
    ans = []
    while True:
        basket = collections.defaultdict(int)
        while len(basket) < len(needs):
            if right >= len(gems):
                return ans
            basket[gems[right]] += 1
            right += 1
        right -= 1

        while len(basket) == len(needs):
            basket[gems[left]] -= 1
            if basket[gems[left]] == 0:
                del basket[gems[left]]
            left += 1
        left -= 1

        ans.append((right - left + 1, left + 1, right + 1))

        left += 1
        right = left


def solution(gems):
    ans = find(gems)
    ans.sort()
    return [ans[0][1], ans[0][2]]
