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
        task_freq = [0] * 26
        task_heap = []
        idle_tasks = deque()
        timestamp = 0

        for task in tasks:
            idx = ord(task) - ord("A")
            task_freq[idx] += 1

        for freq in task_freq:
            if freq:
                heapq.heappush(task_heap, -freq)

        while task_heap or idle_tasks:
            if idle_tasks and idle_tasks[0][0] <= timestamp:
                _, task = idle_tasks.popleft()
                heapq.heappush(task_heap, task)

            if task_heap:
                task = heapq.heappop(task_heap) + 1

                if task:
                    idle_tasks.append((timestamp + cooldown + 1, task))

            timestamp += 1

        return timestamp


print(Solution().leastInterval(["A", "A", "A", "B", "B", "B"], 2) == 8)
print(Solution().leastInterval(["A", "C", "A", "B", "D", "B"], 1) == 6)
print(Solution().leastInterval(["A", "A", "A", "B", "B", "B"], 3) == 10)
print(Solution().leastInterval(["B", "C", "D", "A", "A", "A", "A", "G"], 1) == 8)
