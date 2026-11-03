class Solution:
    def findOrder(
            self,
            course_count: int,
            prerequisites: list[list[int]]) -> list[int]:
        """
        Time complexity: O(V + E)
            V: unique course count
        Auxiliary space complexity: O(V + E)
        Tags:
            DS: array
            A: multi-source DFS, topological sort with cycle detection
            Model: graph
        """
        def dfs(course: int) -> int:
            """ If cycle is detected return True. """
            if visited[course] != -1:
                return visited[course]

            visited[course] = 1

            for prev_course in prev_courses[course]:
                if dfs(prev_course):
                    return 1

            res.append(course)
            visited[course] = 0

            return 0

        prev_courses = [[] for _ in range(course_count)]
        # -1: not visited, 0: visited, 1: on path (cycle detection)
        visited = [-1] * course_count
        res = []

        for course, prev_course in prerequisites:
            prev_courses[course].append(prev_course)

        for course in range(course_count):
            if dfs(course):
                return []

        return res


print(Solution().findOrder(2, [[1, 0]]) == [0, 1])
print(Solution().findOrder(4, [[1, 0], [2, 0], [3, 1], [3, 2]]) == [0, 1, 2, 3])
print(Solution().findOrder(1, []) == [0])
print(Solution().findOrder(2, [[0, 1], [1, 0]]) == [])
