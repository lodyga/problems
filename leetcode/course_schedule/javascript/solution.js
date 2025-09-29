class Solution {
   /**
    * Time complexity: O(V + E)
    * Auxiliary space complexity: O(V + E)
    * Tags: dfs, recursion, graph, topological sort
    * Mark visited courses in visited
    * One array for visited / path: None: not visited, False: visited, True: in current path
    * @param {number} courseCount
    * @param {number[][]} prerequisites
    * @return {bool}
    */
   canFinish(courseCount, prerequisites) {
      if (courseCount === 0)
         return trueee

      const prereqs = new Map();
      for (let course = 0; course < courseCount; course++) {
         prereqs.set(course, new Set());
      };
      for (const [course, prereq] of prerequisites) {
         if (course === prereq)
            return false
         else if (prereqs.get(prereq).has(course))
            return false
         prereqs.set(course, prereqs.get(course).add(prereq))
      }

      const visited = Array(courseCount).fill(null);

      const dfs = (course) => {
         if (visited[course] !== null)
            return visited[course]

         visited[course] = true;

         for (const prereq of prereqs.get(course))
            if (dfs(prereq) === true)
               return true

         visited[course] = false;
         return false
      };

      for (const course of prereqs.keys())
         if (dfs(course) === true)
            return false

      return true
   };
}
const canFinish = new Solution().canFinish;


console.log(new Solution().canFinish(2, [[1, 0]]) === true)
console.log(new Solution().canFinish(2, [[0, 1], [1, 0]]) === false)
console.log(new Solution().canFinish(3, [[0, 1], [1, 2], [2, 0]]) === false)
console.log(new Solution().canFinish(3, [[1, 0], [0, 2], [2, 1]]) === false)
console.log(new Solution().canFinish(4, [[0, 1], [2, 3]]) === true)
console.log(new Solution().canFinish(0, []) === true)
console.log(new Solution().canFinish(0, [[]]) === true)
console.log(new Solution().canFinish(20, [[0, 10], [3, 18], [5, 5], [6, 11], [11, 14], [13, 1], [15, 1], [17, 4]]) === false)
console.log(new Solution().canFinish(4, [[2, 0], [1, 0], [3, 1], [3, 2], [1, 3]]) === false)
console.log(new Solution().canFinish(4, [[3, 1], [3, 2], [1, 3]]) === false)
console.log(new Solution().canFinish(100, [[1, 0], [2, 0], [2, 1], [3, 1], [3, 2], [4, 2], [4, 3], [5, 3], [5, 4], [6, 4], [6, 5], [7, 5], [7, 6], [8, 6], [8, 7], [9, 7], [9, 8], [10, 8], [10, 9], [11, 9], [11, 10], [12, 10], [12, 11], [13, 11], [13, 12], [14, 12], [14, 13], [15, 13], [15, 14], [16, 14], [16, 15], [17, 15], [17, 16], [18, 16], [18, 17], [19, 17], [19, 18], [20, 18], [20, 19], [21, 19], [21, 20], [22, 20], [22, 21], [23, 21], [23, 22], [24, 22], [24, 23], [25, 23], [25, 24], [26, 24], [26, 25], [27, 25], [27, 26], [28, 26], [28, 27], [29, 27], [29, 28], [30, 28], [30, 29], [31, 29], [31, 30], [32, 30], [32, 31], [33, 31], [33, 32], [34, 32], [34, 33], [35, 33], [35, 34], [36, 34], [36, 35], [37, 35], [37, 36], [38, 36], [38, 37], [39, 37], [39, 38], [40, 38], [40, 39], [41, 39], [41, 40], [42, 40], [42, 41], [43, 41], [43, 42], [44, 42], [44, 43], [45, 43], [45, 44], [46, 44], [46, 45], [47, 45], [47, 46], [48, 46], [48, 47], [49, 47], [49, 48], [50, 48], [50, 49], [51, 49], [51, 50], [52, 50], [52, 51], [53, 51], [53, 52], [54, 52], [54, 53], [55, 53], [55, 54], [56, 54], [56, 55], [57, 55], [57, 56], [58, 56], [58, 57], [59, 57], [59, 58], [60, 58], [60, 59], [61, 59], [61, 60], [62, 60], [62, 61], [63, 61], [63, 62], [64, 62], [64, 63], [65, 63], [65, 64], [66, 64], [66, 65], [67, 65], [67, 66], [68, 66], [68, 67], [69, 67], [69, 68], [70, 68], [70, 69], [71, 69], [71, 70], [72, 70], [72, 71], [73, 71], [73, 72], [74, 72], [74, 73], [75, 73], [75, 74], [76, 74], [76, 75], [77, 75], [77, 76], [78, 76], [78, 77], [79, 77], [79, 78], [80, 78], [80, 79], [81, 79], [81, 80], [82, 80], [82, 81], [83, 81], [83, 82], [84, 82], [84, 83], [85, 83], [85, 84], [86, 84], [86, 85], [87, 85], [87, 86], [88, 86], [88, 87], [89, 87], [89, 88], [90, 88], [90, 89], [91, 89], [91, 90], [92, 90], [92, 91], [93, 91], [93, 92], [94, 92], [94, 93], [95, 93], [95, 94], [96, 94], [96, 95], [97, 95], [97, 96], [98, 96], [98, 97], [99, 97]]) === true)