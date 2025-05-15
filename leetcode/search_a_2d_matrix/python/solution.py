class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        """
        Time complexity: O(log(n*m))
        Auxiliary space complexity: O(1)
        Tags: binary search
        """
        top = 0
        bottom = len(matrix) - 1
        left = 0
        right = len(matrix[0]) - 1
        is_row_found = False

        while top <= bottom:
            middle_row_index = (top + bottom) // 2
            middle_row = matrix[middle_row_index]
            
            if (target >= middle_row[0] and
                    target <= middle_row[-1]):
                is_row_found = True
                break
            elif (target < middle_row[0]):
                bottom = middle_row_index - 1
            else:
                top = middle_row_index + 1
        
        # early exit
        if not is_row_found:
            return False

        while left <= right:
            middle_col_index = (left + right) // 2
            middle_number = middle_row[middle_col_index]

            if target == middle_number:
                return True
            elif target < middle_number:
                right = middle_col_index - 1
            else:
                left = middle_col_index + 1

        return False


print(Solution().searchMatrix([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 3), True)
print(Solution().searchMatrix([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 13), False)