class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: list[list[int]], queries: list[list[int]]) -> list[bool]:
        """
        Time complexity: O(q * (V + E))
            q: queries count
        Auxiliary space complexity: O(q + V + E)
        Tags: dfs, tle
        """
        preqs = {course: set() for course in range(numCourses)}
        for preq, course in prerequisites:
            preqs[course].add(preq)

        def dfs(course, searched_preq):
            if not preqs[course]:
                return False
            elif searched_preq in preqs[course]:
                return True

            for preq in preqs[course]:
                if dfs(preq, searched_preq):
                    return True
            
            return False

        querie_response = []
        for preq, course in queries:
            querie_response.append(dfs(course, preq))

        return querie_response


class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: list[list[int]], queries: list[list[int]]) -> list[bool]:
        """
        Time complexity: O(N3 + q)
        Auxiliary space complexity: O(q + V + E)
        Tags: dfs, tle
        """
        direct_preqs = {course: set() for course in range(numCourses)}
        for preq, course in prerequisites:
            direct_preqs[course].add(preq)

        all_preqs = {}  # {course: set(indeirect preqs list)}

        def dfs(course):
            if course not in all_preqs:
                all_preqs[course] = set()

                for preq in direct_preqs[course]:
                    all_preqs[course] |= dfs(preq)
                all_preqs[course].add(course)

            return all_preqs[course]

        
        for course in range(numCourses):
            dfs(course)
        
        querie_response = []
        for preq, course in queries:
            querie_response.append(preq in all_preqs[course])
        return querie_response


print(Solution().checkIfPrerequisite(2, [[1, 0]], [[0, 1], [1, 0]]), [False, True])
print(Solution().checkIfPrerequisite(2, [], [[1, 0], [0, 1]]), [False, False])
print(Solution().checkIfPrerequisite(3, [[1, 2], [1, 0], [2, 0]], [[1, 0], [1, 2]]), [True, True])
print(Solution().checkIfPrerequisite(6, [[0, 1], [1, 2], [2, 4], [3, 2], [5, 3]], [[0, 3], [1, 4], [1, 3], [2, 3], [3, 2], [5, 4]]), [False, True, False, False, True, True])