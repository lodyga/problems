import heapq
from collections import deque


class Solution:
    def leastInterval(self, tasks: list[str], cooldown: int) -> int:
        """
        Time complexity: O(n)
            O(nlogk) -> O(nlog26) -> O(n)
            n: task count
            k: letter count
        Auxiliary space complexity: O(1)
            O(k)
        Tags:
            DS: heap, queue
            A: iteration
        """
        task_heap = []
        task_freaq = {}
        for task in tasks:
            task_freaq[task] = task_freaq.get(task, 0) + 1

        task_queue = deque()
        for freq in task_freaq.values():
            task_queue.append((0, -freq))

        time = 0
        while task_queue or task_heap:
            time += 1

            while task_queue and task_queue[0][0] < time:
                _, freq = task_queue.popleft()
                heapq.heappush(task_heap, freq)

            if not task_heap:
                continue

            freq = heapq.heappop(task_heap) + 1
            if freq:
                task_queue.append((time + cooldown, freq))

        return time


print(Solution().leastInterval(["A", "A", "A", "B", "B", "B"], 2) == 8)
print(Solution().leastInterval(["A", "C", "A", "B", "D", "B"], 1) == 6)
print(Solution().leastInterval(["A", "A", "A", "B", "B", "B"], 3) == 10)
print(Solution().leastInterval(["B", "C", "D", "A", "A", "A", "A", "G"], 1) == 8)
