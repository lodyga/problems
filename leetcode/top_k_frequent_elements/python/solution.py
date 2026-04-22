class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        """
        Time complexity: O(nlogk)
        Auxiliary space complexity: O(n)
        Tags:
            DS: heap, hash map
            A: iteration
        """
        import heapq
        num_freq = {}
        num_heap = []

        for num in nums:
            num_freq[num] = num_freq.get(num, 0) + 1

        for num, freq in num_freq.items():
            if len(num_heap) == k:
                heapq.heappushpop(num_heap, (freq, num))
            else:
                heapq.heappush(num_heap, (freq, num))

        return [num for _, num in num_heap]


class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(n)
        Tags:
            DS: hash map, list
            A: sorting, bucket sort
        """
        num_freq = {}
        res = []
        
        for num in nums:
            num_freq[num] = num_freq.get(num, 0) + 1

        bucekt = [[] for _ in range(max(num_freq.values()))]
        
        for num, freq in num_freq.items():
            bucekt[freq - 1].append(num)

        for nums in reversed(bucekt):
            if nums:
                for num in nums:
                    res.append(num)
                
                    if len(res) == k:
                        return res


class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        """
        Time complexity: O(nlogn)
        Auxiliary space complexity: O(n)
        Tags:
            DS: hash map, list
            A: sorting, bucket sort
        """
        num_freq = {}
        bucket = {}
        res = []
        
        for num in nums:
            num_freq[num] = num_freq.get(num, 0) + 1

        for num, freq in num_freq.items():
            if freq not in bucket:
                bucket[freq] = []
            
            bucket[freq].append(num)

        freqs = sorted(bucket.keys(), reverse=True)
        
        for freq in freqs:
            for num in bucket[freq]:
                res.append(num)
                
                if len(res) == k:
                    return res


class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        """
        Time complexity: O(nlogk)
        Auxiliary space complexity: O(n)
        Tags:
            DS: build-in function
            A: iteration
        """
        from collections import Counter
        return [key for key, _ in Counter(nums).most_common(k)]


print(sorted(Solution().topKFrequent([1, 1, 1, 2, 2, 3], 2)) == sorted([1, 2]))
print(sorted(Solution().topKFrequent([1], 1)) == sorted([1]))
print(sorted(Solution().topKFrequent([1, 2, 1, 2, 1, 2, 3, 1, 3, 2], 2)) == sorted([1, 2]))
print(sorted(Solution().topKFrequent([5, 1, -1, -8, -7, 8, -5, 0, 1, 10, 8, 0, -4, 3, -1, -1, 4, -5, 4, -3, 0, 2, 2, 2, 4, -2, -4, 8, -7, -7, 2, -8, 0, -8, 10, 8, -8, -2, -9, 4, -7, 6, 6, -1, 4, 2, 8, -3, 5, -9, -3, 6, -8, -5, 5, 10, 2, -5, -1, -5, 1, -3, 7, 0, 8, -2, -3, -1, -5, 4, 7, -9, 0, 2, 10, 4, 4, -4, -1, -1, 6, -8, -9, -1, 9, -9, 3, 5, 1, 6, -1, -2, 4, 2, 4, -6, 4, 4, 5, -5], 7)) == sorted([4, -1, 2, -5, 0, 8, -8]))
