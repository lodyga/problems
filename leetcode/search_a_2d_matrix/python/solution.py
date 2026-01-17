class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        """
        Time complexity: O(log(n*m))
        Auxiliary space complexity: O(1)
        Tags:
            A: binary search
        """
        top = 0
        bottom = len(matrix) - 1

        while top <= bottom:
            middle_row_index = (top + bottom) >> 1
            middle_row = matrix[middle_row_index]

            if middle_row[0] <= target <= middle_row[-1]:
                left = 0
                right = len(matrix[0]) - 1
                
                while left <= right:
                    middle = (left + right) >> 1
                    middle_num = middle_row[middle]

                    if target == middle_num:
                        return True
                    elif target < middle_num:
                        right = middle - 1
                    else:
                        left = middle + 1
                
                return False

            elif target < middle_row[0]:
                bottom = middle_row_index - 1
            else:
                top = middle_row_index + 1
        
        return False


print(Solution().searchMatrix([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 3) == True)
print(Solution().searchMatrix([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 13) == False)
