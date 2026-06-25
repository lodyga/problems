class Solution {
   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(n)
    * Tags: dp, top-down with memoization as array
    * @param {number[][]} questions
    * @return {number}
    */
   mostPoints(questions) {
      const N = questions.length;
      const memo = Array(N).fill(-1);

      const dfs = (idx) => {
         if (idx >= N) {
            return 0;
         } else if (memo[idx] !== -1) {
            return memo[idx];
         }

         const [points, brainpower] = questions[idx];
         const skip = dfs(idx + 1);
         const solve = points + dfs(idx + 1 + brainpower);
         memo[idx] = Math.max(skip, solve);

         return memo[idx];
      }

      return dfs(0);
   }
}


class Solution {
   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(n)
    * Tags:
    *     DS: array
    *     A: bottom-up
    * @param {number[][]} questions
    * @return {number}
    */
   mostPoints(questions) {
      const N = questions.length;
      const cache = Array(N + 1).fill(0);

      for (let idx = N - 1; idx > -1; idx--) {
         const [points, brainpower] = questions[idx];
         const nextIdx = idx + 1 + brainpower;
         const skip = cache[idx + 1];
         const solve = points + (nextIdx < N ? cache[nextIdx] : 0);
         cache[idx] = Math.max(skip, solve);
      }

      return cache[0];
   }
}


const mostPoints = new Solution().mostPoints;
console.log(new Solution().mostPoints([[3, 2], [4, 3], [4, 4], [2, 5]]) === 5)
console.log(new Solution().mostPoints([[1, 1], [2, 2], [3, 3], [4, 4], [5, 5]]) === 7)
console.log(new Solution().mostPoints([[72, 5], [36, 5], [95, 5], [50, 1], [62, 1], [14, 3], [72, 5], [86, 2], [43, 3], [51, 3], [14, 1], [91, 5], [47, 4], [72, 4], [63, 5], [40, 3], [68, 1], [8, 3], [84, 5], [7, 5], [40, 1], [35, 3], [66, 2], [39, 5], [40, 1], [92, 3], [67, 5], [34, 3], [84, 4], [75, 5], [6, 1], [71, 3], [77, 3], [25, 3], [53, 3], [32, 3], [88, 5], [18, 2], [21, 3], [78, 2], [69, 5], [45, 4], [94, 2], [70, 1], [85, 2], [7, 2], [68, 4], [71, 4], [57, 2], [12, 5], [53, 5], [51, 3], [46, 1], [28, 3]]) === 845)
