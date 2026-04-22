class Solution {
   /**
    * Time complexity: O(n2)
    * Auxiliary space complexity: O(n2)
    * Tags:
    *     DS: array
    *     A: top-down 
    * @param {number} ROWS
    * @param {number} COLS
    * @return {number}
    */
   uniquePaths(ROWS, COLS) {
      const memo = Array.from({ length: ROWS }, () => Array(COLS).fill(-1));
      memo[ROWS - 1][COLS - 1] = 1;

      const dfs = (row, col) => {
         if (row === ROWS || col === COLS) {
            return 0
         } else if (memo[row][col] !== - 1) {
            return memo[row][col]
         }

         res = dfs(row + 1, col) + dfs(row, col + 1);
         memo[row][col] = res
         return res
      }
      return dfs(0, 0)
   };

   /**
    * Time complexity: O(n2)
    * Auxiliary space complexity: O(n)
    * Tags:
    *     DS: array
    *     A: bottom-up
    * @param {number} ROWS
    * @param {number} COLS
    * @return {number}
    */
   uniquePaths(ROWS, COLS) {
      const cache = Array(COLS + 1).fill(1);
      cache[cache.length - 1] = 0;

      for (let row = ROWS - 2; row > -1; row--) {
         for (let col = COLS - 1; col > -1; col--) {
            cache[col] += cache[col + 1];
         }
      }
      
      return cache[0]
   };
}


const uniquePaths = new Solution().uniquePaths;
console.log(new Solution().uniquePaths(2, 1) === 1)
console.log(new Solution().uniquePaths(1, 2) === 1)
console.log(new Solution().uniquePaths(2, 2) === 2)
console.log(new Solution().uniquePaths(2, 3) === 3)
console.log(new Solution().uniquePaths(3, 2) === 3)
console.log(new Solution().uniquePaths(3, 7) === 28)
console.log(new Solution().uniquePaths(23, 12) === 193536720)
