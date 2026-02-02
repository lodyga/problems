class Solution:
    def findOrder(self, course_count: int, prerequisites: list[list[int]]) -> list[int]:
        """
        Time complexity: O(V + E)
            V: unique course count
        Auxiliary space complexity: O(V + E)
        Tags:
            DS: array
            A: multi-source DFS, topological sort with cycle detection
            Model: graph
        """
        prereqs = {course: set() for course in range(course_count)}

        for course, prereq in prerequisites:
            prereqs[course].add(prereq)

        order = []
        # -1: not visited, 0: visited, 1: on path (cycle detection)
        visited = [-1] * course_count

        def dfs(course):
            if visited[course] != -1:
                return visited[course]

            visited[course] = 1

            for prereq in prereqs[course]:
                if dfs(prereq):
                    return True

            visited[course] = 0
            order.append(course)

            return False

        for course in prereqs:
            if dfs(course):
                return []

        return order


print(Solution().findOrder(2, [[1, 0]]) == [0, 1])
print(Solution().findOrder(4, [[1, 0], [2, 0], [3, 1], [3, 2]]) == [0, 1, 2, 3])
print(Solution().findOrder(1, []) == [0])
print(Solution().findOrder(2, [[0, 1], [1, 0]]) == [])
