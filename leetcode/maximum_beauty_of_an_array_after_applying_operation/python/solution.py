class Solution:
    def maximumBeauty(self, nums: list[int], k: int) -> int:
        import heapq
        """
        Time complexity: O(nlogn)
        Auxiliary space complexity: O(n)
        Tags:
            DS: heap
            A: sorting
        """
        nums.sort()
        beauty_heap = []
        res = 1

        for num in nums:
            while (beauty_heap and beauty_heap[0] < num - k):
                heapq.heappop(beauty_heap)

            if num + k >= 0:
                heapq.heappush(beauty_heap, num + k)
                res = max(res, len(beauty_heap))

        return res


class Solution:
    def maximumBeauty(self, nums: list[int], k: int) -> int:
        """
        Time complexity: O(nlogn)
        Auxiliary space complexity: O(n)
        Tags:
            A: sliding window
        """
        nums.sort()
        res = 0
        left = 0

        for right in range(len(nums)):
            while nums[right] - nums[left] > k*2:
                left += 1

            res = max(res, right - left + 1)

        return res


class Solution:
    def maximumBeauty(self, nums: list[int], k: int) -> int:
        """
        Time complexity: O(2^n)
        Auxiliary space complexity: O(n)
        Tags:
            A: brute-force
        """
        def dfs(index, beauty_num):
            if index == len(nums):
                return 0

            num = nums[index]
            skip = dfs(index + 1, beauty_num)

            if beauty_num == -1:
                start = 1 + max(
                    dfs(index + 1, num - k),
                    dfs(index + 1, num),
                    dfs(index + 1, num + k),
                )
                return max(skip, start)

            elif (
                beauty_num >= num - k and
                beauty_num <= num + k
            ):
                return 1 + dfs(index + 1, beauty_num)

            return max(0, skip)

        return dfs(0, -1)


print(Solution().maximumBeauty([4, 6, 1, 2], 2) == 3)
print(Solution().maximumBeauty([1, 1, 1, 1], 10) == 4)
print(Solution().maximumBeauty([75, 15, 9], 28) == 2)
print(Solution().maximumBeauty([48, 93, 96, 19], 24) == 3)
