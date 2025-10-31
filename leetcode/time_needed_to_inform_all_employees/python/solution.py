class Solution:
    def numOfMinutes(self, n: int, head_id: int, manager_list: list[int], direct_inform_time: list[int]) -> int:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(n)
        Tags: dfs, recursion, graph
        """
        adjs = {index: set() for index in range(n)}  # {manager: set(employee, ...), ...}
        for employee, manager in enumerate(manager_list):
            if manager == -1:
                continue
            adjs[manager].add(employee)
        
        def dfs(manager):
            if manager in indirect_inform_time:
                return indirect_inform_time[manager]

            inform_time = 0
            for employee in adjs[manager]:
                inform_time = max(inform_time, 
                                  dfs(employee) + direct_inform_time[manager])
            
            indirect_inform_time[manager] = inform_time
            return inform_time

        indirect_inform_time = {employee: 0 for employee in adjs if not adjs[employee]}
        for employee in range(n):
            dfs(employee)

        return indirect_inform_time[head_id]


from collections import deque


class Solution:
    def numOfMinutes(self, n: int, head_id: int, manager_list: list[int], direct_inform_time: list[int]) -> int:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(n)
        Tags: bfs, iteration, queue, graph
        """
        adjs = {index: set() for index in range(n)}  # {manager: set(employee, ...), ...}
        for employee, manager in enumerate(manager_list):
            if manager == -1:
                continue
            adjs[manager].add(employee)
        
        def bfs(manager):
            total_time = 0
            queue = deque([(manager, 0)])  # queue((employee id, time), ...)

            while queue:
                manager, time = queue.popleft()
                total_time = max(total_time, time)

                for employee in adjs[manager]:
                    queue.append((employee, time + direct_inform_time[manager]))
            
            return total_time
        
        return bfs(head_id)


print(Solution().numOfMinutes(1, 0, [-1], [0]) == 0)
print(Solution().numOfMinutes(6, 2, [2, 2, -1, 2, 2, 2], [0, 0, 1, 0, 0, 0]) == 1)