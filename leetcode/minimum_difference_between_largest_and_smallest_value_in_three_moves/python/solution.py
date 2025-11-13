import heapq


class Solution:
    def minDifference(self, numbers: list[int]) -> int:
        """
        Time complexity: O(nlogn)
        Auxiliary space complexity: O(n)
        Tags: sorting
        """
        if len(numbers) <= 4:
            return 0

        numbers.sort()

        return min(
            numbers[-4] - numbers[0],
            numbers[-3] - numbers[1],
            numbers[-2] - numbers[2],
            numbers[-1] - numbers[3]
        )


class Solution2:
    def minDifference(self, numbers: list[int]) -> int:
        """
        Time complexity: O(1)
            O(10**5)
        Auxiliary space complexity: O(1)
        Tags: bucket sort
        mle
        """
        if len(numbers) <= 4:
            return 0

        bucket = [0] * (max(numbers) + 1)
        for number in numbers:
            bucket[number] += 1

        left = []
        index = 0
        counter = 0
        while True:
            if bucket[index]:
                for _ in range(bucket[index]):
                    left.append(index)
                counter += bucket[index]
                if counter >= 4:
                    break
            index += 1

        right = []
        index = len(bucket) - 1
        counter = 0
        while True:
            if bucket[index]:
                for _ in range(bucket[index]):
                    right.append(index)
                counter += bucket[index]
                if counter >= 4:
                    break
            index -= 1
        right = right[::-1]

        return min(r - l for l, r in zip(left, right))


class Solution:
    def minDifference(self, numbers: list[int]) -> int:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(1)
        Tags: heap
        """
        if len(numbers) <= 4:
            return 0

        min_heap = []
        max_heap = []

        for number in numbers:
            if len(max_heap) < 4:
                heapq.heappush(max_heap, number)
            else:
                heapq.heappushpop(max_heap, number)

            if len(min_heap) < 4:
                heapq.heappush(min_heap, -number)
            else:
                heapq.heappushpop(min_heap, -number)

        max_numbers = []
        for _ in range(4):
            max_numbers.append(heapq.heappop(max_heap))
        min_numbers = []
        for _ in range(4):
            min_numbers.append(-heapq.heappop(min_heap))
        min_numbers.reverse()

        return min(r - l for l, r in zip(min_numbers, max_numbers))


class Solution:
    def minDifference(self, numbers: list[int]) -> int:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(1)
        Tags: heap
        """
        if len(numbers) <= 4:
            return 0

        min_numbers = sorted(heapq.nsmallest(4, numbers))
        max_numbers = sorted(heapq.nlargest(4, numbers))
        return min(r - l for l, r in zip(min_numbers, max_numbers))


print(Solution().minDifference([5, 3, 2, 4]) == 0)
print(Solution().minDifference([3, 100, 20]) == 0)
print(Solution().minDifference([1, 5, 0, 10, 14]) == 1)
print(Solution().minDifference([90, 35, 67, 53, 61]) == 6)
print(Solution().minDifference([6, 6, 0, 1, 1, 4, 6]) == 2)
