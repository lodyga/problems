class Solution:
    def minDifference(self, nums: list[int]) -> int:
        """
        Time complexity: O(nlogn)
        Auxiliary space complexity: O(n)
        Tags:
            A: sorting, brute force
        """
        if len(nums) <= 4:
            return 0

        nums.sort()

        return min(
            nums[-4] - nums[0],
            nums[-3] - nums[1],
            nums[-2] - nums[2],
            nums[-1] - nums[3]
        )


class Solution:
    def minDifference(self, nums: list[int]) -> int:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(n)
        Tags:
            DS: heap
        """
        import heapq
        if len(nums) <= 4:
            return 0

        min_heap = []
        max_heap = []

        for num in nums:
            heapq.heappush(min_heap, num)
            heapq.heappush(max_heap, -num)
        
        min_nums = []
        max_nums = []
        
        for _ in range(4):
            min_nums.append(heapq.heappop(min_heap))
            max_nums.append(-heapq.heappop(max_heap))

        max_nums.reverse()
        return min(max_nums[i] - min_nums[i] for i in range(4))


class Solution:
    def minDifference(self, nums: list[int]) -> int:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(1)
        Tags:
            DS: heap
        """
        import heapq
        if len(nums) <= 4:
            return 0

        min_heap = []
        max_heap = []

        for index, num in enumerate(nums):
            if index < 4:
                heapq.heappush(min_heap, -num)
                heapq.heappush(max_heap, num)
            else:
                heapq.heappushpop(min_heap, -num)
                heapq.heappushpop(max_heap, num)
        
        min_nums = sorted(-num for num in min_heap)
        max_nums = sorted(max_heap)
        return min(max_nums[i] - min_nums[i] for i in range(4))


class Solution:
    def minDifference(self, nums: list[int]) -> int:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(1)
        Tags:
            DS: heap
        """
        import heapq
        if len(nums) <= 4:
            return 0

        min_nums = sorted(heapq.nsmallest(4, nums))
        max_nums = sorted(heapq.nlargest(4, nums))
        return min(max_nums[i] - min_nums[i] for i in range(4))


print(Solution().minDifference([5, 3, 2, 4]) == 0)
print(Solution().minDifference([3, 100, 20]) == 0)
print(Solution().minDifference([1, 5, 0, 10, 14]) == 1)
print(Solution().minDifference([90, 35, 67, 53, 61]) == 6)
print(Solution().minDifference([6, 6, 0, 1, 1, 4, 6]) == 2)
