class Solution:
    def firstMissingPositive(self, nums: list[int]) -> int:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(1)
        Tags:
            A: iteration, negative marking
        """
        N = len(nums)

        for index, num in enumerate(nums):
            if num <= 0:
                nums[index] = N + 1

        for index, num in enumerate(nums):
            num = abs(num)
            if num <= N:
                nums[num - 1] = -abs(nums[num - 1])

        for index, num in enumerate(nums):
            if num > 0:
                return index + 1

        return N + 1


class Solution2:
    def firstMissingPositive(self, nums: list[int]) -> int:
        """
        Time complexity: O(nlogn)
        Auxiliary space complexity: O(n)
        Tags:
            DS: heap
        """
        import heapq
        heapq.heapify(nums)
        missing_num = 1

        while nums:
            num = heapq.heappop(nums)
            if num < 1:
                continue

            if num == missing_num:
                missing_num += 1
            else:
                return missing_num

        return missing_num


print(Solution().firstMissingPositive([1, 2, 0]) == 3)
print(Solution().firstMissingPositive([3, 4, -1, 1]) == 2)
print(Solution().firstMissingPositive([7, 8, 9, 11, 12]) == 1)
