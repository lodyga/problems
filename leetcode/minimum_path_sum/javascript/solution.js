class Solution {
   /**
    * Time complexity: O(n2)
    * Auxiliary space complexity: O(n2)
    * Tags:
    *     DS: array (matrix)
    *     A: top-dwon
    * @param {number[][]} grid
    * @return {number}
    */
   minPathSum(grid) {
      const dfs = (row, col) => {
         if (row === ROWS || col === COLS) {
            return INF;
         }
         else if (memo[row][col] !== -1) {
            return memo[row][col];
         }

         const cell = grid[row][col];
         const res = cell + Math.min(dfs(row + 1, col), dfs(row, col + 1));
         memo[row][col] = res;

         return res;
      };

      const INF = 1e7;
      const ROWS = grid.length;
      const COLS = grid[0].length;
      const memo = Array.from({ length: ROWS }, () => Array(COLS).fill(-1));
      memo[ROWS - 1][COLS - 1] = grid[ROWS - 1][COLS - 1];
      return dfs(0, 0);
   }
}


class Solution {
   /**
    * Time complexity: O(n2)
    * Auxiliary space complexity: O(n2)
    * Tags:
    *     DS: array (matrix)
    *     A: bottom-up
    * @param {number[][]} grid
    * @return {number}
    */
   minPathSum(grid) {
      const INF = 1e7;
      const ROWS = grid.length;
      const COLS = grid[0].length;
      const cache = Array.from(({ length: ROWS + 1 }), () => Array(COLS + 1).fill(INF));
      cache[ROWS][COLS - 1] = 0;

      for (let row = ROWS - 1; row > -1; row--) {
         for (let col = COLS - 1; col > -1; col--) {
            const cell = grid[row][col];
            const right = cache[row][col + 1];
            const down = cache[row + 1][col];
            cache[row][col] = cell + Math.min(right, down);
         }
      }

      return cache[0][0];
   }
}


class Solution {
   /**
    * Time complexity: O(n2)
    * Auxiliary space complexity: O(n)
    * Tags:
    *     DS: array (matrix)
    *     A: bottom-up
    * @param {number[][]} grid
    * @return {number}
    */
   minPathSum(grid) {
      const INF = 10e7;
      const ROWS = grid.length;
      const COLS = grid[0].length;
      let nextCache = Array(COLS + 1).fill(INF);
      nextCache[COLS - 1] = 0;

      for (let row = ROWS - 1; row > -1; row--) {
         const cache = Array(COLS + 1).fill(INF);

         for (let col = COLS - 1; col > -1; col--) {
            cache[col] = grid[row][col]
               + Math.min(
                  nextCache[col],
                  cache[col + 1]
               );
         }

         nextCache = cache;
      }

      return nextCache[0];
   }
}


const minPathSum = new Solution().minPathSum;
console.log(new Solution().minPathSum([[1, 2], [3, 4]]) === 7)
console.log(new Solution().minPathSum([[1, 3, 1], [1, 5, 1], [4, 2, 1]]) === 7)
console.log(new Solution().minPathSum([[1, 2, 3], [4, 5, 6]]) === 12)
