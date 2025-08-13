class Solution {
   /**
    * Time complexity: O(n2)
    * Auxiliary space complexity: O(n)
    * Tags: dp, bottom-up
    * @param {number[][]} obstacleGrid
    * @return {number}
    */
   uniquePathsWithObstacles(obstacleGrid) {
      const rows = obstacleGrid.length;
      const cols = obstacleGrid[0].length;

      const cache = Array(cols).fill(0);
      cache[cache.length - 1] = 1;

      for (let row = rows - 1; row >= 0; row--) {
         for (let col = cols - 1; col >= 0; col--) {
            if (obstacleGrid[row][col]) {
               cache[col] = 0;
            } else {
               if (col !== cols - 1) {
                  cache[col] += cache[col + 1]
               } 
            }
         }
      }
      return cache[0]
   };
}
const uniquePathsWithObstacles = new Solution().uniquePathsWithObstacles;


class Solution {
   /**
    * Time complexity: O(n2)
    * Auxiliary space complexity: O(n2)
    * Tags: dp, top-down
    * @param {number[][]} obstacleGrid
    * @return {number}
    */
   uniquePathsWithObstacles(obstacleGrid) {
      const rows = obstacleGrid.length;
      const cols = obstacleGrid[0].length;
      const memo = Array.from({ length: rows }, () => Array(cols).fill(null));
      memo[rows - 1][cols - 1] = 1;

      const dfs = (row, col) => {
         if (
            row == rows ||
            col == cols ||
            obstacleGrid[row][col]
         ) {
            return 0
         }
         else if (memo[row][col] != null) {
            return memo[row][col]
         } else {
            memo[row][col] = dfs(row + 1, col) + dfs(row, col + 1)
            return memo[row][col]
         }
      }
      return dfs(0, 0)
   };
}
const uniquePathsWithObstacles = new Solution().uniquePathsWithObstacles;


console.log(new Solution().uniquePathsWithObstacles([[0, 0, 0], [0, 1, 0], [0, 0, 0]]), 2)
console.log(new Solution().uniquePathsWithObstacles([[0, 1], [0, 0]]), 1)
console.log(new Solution().uniquePathsWithObstacles([[0, 0], [0, 1]]), 0)
console.log(new Solution().uniquePathsWithObstacles([[0, 0, 0], [0, 0, 0], [0, 1, 0]]), 3)
console.log(new Solution().uniquePathsWithObstacles([[0, 0, 0], [0, 0, 1], [0, 0, 0]]), 3)