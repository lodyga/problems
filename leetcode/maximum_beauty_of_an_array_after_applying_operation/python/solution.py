import heapq


class Solution:
    def maximumBeauty(self, numbers: list[int], k: int) -> int:
        """
        Time complexity: O(n*k)
        Auxiliary space complexity: O(n*k)
        Tags: greedy
        """
        beauty_frequency = {}
        for number in numbers:
            for beauty_number in range(number - k, number + k + 1):
                beauty_frequency[beauty_number] = beauty_frequency.get(
                    beauty_number, 0) + 1
        return max(beauty_frequency.values())


class Solution:
    def maximumBeauty(self, numbers: list[int], k: int) -> int:
        """
        Time complexity: O(nlogn)
        Auxiliary space complexity: O(k)
        Tags: heap
        """
        interval_heap = []
        end_heap = []
        counter = 0
        max_counter = 0
        for number in numbers:
            heapq.heappush(interval_heap, (number - k, number + k))

        while interval_heap:
            start, end = heapq.heappop(interval_heap)
            heapq.heappush(end_heap, end)

            while end_heap and end_heap[0] < start:
                heapq.heappop(end_heap)
                counter -= 1

            counter += 1
            max_counter = max(max_counter, counter)

        return max_counter


class Solution:
    def maximumBeauty(self, numbers: list[int], k: int) -> int:
        """
        Time complexity: O(nlogn)
        Auxiliary space complexity: O(n)
        Tags: sliding window
        """
        numbers.sort()
        left = 0
        max_beauty = 0

        for right in range(len(numbers)):
            while numbers[right] - numbers[left] > 2 * k:
                left += 1

            length = right - left + 1
            max_beauty = length if length > max_beauty else max_beauty

        return max_beauty


print(Solution().maximumBeauty([4, 6, 1, 2], 2) == 3)
print(Solution().maximumBeauty([1, 1, 1, 1], 10) == 4)
print(Solution().maximumBeauty([48, 93, 96, 19], 24) == 3)
print(Solution().maximumBeauty([75, 15, 9], 28) == 2)
