class Solution {
   /**
    * Time complexity: O(V + E)
    * Auxiliary space complexity: O(V + E)
    * Tags: dfs, recursion, graph, topological sort
    * @param {number} courseCount
    * @param {number[][]} prerequisites
    * @return {number[][]}
    */
   findOrder(courseCount, prerequisites) {
      if (courseCount === 0)
         return []
      
      const prereqs = new Map();
      for (let course = 0; course < courseCount; course++) {
         prereqs.set(course, new Set());
      }
      for (const [course, prereq] of prerequisites) {
         if (course === prereq)
            return []
         else if (prereqs.get(prereq).has(course))
            return []
         prereqs.set(course, prereqs.get(course).add(prereq));
      }

      const visited = Array(courseCount).fill(null);
      const schedule = [];

      const dfs = (course) => {
         if (visited[course] !== null)
            return visited[course]

         visited[course] = true;

         for (const prereq of prereqs.get(course))
            if (dfs(prereq) === true)
               return true
         
         schedule.push(course);
         visited[course] = false;

         return false
      };

      for (let course = 0; course < courseCount; course++) {
         if (dfs(course) === true)
            return []
      }
      return schedule
   };
}
const findOrder = new Solution().findOrder;


console.log(new Solution().findOrder(2, [[1, 0]]), [0, 1])
console.log(new Solution().findOrder(4, [[1, 0], [2, 0], [3, 1], [3, 2]]), [0, 1, 2, 3])
console.log(new Solution().findOrder(1, []), [0])
console.log(new Solution().findOrder(2, [[0, 1], [1, 0]]), [])