class Solution {
   /**
    * Time complexity: O(V + E)
    *     V: unique course count
    * Auxiliary space complexity: O(V + E)
    * Tags:
    *     DS: array (graph)
    *     A: multi-source DFS, topological sort with cycle detection
    * @param {number} courseCount
    * @param {number[][]} prerequisites
    * @return {number[][]}
    */
   findOrder(courseCount, prerequisites) {
      const prereqs = new Map();
      for (let course = 0; course < courseCount; course++) {
         prereqs.set(course, []);
      }
      for (const [course, prereq] of prerequisites) {
         prereqs.get(course).push(prereq)
      }

      const schedule = [];
      // -1: not visited, 0: visited, 1: on path (cycle detection)
      const visited = Array(courseCount).fill(-1);

      const dfs = (course) => {
         if (visited[course] !== -1)
            return visited[course]

         visited[course] = 1;

         for (const prereq of prereqs.get(course))
            if (dfs(prereq))
               return true

         visited[course] = 0;
         schedule.push(course);

         return false
      };

      for (let course of prereqs.keys()) {
         if (dfs(course)) {
            return []
         }
      }
      return schedule
   };
}


const findOrder = new Solution().findOrder;
console.log(new Solution().findOrder(2, [[1, 0]]).toString() === [0, 1].toString())
console.log(new Solution().findOrder(4, [[1, 0], [2, 0], [3, 1], [3, 2]]).toString() === [0, 1, 2, 3].toString())
console.log(new Solution().findOrder(1, []).toString() === [0].toString())
console.log(new Solution().findOrder(2, [[0, 1], [1, 0]]).toString() === [].toString())
