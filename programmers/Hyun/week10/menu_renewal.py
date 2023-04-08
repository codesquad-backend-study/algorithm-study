import itertools
import time

nums = [i for i in range(20)]
answer_list = []



def nCr(n, ans, r):
    if len(ans) > r:
        return

    if n == len(nums):
        if len(ans) == r:
            temp = [i for i in ans]
            answer_list.append(temp)
        return
    ans.append(nums[n])
    nCr(n + 1, ans, r)
    ans.pop()
    nCr(n + 1, ans, r)


start = time.time()

nCr(0, [], 3)

end = time.time()

print(f"1 : {end-start:.5f}sec ")

start = time.time()

combinations = itertools.combinations([i for i in range(20)], 3)

end = time.time()


print(f"2 : {end-start:.5f}sec")
