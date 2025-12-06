class Solution {
   /**
    * Time complexity: O(n2)
    * Auxiliary space complexity: O(n2)
    * Tags:
    *     DS: array
    *     A: top-down 
    * @param {number} rows
    * @param {number} cols
    * @return {number}
    */
   uniquePaths(rows, cols) {
      const memo = Array.from({ length: rows }, () => Array(cols).fill(-1));
      memo[rows - 1][cols - 1] = 1;

      const dfs = (row, col) => {
         if (row === rows || col === cols) {
            return 0
         } else if (memo[row][col] !== - 1) {
            return memo[row][col]
         }
         memo[row][col] = dfs(row + 1, col) + dfs(row, col + 1);
         return memo[row][col]
      }
      return dfs(0, 0)
   };

   /**
    * Time complexity: O(n2)
    * Auxiliary space complexity: O(n)
    * Tags:
    *     DS: array
    *     A: bottom-up
    * @param {number} rows
    * @param {number} cols
    * @return {number}
    */
   uniquePaths(rows, cols) {
      const cache = Array(cols + 1).fill(1);
      cache[cache.length - 1] = 0;

      for (let row = rows - 2; row > -1; row--) {
         for (let col = cols - 1; col > -1; col--) {
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
