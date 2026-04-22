class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        """
        Time complexity: O(log(n*m))
        Auxiliary space complexity: O(1)
        Tags:
            A: binary search
        """
        ROWS = len(matrix)
        COLS = len(matrix[0])
        left = 0
        right = COLS - 1
        top = 0
        bottom = ROWS - 1
        is_row_found = False

        while top <= bottom:
            mid = (top + bottom) // 2
            mid_row = matrix[mid]

            if mid_row[0] <= target <= mid_row[-1]:
                is_row_found = True
                row_idx = mid
                break
            elif target < mid_row[0]:
                bottom = mid - 1
            else:
                top = mid + 1

        if not is_row_found:
            return False

        while left <= right:
            mid = (left + right) // 2
            mid_num = matrix[row_idx][mid]

            if target == mid_num:
                return True
            elif target < mid_num:
                right = mid - 1
            else:
                left = mid + 1

        return False


print(Solution().searchMatrix([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 3) == True)
print(Solution().searchMatrix([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 13) == False)
