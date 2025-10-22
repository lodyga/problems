import heapq


class Solution:
    def getFinalState(self, numbers: list[int], k: int, multiplier: int) -> list[int]:
        """
        Time complexity: O(klogn)
        Auxiliary space complexity: O(n)
        Tags: heap
        """
        number_heap = [(numebr, index) for index, numebr in enumerate(numbers)]
        heapq.heapify(number_heap)

        for _ in range(k):
            _, index = heapq.heappop(number_heap)
            numbers[index] *= multiplier
            heapq.heappush(number_heap, (numbers[index], index))
        return numbers


print(Solution().getFinalState([2, 1, 3, 5, 6], 5, 2) == [8, 4, 6, 5, 6])
print(Solution().getFinalState([1, 2], 3, 4) == [16, 8])