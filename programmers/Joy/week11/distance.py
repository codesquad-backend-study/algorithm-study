class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        answer = []

        for i in range(len(nums)) :
            tmp = nums[i]
            tmp2 = target - tmp
            if nums.count(tmp2) == 0 :
                continue
            idx = nums.index(tmp2)
            if idx == i :
                continue
            answer.append(i)
            answer.append(idx)
            break

        return answer

        # dic = {k:[] for k in nums}

        # for i, k in enumerate(nums) :
        #     dic[k].append(i)
