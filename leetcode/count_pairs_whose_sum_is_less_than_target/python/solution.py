# draft
# countPairs([1, 1, 3, 4, 5], 6) -> 5
# 1,4; 1,3; 1,1  add every pair and increase the left pointer
# 1,4; 1,3


class Solution:
    def countPairs(self, numbers: list[int], target: int) -> int:
        """
        Time complexity: O(nlogn)
        Auxiliary space complexity: O(n)
        Tags: two pointers
        """
        numbers.sort()
        counter = 0
        left = 0
        right = len(numbers) - 1

        while left < right:
            if numbers[left] + numbers[right] < target:
                counter += right - left
                left += 1
            else:
                right -= 1

        return counter

    def countPairs(self, numbers: list[int], target: int) -> int:
        """
        Time complexity: O(n2)
        Auxiliary space complexity: O(n)
        Tags: brute force
        """
        numbers.sort()
        counter = 0

        for i in range(len(numbers) - 1):
            for j in range(i + 1, len(numbers)):
                if numbers[i] + numbers[j] < target:
                    counter += 1

        return counter


print(Solution().countPairs([1, 1, 3, 4, 5], 6) == 5)
print(Solution().countPairs([-1, 1, 2, 3, 1], 2) == 3)
print(Solution().countPairs([-6, 2, 5, -2, -7, -1, 3], -2) == 10)
print(Solution().countPairs([6, -1, 7, 4, 2, 3], 8) == 8)
print(Solution().countPairs([-5, 0, -7, -1, 9, 8, -9, 9], -14) == 1)