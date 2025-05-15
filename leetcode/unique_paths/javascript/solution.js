class Solution {
   /**
    * Time complexity: O(m*n)
    *     m: number of rows
    *     n: number of coulmns
    * Auxiliary space complexity: O(n)
    * Tags: dp, bottom-up
    * @param {number} rows
    * @param {number} cols
    * @return {number}
    */
   uniquePaths(rows, cols) {
      const currentRow = Array(cols).fill(1);  // cache

      for (let row = 0; row < rows - 1; row++) {
         for (let col = cols - 2; col >= 0; col--) {
            currentRow[col] = currentRow[col + 1] + currentRow[col];
         }
      }
      return currentRow[0]
   };
}


class Solution {
   /**
    * Time complexity: O(m*n)
    *     m: number of rows
    *     n: number of coulmns
    * Auxiliary space complexity: O(m*n)
    * Tags: dp, top-down with memoization as list
    * @param {number} rows
    * @param {number} cols
    * @return {number}
    */
   uniquePaths(rows, cols) {
      const memo = Array.from({ length: rows }, () => Array(cols).fill(1));

      function dfs(row, col) {
         if (row === rows - 1 || col === cols - 1) {
         } else {
            memo[row][col] = dfs(row + 1, col) + dfs(row, col + 1);
         }
         return memo[row][col]
      }
      return dfs(0, 0)
   };
}


console.log(new Solution().uniquePaths(1, 2), 1)
console.log(new Solution().uniquePaths(2, 3), 3)
console.log(new Solution().uniquePaths(3, 2), 3)
console.log(new Solution().uniquePaths(3, 7), 28)