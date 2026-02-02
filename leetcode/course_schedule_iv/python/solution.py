class Solution:
    def checkIfPrerequisite(self, N: int, prerequisites: list[list[int]], queries: list[list[int]]) -> list[bool]:
        """
        Time complexity: O(V*(V + E) + q)
            q: queries len
        Auxiliary space complexity: O(V + E + q)
        Tags:
            DS: array
            A: DFS with memoization (DP on DAG)
            Model: graph
        """
        # Direct prerequisities.
        prereq_courses = [set() for _ in range(N)]
        for prereq_course, course in prerequisites:
            prereq_courses[course].add(prereq_course)

        # Indirect prerequisities.
        # [course index: set(prerequisities)]
        memo = [None for _ in range(N)]

        def dfs(course):
            if memo[course] is not None:
                return memo[course]
            
            memo[course] = set()

            for prereq_course in prereq_courses[course]:
                # Add direct prerequisite.
                memo[course].add(prereq_course)
                # Add all indirect prerequisites.
                memo[course].update(dfs(prereq_course))

            return memo[course]

        # Search for all indirect prerequisities.
        for course in range(N):
            dfs(course)

        # Answer queries.
        return [prereq_course in memo[course] 
                for prereq_course, course in queries]


class Solution:
    def checkIfPrerequisite(self, num_courses: int, prerequisites: list[list[int]], queries: list[list[int]]) -> list[bool]:
        """
        Time complexity: O((V + E) * q)
            q: queries len
        Auxiliary space complexity: O(V + E + q)
        Tags:
            DS: hash map, hash set
            A: DFS
            Model: graph
        """
        prereqs = {course: set() for course in range(num_courses)}
        for prereq, course in prerequisites:
            prereqs[course].add(prereq)

        def dfs(course, target):
            if not prereqs[course]:
                return False
            elif target in prereqs[course]:
                return True

            for prereq in prereqs[course]:
                if dfs(prereq, target):
                    return True
            
            return False

        response = []
        for prereq, course in queries:
            response.append(dfs(course, prereq))

        return response


print(Solution().checkIfPrerequisite(2, [[1, 0]], [[0, 1], [1, 0]]) == [False, True])
print(Solution().checkIfPrerequisite(2, [], [[1, 0], [0, 1]]) == [False, False])
print(Solution().checkIfPrerequisite(3, [[1, 2], [1, 0], [2, 0]], [[1, 0], [1, 2]]) == [True, True])
print(Solution().checkIfPrerequisite(6, [[0, 1], [1, 2], [2, 4], [3, 2], [5, 3]], [[0, 3], [1, 4], [1, 3], [2, 3], [3, 2], [5, 4]]) == [False, True, False, False, True, True])
