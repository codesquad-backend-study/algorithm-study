from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # 뒤부터 탐색하는 것이 더 효율적임
        row, col = 0, len(matrix[0]) - 1

        while row < len(matrix) and col >= 0:
            current = matrix[row][col]

            if current == target:
                return True

            # 뒤부터 탐색하니까 바로 다음 row로 넘어갈 수 있는 거임
            if current < target:
                row += 1
                continue

            # 찾을 가능성이 있으니 왼쪽으로 가면서 탐색
            if current > target:
                col -= 1

        return False
