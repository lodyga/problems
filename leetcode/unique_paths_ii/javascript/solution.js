class Solution {
   /**
    * Time complexity: O(n2)
    * Auxiliary space complexity: O(n2)
    * Tags:
    *     DS: array (matrix)
    *     A: top-down
    * @param {number[][]} obstacleGrid
    * @return {number}
    */
   uniquePathsWithObstacles(obstacleGrid) {
      const ROWS = obstacleGrid.length;
      const COLS = obstacleGrid[0].length;
      // if exit or entrance is blocked
      if (
         obstacleGrid[ROWS - 1][COLS - 1] ||
         obstacleGrid[0][0]
      )
         return 0
      const memo = Array.from({ length: ROWS }, () => Array(COLS).fill(-1));
      memo[ROWS - 1][COLS - 1] = 1;

      const dfs = (row, col) => {
         if (
            row == ROWS ||
            col == COLS ||
            obstacleGrid[row][col]
         ) {
            return 0
         }
         else if (memo[row][col] !== -1) {
            return memo[row][col]
         }

         const right = dfs(row, col + 1);
         const down = dfs(row + 1, col);
         memo[row][col] = right + down;
         return memo[row][col]
      }
      return dfs(0, 0)
   };

   /**
    * Time complexity: O(n2)
    * Auxiliary space complexity: O(n2)
    * Tags:
    *     DS: array (matrix)
    *     A: bottom-up
    * @param {number[][]} obstacleGrid
    * @return {number}
    */
   uniquePathsWithObstacles(obstacleGrid) {
      const ROWS = obstacleGrid.length;
      const COLS = obstacleGrid[0].length;
      // if exit or entrance is blocked
      if (
         obstacleGrid[ROWS - 1][COLS - 1] ||
         obstacleGrid[0][0]
      )
         return 0
      const cache = Array.from({ length: ROWS + 1 }, () => Array(COLS + 1).fill(0));
      cache[ROWS][COLS - 1] = 1;

      for (let row = ROWS - 1; row > -1; row--) {
         for (let col = COLS - 1; col > -1; col--) {
            if (obstacleGrid[row][col])
               continue;
            const right = cache[row][col + 1];
            const down = cache[row + 1][col];
            cache[row][col] = right + down;
         }
      }
      return cache[0][0]
   };

   /**
    * Time complexity: O(n2)
    * Auxiliary space complexity: O(n)
    * Tags:
    *     DS: array (matrix)
    *     A: bottom-up
    * @param {number[][]} obstacleGrid
    * @return {number}
    */
   uniquePathsWithObstacles(obstacleGrid) {
      const ROWS = obstacleGrid.length;
      const COLS = obstacleGrid[0].length;
      // if exit or entrance is blocked
      if (
         obstacleGrid[ROWS - 1][COLS - 1] ||
         obstacleGrid[0][0]
      )
         return 0
      let nextCache = Array(COLS + 1).fill(0);
      nextCache[COLS - 1] = 1;

      for (let row = ROWS - 1; row > -1; row--) {
         const cache = Array(COLS + 1).fill(0);
         for (let col = COLS - 1; col > -1; col--) {
            if (obstacleGrid[row][col])
               continue;

            const right = cache[col + 1];
            const down = nextCache[col];
            cache[col] = right + down;
         }
         nextCache = cache;
      }
      return nextCache[0]
   };
}


const uniquePathsWithObstacles = new Solution().uniquePathsWithObstacles;
console.log(new Solution().uniquePathsWithObstacles([[0, 0, 0], [0, 1, 0], [0, 0, 0]]) === 2)
console.log(new Solution().uniquePathsWithObstacles([[0, 1], [0, 0]]) === 1)
console.log(new Solution().uniquePathsWithObstacles([[0, 0], [0, 1]]) === 0)
console.log(new Solution().uniquePathsWithObstacles([[0, 0, 0], [0, 0, 0], [0, 1, 0]]) === 3)
console.log(new Solution().uniquePathsWithObstacles([[0, 0, 0], [0, 0, 1], [0, 0, 0]]) === 3)
