class Solution:
    def specialArray(self, numbers: list[int]) -> int:
        """
        Time complexity: O(nlogn)
        Auxiliary space complexity: O(1)
        Tags: binary search
        """
        left = 1
        right = len(numbers)
        special_number = -1

        while left <= right:
            # number & number count
            middle = (left + right) // 2
            special_count = sum(True for number in numbers if number >= middle)

            if special_count >= middle:
                if special_count == middle:
                    special_number = middle
                left = middle + 1
            else:
                right = middle - 1

        return special_number


print(Solution().specialArray([3, 5]) == 2)
print(Solution().specialArray([0, 0]) == -1)
print(Solution().specialArray([0, 4, 3, 0, 4]) == 3)
print(Solution().specialArray([3, 6, 7, 7, 0]) == -1)