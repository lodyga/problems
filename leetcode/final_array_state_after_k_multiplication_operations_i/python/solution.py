class Solution:
    def getFinalState(self, nums: list[int], k: int, multiplier: int) -> list[int]:
        import heapq
        """
        Time complexity: O(n + klogn)
        Auxiliary space complexity: O(n)
        Tags:
            DS: heap
            A: iteration
        """
        nums_copy = nums.copy()
        num_heap = [(num, index) for index, num in enumerate(nums)]
        heapq.heapify(num_heap)

        for _ in range(k):
            _, index = heapq.heappop(num_heap)
            nums_copy[index] *= multiplier
            heapq.heappush(num_heap, (nums_copy[index], index))
        
        return nums_copy


print(Solution().getFinalState([2, 1, 3, 5, 6], 5, 2) == [8, 4, 6, 5, 6])
print(Solution().getFinalState([1, 2], 3, 4) == [16, 8])
