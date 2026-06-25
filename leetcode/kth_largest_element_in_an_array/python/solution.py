import heapq


class Solution:
    def findKthLargest(self, nums: list[int], k: int) -> int:
        """
        Time complexity: O(nlogk)
        Auxiliary space complexity: O(k)
        Tags:
            DS: heap
            A: iteration
        """
        num_heap = []

        for num in nums:
            if len(num_heap) < k:
                heapq.heappush(num_heap, num)
            else:
                heapq.heappushpop(num_heap, num)
        
        return num_heap[0]


class Solution:
    def findKthLargest(self, nums: list[int], k: int) -> int:
        """
        Time complexity: O(nlogk)
        Auxiliary space complexity: O(1)
        Tags:
            DS: heap
            A: iteration, in-place method
        """
        heapq.heapify(nums)

        while len(nums) > k:
            heapq.heappop(nums)
        
        return nums[0]


class Solution:
    def findKthLargest(self, nums: list[int], k: int) -> int:
        """
        Time complexity: O(nlogk)
        Auxiliary space complexity: O(k)
        Tags:
            DS: heap
            A: build-in function
        """
        return heapq.nlargest(k, nums)[-1]


print(Solution().findKthLargest([3, 2, 1, 5, 6, 4], 2) == 5)
print(Solution().findKthLargest([3, 2, 3, 1, 2, 4, 5, 5, 6], 4) == 4)
