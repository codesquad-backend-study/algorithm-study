def searchMatrix(matrix, target):
    matrix_start = 0
    matrix_end = len(matrix) - 1
    while matrix_start <= matrix_end:
        matrix_mid = (matrix_start + matrix_end) // 2
        nums = matrix[matrix_mid]
        start = 0
        end = len(nums) - 1

        num = 0
        while start <= end:
            mid = start + (end - start) // 2
            if target < nums[mid]:
                end = mid - 1
            elif nums[mid] < target:
                start = mid + 1
            else:
                return True
            num = nums[mid]
        print(num)
        if num < target:
            matrix_start = matrix_mid + 1
        else:
            matrix_end = matrix_mid - 1
    return False

print(searchMatrix([[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]], 20))
