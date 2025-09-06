import heapq


class Solution:
    def findMaximizedCapital(self, project_count: int, current_capital: int, profits: list[int], capital_list: list[int]) -> int:
        """
        Time complexity: O(nlogn)
        Auxiliary space complexity: O(n)
        Tags: heap
        """
        min_heap = []  # heap((capital, -profit), )
        max_heap = []  # heap(-profit, )

        for capital, profit in zip(capital_list, profits):
            heapq.heappush(min_heap, (capital, -profit))
        
        for _ in range(project_count):
            while min_heap and current_capital >= min_heap[0][0]:
                _, profit = heapq.heappop(min_heap)
                heapq.heappush(max_heap, profit)
            
            if not max_heap:
                break

            current_capital -= heapq.heappop(max_heap)

        return current_capital


print(Solution().findMaximizedCapital(2, 0, [1, 2, 3], [0, 1, 1]) == 4)
print(Solution().findMaximizedCapital(3, 0, [1, 2, 3], [0, 1, 2]) == 6)
print(Solution().findMaximizedCapital(1, 0, [1, 2, 3], [1, 1, 2]) == 0)