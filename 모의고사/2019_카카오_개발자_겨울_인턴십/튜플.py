import re


def solution(s):
    a = s.split('},')
    for i in range(len(a)):
        a[i] = re.sub(r"[{}]", "", a[i])
    a.sort(key=lambda x: len(x))

    ans = []
    exist = set()

    for each in a:
        nums = list(map(int, each.split(',')))
        for num in nums:
            if num not in exist:
                ans.append(num)
                exist.add(num)

    return ans
