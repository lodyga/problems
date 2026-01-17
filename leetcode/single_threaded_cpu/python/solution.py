import heapq


class Solution:
    def getOrder(self, tasks: list[list[int]]) -> list[int]:
        """
        Time complexity: O(nlogn)
        Auxiliary space complexity: O(n)
        Tags:
            DS: heap
            A: sorting
        """
        data = [(enq_time, duration, id) for
                id, (enq_time, duration) in enumerate(tasks)]
        data.sort()
        index = 0
        time = data[0][0]
        task_heap = []
        task_order = []

        while index < len(data) or task_heap:
            while index < len(data) and data[index][0] <= time:
                _, duration, id = data[index]
                heapq.heappush(task_heap, (duration, id))
                index += 1

            if task_heap:
                duration, id = heapq.heappop(task_heap)
                time += duration
                task_order.append(id)
            else:
                # time fast forward
                time = data[index][0]

        return task_order


print(Solution().getOrder([[1, 2], [2, 4], [3, 2], [4, 1]]) == [0, 2, 3, 1])
print(Solution().getOrder([[7, 10], [7, 12], [7, 5], [7, 4], [7, 2]]) == [4, 3, 2, 0, 1])
print(Solution().getOrder([[1000000000, 1000000000]]) == [0])
print(Solution().getOrder([[19, 13], [16, 9], [21, 10], [32, 25], [37, 4], [49, 24], [2, 15], [38, 41], [37, 34], [33, 6], [45, 4], [18, 18], [46, 39], [12, 24]]) == [6, 1, 2, 9, 4, 10, 0, 11, 5, 13, 3, 8, 12, 7])
