import heapq


class Solution:
    def getOrder(self, tasks: list[list[int]]) -> list[int]:
        """
        Time complexity: O(nlogn)
        Auxiliary space complexity: O(n)
        Tags: heap
        """
        enqueued_tasks = []  # [enqueue time, processing time]
        for index, (enqueue, processing) in enumerate(tasks):
            heapq.heappush(enqueued_tasks, [enqueue, processing, index])
        
        processing_tasks = []
        timestamp = enqueued_tasks[0][0]
        order = []

        while enqueued_tasks or processing_tasks:
            while enqueued_tasks and enqueued_tasks[0][0] <= timestamp:
                _, processing, index = heapq.heappop(enqueued_tasks)
                heapq.heappush(processing_tasks, [processing, index])
            
            if processing_tasks:
                processing, index = heapq.heappop(processing_tasks)
                order.append(index)
                timestamp += processing
            else:
                # timestamp fast forward
                timestamp = enqueued_tasks[0][0]
            
        return order


print(Solution().getOrder([[1, 2], [2, 4], [3, 2], [4, 1]]) == [0, 2, 3, 1])
print(Solution().getOrder([[7, 10], [7, 12], [7, 5], [7, 4], [7, 2]]) == [4, 3, 2, 0, 1])
print(Solution().getOrder([[1000000000 ,1000000000]]) == [0])