class Solution:
    def minOperations(self, grid: list[list[int]], x: int) -> int:
        """
        Time complexity: O((nm)logn(nm))
            n, m: grid size
        Auxiliary space complexity: O(nm)
        Tags:
            DS: array
            A: sorting
        """
        nums = [cell for row in grid for cell in row]
        mod = nums[0] % x
        
        for num in nums:
            if num % x != mod:
                return -1
            
        nums.sort()
        median = nums[len(nums) // 2]

        return sum(abs(num - median) // x 
                   for num in nums)


class Solution:
    def minOperations(self, grid: list[list[int]], x: int) -> int:
        """
        Time complexity: O(n4)
        Auxiliary space complexity: O(n)
        Tags:
        """
        ROWS = len(grid)
        COLS = len(grid[0])
        if ROWS == COLS == 1:
            return 0

        left = min(min(row) for row in grid)
        right = max(max(row) for row in grid)
        middle = int(sum(sum(row) for row in grid) // (ROWS * COLS))
        mod = sum((value - left) % x for row in grid for value in row)

        if mod != 0:
            return -1

        def min_operations(direction):
            min_counter = 10**9
            index = 0
            current_middle = middle
            while left <= current_middle <= right:
                is_break = False
                counter = 0
                current_middle = middle + index
                for row in range(ROWS):
                    if is_break:
                        break
                    for col in range(COLS):
                        cell = grid[row][col]
                        if abs(cell - current_middle) % x:
                            is_break = True
                            break
                        counter += abs(cell - current_middle) // x

                if is_break is False:
                    if counter < min_counter:
                        min_counter = counter
                    else:
                        break

                index += 1 * direction

            return min_counter

        res = min(min_operations(1), min_operations(-1))
        return res if res != 10**9 else -1


print(Solution().minOperations([[2, 4], [6, 8]], 2) == 4)
print(Solution().minOperations([[1, 5], [2, 3]], 1) == 5)
print(Solution().minOperations([[1, 2], [3, 4]], 2) == -1)
print(Solution().minOperations([[146]], 86) == 0)
print(Solution().minOperations([[931, 128], [639, 712]], 73) == 12)
print(Solution().minOperations([[1,1,10000]], 1) == 9999)
print(Solution().minOperations([[503, 503, 9852, 9852, 9852, 9852, 9852, 503, 9852, 503], [9852, 9852, 9852, 9852, 503, 9852, 9852, 9852, 503, 503], [503, 503, 9852, 9852, 9852, 9852, 9852, 503, 9852, 9852], [9852, 9852, 503, 9852, 503, 9852, 503, 503, 9852, 503], [503, 503, 503, 503, 9852, 9852, 503, 503, 503, 503], [9852, 503, 9852, 9852, 9852, 9852, 503, 9852, 9852, 503], [503, 503, 9852, 9852, 503, 503, 9852, 503, 9852, 9852], [503, 9852, 503, 9852, 503, 503, 503, 503, 503, 503], [503, 503, 9852, 9852, 9852, 503, 503, 503, 9852, 9852], [9852, 9852, 9852, 9852, 503, 503, 503, 503, 503, 9852]], 9349) == 49)


class Solution:
    def minOperations(self, grid: list[list[int]], x: int) -> int:
        import heapq
        """
        Failed
        Time complexity: O(dn2logn2)
            n, m: grid size
            d: max distance between cell number and median
        Auxiliary space complexity: O(n)
        Tags:
            DS: heap, hash map
            A: sorting
        """
        ROWS = len(grid)
        COLS = len(grid[0])
        num_freq = {}

        if ROWS == COLS == 1:
            return 0

        for row in grid:
            for cell in row:
                num_freq[cell] = num_freq.get(cell, 0) + 1


        nums = sorted(num for row in grid for num in row)
        middle = (ROWS * COLS) // 2
        median = (nums[middle - 1] + nums[middle]) / 2
        min_heap = []
        max_heap = []
        counter = 0

        for num, freq in num_freq.items():
            if num <= median:
                heapq.heappush(min_heap, (num, freq))
            else:
                heapq.heappush(max_heap, (-num, freq))

        while True:
            if min_heap[0][0] == -max_heap[0][0]:
                break
            elif -max_heap[0][0] - min_heap[0][0] < x:
                return -1

            if (median - min_heap[0][0]) >= (-max_heap[0][0] - median):
                num, freq = heapq.heappop(min_heap)
                heapq.heappush(min_heap, (num + x, freq))
            else:
                num, freq = heapq.heappop(max_heap)
                heapq.heappush(max_heap, (num + x, freq))

            counter += freq

        return counter

#
# 2, 4, 6, 8
# 8, 6, 4, 2
# 5
# 4, 4
# 4, 4

# 0, 2, 4, 6
# 6, 4, 2, 0
# avg = 3
# 2, 2
# 4, 4
