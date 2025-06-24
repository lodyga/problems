import heapq
from collections import deque


class Solution:
    def leastInterval(self, tasks: list[str], cooldown: int) -> int:
        """
        Time complexity: O(n)
            O(nlogn) -> log26 => const ->  O(n)
        Auxiliary space complexity: O(1)
            O(26) -> O(1)
        Tags: heap, queue
        """
        task_frequency = {}  # {task: frquency, ...}  O(26)
        for task in tasks:
            task_frequency[task] = task_frequency.get(task, 0) + 1

        # [-frequency1, ...]  O(26)
        task_heap = [-frequency
                     for frequency in task_frequency.values()]
        heapq.heapify(task_heap)

        task_length = 0
        queue = deque()  # deque((cooldown, -frequency), ...) O(26)
        while task_heap or queue:  # O(n)
            while queue and queue[0][0] == task_length:
                _, frequency = queue.popleft()
                heapq.heappush(task_heap, frequency)  # O(26)

            if task_heap:
                frequency = heapq.heappop(task_heap) + 1
                if frequency:
                    queue.append((task_length + cooldown + 1, frequency))

            task_length += 1

        return task_length


print(Solution().leastInterval(["A", "A", "A", "B", "B", "B"], 2) == 8)  # A -> B -> idle -> A -> B -> idle -> A -> B
print(Solution().leastInterval(["A", "C", "A", "B", "D", "B"], 1) == 6)  # A -> B -> C -> D -> A -> B
print(Solution().leastInterval(["A", "A", "A", "B", "B", "B"], 3) == 10)  # A -> B -> idle -> idle -> A -> B -> idle -> idle -> A -> B