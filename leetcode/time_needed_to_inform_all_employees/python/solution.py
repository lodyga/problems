class Solution:
    def numOfMinutes(self, n: int, head_id: int, managers: list[int], direct_inform_time: list[int]) -> int:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(n)
        Tags:
            DS: array
            A: DFS with memoization (DP on DAG)
            Model: graph
        """
        # Total indirect information time.
        memo = [-1] * n
        memo[head_id] = direct_inform_time[head_id]

        def dfs(id):
            if memo[id] != -1:
                return memo[id]

            memo[id] = direct_inform_time[id] + dfs(managers[id])
            return memo[id]

        for id in range(n):
            dfs(id)

        return max(memo)


class Solution:
    def numOfMinutes(self, n: int, head_id: int, managers: list[int], direct_inform_time: list[int]) -> int:
        from collections import deque
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(n)
        Tags:
            DS: array
            A: BFS
            Model: graph
        """
        manager_to_emp = {}
        for emp, manager in enumerate(managers):
            if manager not in manager_to_emp:
                manager_to_emp[manager] = []

            manager_to_emp[manager].append(emp)

        # bfs
        # deque([(employee id, employee inform time)])
        queue = deque([(head_id, direct_inform_time[head_id])])
        res = 0

        while queue:
            manager_id, time = queue.popleft()
            res = max(res, time)

            if manager_id in manager_to_emp:
                for emp_id in manager_to_emp[manager_id]:
                    queue.append((emp_id, time + direct_inform_time[emp_id]))

        return res


print(Solution().numOfMinutes(1, 0, [-1], [0]) == 0)
print(Solution().numOfMinutes(6, 2, [2, 2, -1, 2, 2, 2], [0, 0, 1, 0, 0, 0]) == 1)
