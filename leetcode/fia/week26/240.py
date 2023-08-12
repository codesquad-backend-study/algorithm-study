class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for line in matrix:
            start, end = 0, len(line) - 1

            while start <= end:
                mid = start + (end - start) // 2

                if line[mid] == target:
                    return True
                if line[mid] > target:
                    end = mid - 1
                elif line[mid] < target:
                    start = mid + 1

        return False
