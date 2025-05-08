class Solution:
    def sortedSquares(self, numbers: list[int]) -> list[int]:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(n)
        Tags: two pointers
        """
        squared_list = []
        left = 0
        right = len(numbers) - 1

        while left <= right:
            if abs(numbers[left]) > abs(numbers[right]):
                squared_list.append(numbers[left] ** 2)
                left += 1
            else:
                squared_list.append(numbers[right] ** 2)
                right -= 1
        
        squared_list.reverse()
        return squared_list


print(Solution().sortedSquares([-4, -1, 0, 3, 10]) == [0, 1, 9, 16, 100])
print(Solution().sortedSquares([-7, -3, 2, 3, 11]) == [4, 9, 9, 49, 121])
print(Solution().sortedSquares([1, 2, 3]) == [1, 4, 9])
print(Solution().sortedSquares([-3, -2, -1]) == [1, 4, 9])
print(Solution().sortedSquares([0]) == [0])
print(Solution().sortedSquares([0, 1]) == [0, 1])
print(Solution().sortedSquares([-10000, -9999, -7, -5, 0, 0, 10000]) == [0, 0, 25, 49, 99980001, 100000000, 100000000])
print(Solution().sortedSquares([-1, 1]) == [1, 1])
print(Solution().sortedSquares([-1, 1, 1]) == [1, 1, 1])
print(Solution().sortedSquares([-3, -3, -2, 1]) == [1, 4, 9, 9])