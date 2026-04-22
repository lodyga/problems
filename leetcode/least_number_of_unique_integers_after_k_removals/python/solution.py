class Solution:
    def findLeastNumOfUniqueInts(self, nums: list[int], k: int) -> int:
        import heapq
        """
        Time complexity: O(n + klogn)
        Auxiliary space complexity: O(n)
        Tags:
            DS: heap
            A: iteration
        """
        num_freq = {}
        # heap([freq, ...])
        min_freq = []

        for num in nums:
            num_freq[num] = num_freq.get(num, 0) + 1

        for freq in num_freq.values():
            heapq.heappush(min_freq, freq)

        while k > 0:
            freq = heapq.heappop(min_freq)

            if freq > k:
                heapq.heappush(min_freq, freq - k)

            k -= freq

        return len(min_freq)


class Solution:
    def findLeastNumOfUniqueInts(self, nums: list[int], k: int) -> int:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(n)
        Tags:
            DS: bucket sort
            A: iteration
        """
        num_freq = {}
        bucket = [0] * len(nums)
        res = 0

        for num in nums:
            num_freq[num] = num_freq.get(num, 0) + 1

        for freq in num_freq.values():
            bucket[freq - 1] += 1

        for index, freq in enumerate(bucket, 1):
            if k <= 0:
                res += freq
            else:
                k -= freq * index
                
                if k < 0:
                    while k < 0:
                        k += index
                        res += 1
                
                    k = 0

        return res


print(Solution().findLeastNumOfUniqueInts([5, 5, 4], 1) == 1)
print(Solution().findLeastNumOfUniqueInts([4, 3, 1, 1, 3, 3, 2], 3) == 2)
print(Solution().findLeastNumOfUniqueInts([1, 1, 2, 2, 3, 3], 1) == 3)
