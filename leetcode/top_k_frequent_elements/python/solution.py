import heapq

class Solution:
    def topKFrequent(self, numbers: list[int], k: int) -> list[int]:
        """
        Time complexity: O(nlogk)
        Auxiliary space complexity: O(n+k)
        Tags: heap
        """
        number_frequency = {}
        frequency_number = []

        for number in numbers:
            number_frequency[number] = number_frequency.get(number, 0) + 1
        
        for number, frequency in number_frequency.items():
            if len(frequency_number) < k:
                heapq.heappush(frequency_number, (frequency, number))
            else:
                heapq.heappushpop(frequency_number, (frequency, number))
        
        return [number for _, number in frequency_number]


class Solution:
    def topKFrequent(self, numbers, solution_len):
        """
        Time complexity: O(nlogn)
        Auxiliary space complexity: O(n)
        Tags: bucket as hash map
        It's actually faster to use dict and sort its keys than to traverse through list.
        """
        solution = []
        number_frequency = {}
        bucket = {}  # frequenty to number map

        # number_frequency values
        for number in numbers:
            number_frequency[number] = number_frequency.get(number, 0) + 1

        # reverse number_frequency {key: val} pairs as bucket
        for key, val in number_frequency.items():
            if not val in bucket:
                bucket[val] = []
            bucket[val].append(key)

        # sort frequencies descending
        keys = sorted(bucket.keys(), reverse=True)

        # get top solution_len values
        for key in keys:
            for number in bucket[key]:
                solution.append(number)
                if len(solution) == solution_len:
                    return solution

        return -1


class Solution:
    def topKFrequent(self, numbers, solution_len):
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(n)
        Tags: bucket as list
        """
        solution = []
        counts = {}
        bucket = [[] for _ in range(len(numbers) + 1)]
        
        # counts values
        for number in numbers:
            counts[number] = counts.get(number, 0) + 1

        # bucket as a list of lists
        # [[], [3], [2], [1], [], [], []]
        for key, val in counts.items():
            bucket[val].append(key)
        
        # get top solution_len values
        for numbers in reversed(bucket):
            for number in numbers:
                solution.append(number)
                if len(solution) == solution_len:
                    return solution

        return -1


from collections import Counter

class Solution:
    def topKFrequent(self, numbers: list[int], k: int) -> list[int]:
        """
        Time complexity: O(nlogk)
        Auxiliary space complexity: O(n+k)
        Tags: build-in function
        """
        return [key for key, _ in Counter(numbers).most_common(k)]


print(sorted(Solution().topKFrequent([1, 1, 1, 2, 2, 3], 2)) == sorted([1, 2]))
print(sorted(Solution().topKFrequent([1], 1)) == sorted([1]))
print(sorted(Solution().topKFrequent([5, 1, -1, -8, -7, 8, -5, 0, 1, 10, 8, 0, -4, 3, -1, -1, 4, -5, 4, -3, 0, 2, 2, 2, 4, -2, -4, 8, -7, -7, 2, -8, 0, -8, 10, 8, -8, -2, -9, 4, -7, 6, 6, -1, 4, 2, 8, -3, 5, -9, -3, 6, -8, -5, 5, 10, 2, -5, -1, -5, 1, -3, 7, 0, 8, -2, -3, -1, -5, 4, 7, -9, 0, 2, 10, 4, 4, -4, -1, -1, 6, -8, -9, -1, 9, -9, 3, 5, 1, 6, -1, -2, 4, 2, 4, -6, 4, 4, 5, -5], 7)) == sorted([4, -1, 2, -5, 0, 8, -8]))