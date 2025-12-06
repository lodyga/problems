from collections import Counter
import heapq


class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        """
        Time complexity: O(nlogk)
        Auxiliary space complexity: O(n)
        Tags: 
            DS: heap, hash map
            A: iteration
        """
        num_frequency = {}
        for num in nums:
            num_frequency[num] = num_frequency.get(num, 0) + 1

        num_heap = []
        for num, frequency in num_frequency.items():
            if len(num_heap) == k:
                heapq.heappushpop(num_heap, (frequency, num))
            else:
                heapq.heappush(num_heap, (frequency, num))

        return [num for _, num in num_heap]


class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(n)
        Tags: 
            DS: bucket as list, hash map
            A: iteration
        """
        num_frequency = {}
        for num in nums:
            num_frequency[num] = num_frequency.get(num, 0) + 1

        num_bucekt = [set() for _ in range(max(num_frequency.values()) + 1)]
        for num, frequency in num_frequency.items():
            num_bucekt[frequency].add(num)

        result = set()
        for num_set in reversed(num_bucekt):
            if len(num_set) == 0:
                continue
            for num in num_set:
                result.add(num)
                if len(result) == k:
                    return list(result)


class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        """
        Time complexity: O(nlogn)
        Auxiliary space complexity: O(n)
        Tags: 
            DS: bucket as hash map
            A: iteration, sorting
        """
        num_frequency = {}
        for number in nums:
            num_frequency[number] = num_frequency.get(number, 0) + 1

        bucket = {}
        for num, frequency in num_frequency.items():
            if frequency not in bucket:
                bucket[frequency] = set()
            bucket[frequency].add(num)

        keys = sorted(bucket.keys(), reverse=True)
        result = []
        for key in keys:
            for num in bucket[key]:
                result.append(num)
                if len(result) == k:
                    return result


class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        """
        Time complexity: O(nlogk)
        Auxiliary space complexity: O(n)
        Tags:
            DS: build-in function
            A: iteration
        """
        return [key for key, _ in Counter(nums).most_common(k)]


print(sorted(Solution().topKFrequent([1, 1, 1, 2, 2, 3], 2)) == sorted([1, 2]))
print(sorted(Solution().topKFrequent([1], 1)) == sorted([1]))
print(sorted(Solution().topKFrequent([1, 2, 1, 2, 1, 2, 3, 1, 3, 2], 2)) == sorted([1, 2]))
print(sorted(Solution().topKFrequent([5, 1, -1, -8, -7, 8, -5, 0, 1, 10, 8, 0, -4, 3, -1, -1, 4, -5, 4, -3, 0, 2, 2, 2, 4, -2, -4, 8, -7, -7, 2, -8, 0, -8, 10, 8, -8, -2, -9, 4, -7, 6, 6, -1, 4, 2, 8, -3, 5, -9, -3, 6, -8, -5, 5, 10, 2, -5, -1, -5, 1, -3, 7, 0, 8, -2, -3, -1, -5, 4, 7, -9, 0, 2, 10, 4, 4, -4, -1, -1, 6, -8, -9, -1, 9, -9, 3, 5, 1, 6, -1, -2, 4, 2, 4, -6, 4, 4, 5, -5], 7)) == sorted([4, -1, 2, -5, 0, 8, -8]))
