class Solution:
    def canBeEqual(self, target: list[int], arr: list[int]) -> bool:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(1)
        Tags:
            DS: array
            A: iteration
        """
        num_freq = [0] * 1000

        for num in target:
            num_freq[num - 1] += 1

        for num in arr:
            if num_freq[num - 1] == 0:
                return False

            num_freq[num - 1] -= 1

        return True


print(Solution().canBeEqual([1, 2, 3, 4], [2, 4, 1, 3]) == True)
print(Solution().canBeEqual([7], [7]) == True)
print(Solution().canBeEqual([3, 7, 9], [3, 7, 11]) == False)
print(Solution().canBeEqual([1, 1, 1, 1, 1], [1, 1, 1, 1, 1]) == True)
