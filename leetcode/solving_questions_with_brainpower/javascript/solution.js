class Solution {
   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(n)
    * Tags: dp, top-down with memoization as array
    * @param {number[][]} questions
    * @return {number}
    */
   mostPoints(questions) {
      const memo = Array(questions.length).fill(-1);

      const dfs = (index) => {
         if (index >= questions.length) {
            return 0
         } else if (memo[index] !== -1) {
            return memo[index]
         }

         const points = questions[index][0];
         const cooldown = questions[index][1];
         const skip = dfs(index + 1);
         const solve = points + dfs(index + 1 + cooldown);
         memo[index] = Math.max(skip, solve);
         return memo[index]
      }
      return dfs(0)
   };


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
      const cache = Array(questions.length).fill(0);

      for (let index = questions.length - 1; index > -1; index--) {
         const points = questions[index][0];
         const cooldown = questions[index][1];
         const nextIndex = index + 1 + cooldown;
         const skip = index + 1 < questions.length ? cache[index + 1] : 0;
         const solve = points + (nextIndex < questions.length ? cache[nextIndex] : 0);
         cache[index] = Math.max(skip, solve);
      }
      return cache[0]
   };
}


const mostPoints = new Solution().mostPoints;
console.log(new Solution().mostPoints([[3, 2], [4, 3], [4, 4], [2, 5]]) === 5)
console.log(new Solution().mostPoints([[1, 1], [2, 2], [3, 3], [4, 4], [5, 5]]) === 7)
console.log(new Solution().mostPoints([[72, 5], [36, 5], [95, 5], [50, 1], [62, 1], [14, 3], [72, 5], [86, 2], [43, 3], [51, 3], [14, 1], [91, 5], [47, 4], [72, 4], [63, 5], [40, 3], [68, 1], [8, 3], [84, 5], [7, 5], [40, 1], [35, 3], [66, 2], [39, 5], [40, 1], [92, 3], [67, 5], [34, 3], [84, 4], [75, 5], [6, 1], [71, 3], [77, 3], [25, 3], [53, 3], [32, 3], [88, 5], [18, 2], [21, 3], [78, 2], [69, 5], [45, 4], [94, 2], [70, 1], [85, 2], [7, 2], [68, 4], [71, 4], [57, 2], [12, 5], [53, 5], [51, 3], [46, 1], [28, 3]]) === 845)
