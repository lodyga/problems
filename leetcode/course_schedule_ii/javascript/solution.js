class Solution {
   /**
    * Time complexity: O(V + E)
    *     V: unique course count
    * Auxiliary space complexity: O(V + E)
    * Tags:
    *     DS: array
    *     A: multi-source DFS, topological sort with cycle detection
    *     Model: graph
    * @param {number} courseCount
    * @param {number[][]} prerequisites
    * @return {number[][]}
    */
   findOrder(courseCount, prerequisites) {
      const dfs = (course) => {
         if (visited[course] !== -1) {
            return visited[course];
         }

         visited[course] = 1;

         for (const prevCourse of prevCourses[course])
            if (dfs(prevCourse)) {
               return true;
            }

         visited[course] = 0;
         res.push(course);

         return false;
      };

      const prevCourses = Array.from({ length: courseCount }, () => []);
      const res = [];
      // -1: not visited, 0: visited, 1: on path (cycle detection)
      const visited = Array(courseCount).fill(-1);

      for (const [course, prevCourse] of prerequisites) {
         prevCourses[course].push(prevCourse);
      }

      for (let course of prevCourses.keys()) {
         if (dfs(course)) {
            return [];
         }
      }

      return res;
   }
}


const findOrder = new Solution().findOrder;
console.log(new Solution().findOrder(2, [[1, 0]]).toString() === [0, 1].toString())
console.log(new Solution().findOrder(4, [[1, 0], [2, 0], [3, 1], [3, 2]]).toString() === [0, 1, 2, 3].toString())
console.log(new Solution().findOrder(1, []).toString() === [0].toString())
console.log(new Solution().findOrder(2, [[0, 1], [1, 0]]).toString() === [].toString())
