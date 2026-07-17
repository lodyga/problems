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
        N = len(tasks)
        data = [[task[0], task[1], idx] for idx, task in enumerate(tasks)]
        data.sort()
        timestamp = data[0][0]
        task_heap = []
        idx = 0
        res = []

        while idx < N or task_heap:
            while idx < N and data[idx][0] <= timestamp:
                _, processing_time, id = data[idx]
                heapq.heappush(task_heap, (processing_time, id))
                idx += 1

            if task_heap:
                processing_time, id = heapq.heappop(task_heap)
                timestamp += processing_time
                res.append(id)
            else:
                # time fast forward
                timestamp = data[idx][0]

        return res


print(Solution().getOrder([[1, 2], [2, 4], [3, 2], [4, 1]]) == [0, 2, 3, 1])
print(Solution().getOrder([[7, 10], [7, 12], [7, 5], [7, 4], [7, 2]]) == [4, 3, 2, 0, 1])
print(Solution().getOrder([[1000000000, 1000000000]]) == [0])
print(Solution().getOrder([[19, 13], [16, 9], [21, 10], [32, 25], [37, 4], [49, 24], [2, 15], [38, 41], [37, 34], [33, 6], [45, 4], [18, 18], [46, 39], [12, 24]]) == [6, 1, 2, 9, 4, 10, 0, 11, 5, 13, 3, 8, 12, 7])

