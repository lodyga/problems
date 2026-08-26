import heapq


class Solution:
    def firstMissingPositive(self, nums: list[int]) -> int:
        """
        Time complexity: O(nlogn)
        Auxiliary space complexity: O(n)
        Tags:
            DS: heap
        """
        heapq.heapify(nums)
        res = 1

        while nums:
            num = heapq.heappop(nums)

            if num < res:
                continue

            elif num == res:
                res += 1

            else:
                return res

        return res


class Solution:
    def firstMissingPositive(self, nums: list[int]) -> int:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(1)
        Tags:
            A: iteration, negative marking
        """
        N = len(nums)

        for idx, num in enumerate(nums):
            if num <= 0:
                nums[idx] = N + 1

        for idx, num in enumerate(nums):
            num = abs(num)

            if num <= N:
                nums[num - 1] = -abs(nums[num - 1])

        for idx, num in enumerate(nums):
            if num > 0:
                return idx + 1

        return N + 1


print(Solution().firstMissingPositive([1, 2, 0]) == 3)
print(Solution().firstMissingPositive([3, 4, -1, 1]) == 2)
print(Solution().firstMissingPositive([7, 8, 9, 11, 12]) == 1)
print(Solution().firstMissingPositive([0, 2, 2, 1, 1]) == 3)
