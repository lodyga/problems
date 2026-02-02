class Solution {
   /**
    * Time complexity: O(V*(V + E) + q)
    *     q: queries len
    * Auxiliary space complexity: O(V + E + q)
    * Tags:
    *     DS: array
    *     A: DFS with memoization (DP on DAG)
    *     Model: graph
    * @param {number} numCourses
    * @param {number[][]} prerequisites
    * @param {number[][]} queries
    * @return {boolean[]}
    */
   checkIfPrerequisite(numCourses, prerequisites, queries) {
      const prereqCourses = Array.from({ length: numCourses }, () => new Set());
      for (const [prereqCourse, course] of prerequisites) {
         prereqCourses[course].add(prereqCourse)
      }

      // {course: set(indeirect preqs list)}
      // const memo = Array.from({ length: numCourses }, () => new Set());
      const memo = Array(numCourses);

      const dfs = (course) => {
         if (memo[course] !== undefined)
            return memo[course]

         memo[course] = new Set();

         for (const prereqCourse of prereqCourses[course]) {
            memo[course].add(prereqCourse);
            memo[course] = new Set([...memo[course], ...dfs(prereqCourse)]);
         }
         return memo[course]
      }

      for (let course = 0; course < numCourses; course++) {
         dfs(course);
      }

      const res = [];
      for (const [prereq, course] of queries) {
         res.push(memo[course].has(prereq));
      }
      return res
   };

   /**
    * Time complexity: O((V + E) * q)
    *     q: queries len
    * Auxiliary space complexity: O(V + E + q)
    * Tags:
    *     DS: hash map, hash set
    *     A: DFS
    *     Model: graph
    * @param {number} numCourses
    * @param {number[][]} prerequisites
    * @param {number[][]} queries
    * @return {boolean[]}
    */
   checkIfPrerequisite(numCourses, prerequisites, queries) {
      const prereqs = new Map();
      for (let course = 0; course < numCourses; course++) {
         prereqs.set(course, new Set())
      }
      for (const [prereq, course] of prerequisites) {
         prereqs.set(course, prereqs.get(course).add(prereq));
      }

      const dfs = (course, target) => {
         if (prereqs.get(course).length === 0) {
            return false
         } else if (prereqs.get(course).has(target)) {
            return true
         }

         for (const prereq of prereqs.get(course))
            if (dfs(prereq, target))
               return true

         return false
      }

      const response = [];
      for (const [prereq, course] of queries) {
         response.push(dfs(course, prereq));
      }
      return response
   };
}


const checkIfPrerequisite = new Solution().checkIfPrerequisite;
console.log(new Solution().checkIfPrerequisite(2, [[1, 0]], [[0, 1], [1, 0]]).toString() === [false, true].toString())
console.log(new Solution().checkIfPrerequisite(2, [], [[1, 0], [0, 1]]).toString() === [false, false].toString())
console.log(new Solution().checkIfPrerequisite(3, [[1, 2], [1, 0], [2, 0]], [[1, 0], [1, 2]]).toString() === [true, true].toString())
console.log(new Solution().checkIfPrerequisite(6, [[0, 1], [1, 2], [2, 4], [3, 2], [5, 3]], [[0, 3], [1, 4], [1, 3], [2, 3], [3, 2], [5, 4]]).toString() === [false, true, false, false, true, true].toString())
