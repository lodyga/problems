class Solution {
   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(n)
    * Tags:
    *     DS: array
    *     A: top-down
    * @param {number[]} stoneValue
    * @return {string}
    */
   stoneGameIII(stoneValue) {
      const LOWER_BOUND = -(10 ** 8);
      const memo = Array(stoneValue.length + 1).fill(-1);
      memo[stoneValue.length] = 0;

      const dfs = (start) => {
         if (memo[start] !== -1) {
            return memo[start]
         }

         let subpileSum = 0;
         let score = LOWER_BOUND;

         for (let index = start; index < Math.min(start + 3, stoneValue.length); index++) {
            subpileSum += stoneValue[index];
            const points = subpileSum - dfs(index + 1)
            score = Math.max(score, points);
         }
         memo[start] = score;
         return score
      }
      return dfs(0) === 0 ? 'Tie' : (dfs(0) > 0 ? 'Alice' : 'Bob')
   };
}


const stoneGameIII = new Solution().stoneGameIII;
console.log(new Solution().stoneGameIII([1, 2, 3, 7]) === 'Bob')
console.log(new Solution().stoneGameIII([1, 2, 3, -9]) === 'Alice')
console.log(new Solution().stoneGameIII([1, 2, 3, 6]) === 'Tie')
console.log(new Solution().stoneGameIII([-1, -2]) === 'Alice')
console.log(new Solution().stoneGameIII([-1, -2, -3]) === 'Tie')
console.log(new Solution().stoneGameIII([-13, 17, 7, -13, 6, -3, -15, 15, -3, 4, 6, -5, 16, 0, 12, -6, 8, 13, 15, -4, -11, -16, 15]) === 'Alice')
