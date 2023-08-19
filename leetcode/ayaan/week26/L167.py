def twoSum(numbers, target):
    for i, number in enumerate(numbers):
        start = i + 1
        end = len(numbers) - 1
        find_number = target - number

        while start <= end:
            mid = start + (end - start) // 2
            if find_number < numbers[mid]:
                end = mid - 1
            elif numbers[mid] < find_number:
                start = mid + 1
            else:
                return [i + 1, mid + 1]

twoSum([2, 7, 11, 15], 9)
