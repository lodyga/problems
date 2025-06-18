import heapq

class Solution:
    def findKthLargest(self, numbers: list[int], k: int) -> int:
        """
        Time complexity: O(nlogk)
        Auxiliary space complexity: O(k)
        Tags: heap
        """
        number_heap = []
        heapq.heapify(number_heap)

        for number in numbers:
            if len(number_heap) < k:
                heapq.heappush(number_heap, number)
            else:
                heapq.heappushpop(number_heap, number)
        
        return heapq.heappop(number_heap)


class Solution:
    def findKthLargest(self, numbers: list[int], k: int) -> int:
        """
        Time complexity: O(nlogk)
        Auxiliary space complexity: O(n)
        Tags: heap
        """
        return heapq.nlargest(k, numbers)[-1]


print(Solution().findKthLargest([3, 2, 1, 5, 6, 4], 2) == 5)
print(Solution().findKthLargest([3, 2, 3, 1, 2, 4, 5, 5, 6], 4) == 4)


# O(nlogn), O(n)
# quick select, tle
class Solution:
    def findKthLargest(self, numbers: list[int], k: int) -> int:
        k = len(numbers) - k
        
        def quick_select(left, right):
            pivot = numbers[right]
            pivot_index = left

            for index in range(left, right):
                if numbers[index] < pivot:
                    numbers[index], numbers[pivot_index] = numbers[pivot_index], numbers[index]
                    pivot_index += 1
                
            numbers[pivot_index], numbers[right] = numbers[right], numbers[pivot_index]
            
            if k < pivot_index:
                return quick_select(left, pivot_index - 1)
            elif k > pivot_index:
                return quick_select(pivot_index + 1, right)
            else:
                return numbers[pivot_index]
        
        return quick_select(0, len(numbers) - 1)