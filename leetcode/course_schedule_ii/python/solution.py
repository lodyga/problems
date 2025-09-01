class Solution:
    def findOrder(self, course_count: int, prerequisites: list[list[int]]) -> list[int]:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(n)
        Tags: dfs, recursion, graph, topological sort
        """
        prereqs = {course: set() for course in range(course_count)}
        for course, preq_course in prerequisites:
            prereqs[course].add(preq_course)
        
        course_order = []
        # calculate order for each course only once
        visited = [False] * course_count
        # build the path for cycle detection
        path = [False] * course_count

        def dfs(course):
            # detect cycle
            if path[course]:
                return False
            # if already visited
            elif visited[course]:
                return True
            
            path[course] = True

            for preq_course in prereqs[course]:
                if dfs(preq_course) == False:
                    return False
            
            path[course] = False
            visited[course] = True
            course_order.append(course)
            return True

        for course in prereqs:
            if dfs(course) == False:
                return []
        
        return course_order


print(Solution().findOrder(2, [[1, 0]]) == [0, 1])
print(Solution().findOrder(4, [[1, 0], [2, 0], [3, 1], [3, 2]]) == [0, 1, 2, 3])
print(Solution().findOrder(1, []) == [0])
print(Solution().findOrder(2, [[0, 1], [1, 0]]) == [])