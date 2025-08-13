class Solution {
   /**
    * Time complexity: O(n2)
    * Auxiliary space complexity: O(n2)
    * Tags: dp, top-dwon
    * @param {number[][]} grid
    * @return {number}
    */
   minPathSum(grid) {
      const rows = grid.length;
      const cols = grid[0].length;
      const memo = Array.from({ length: rows }, () => Array(cols).fill(null));
      memo[rows - 1][cols - 1] = grid[rows - 1][cols - 1];

      const dfs = (row, col) => {
         if (
            row == rows ||
            col == cols
         ) {
            return 40000
         } else if (memo[row][col] !== null) {
            return memo[row][col]
         }

         memo[row][col] = grid[row][col] +
            Math.min(dfs(row + 1, col), dfs(row, col + 1))

         return memo[row][col]
      }
      return dfs(0, 0)
   };
}


class Solution {
   /**
    * Time complexity: O(n2)
    * Auxiliary space complexity: O(n)
    * Tags: dp, bottom-up
    * @param {number[][]} grid
    * @return {number}
    */
   minPathSum(grid) {
      const rows = grid.length;
      const cols = grid[0].length;
      const cache = Array(cols).fill(40000)
      cache[cols - 1] = 0;

      for (let row = rows - 1; row >= 0; row--) {
         for (let col = cols - 1; col >= 0; col--) {
            if (col === cols - 1) {
               cache[col] += grid[row][col]
            } else {
               cache[col] = grid[row][col] + Math.min(cache[col], cache[col + 1]);
            }
         }
      }
      return cache[0]
   };
}
const minPathSum = new Solution().minPathSum;


console.log(new Solution().minPathSum([[1, 2], [3, 4]]), 7)
console.log(new Solution().minPathSum([[1, 3, 1], [1, 5, 1], [4, 2, 1]]), 7)
console.log(new Solution().minPathSum([[1, 2, 3], [4, 5, 6]]), 12)