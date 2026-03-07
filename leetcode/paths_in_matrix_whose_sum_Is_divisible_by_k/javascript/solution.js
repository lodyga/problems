class Solution {
   /**
    * Time complexity: O(n3)
    *     O(n*m*k)
    * Auxiliary space complexity: O(n3)
    *     O(n*m*k)
    * Tags:
    *     DS: array (matrix)
    *     A: top-down
    * @param {number[][]} grid
    * @param {number} k
    * @return {number}
    */
   numberOfPaths(grid, k) {
      const MOD = 1e9 + 7;
      const [ROWS, COLS] = [grid.length, grid[0].length];
      // memo[row][col][r]: Number of ways to reach bottom-right with remainder at this cell.
      const memo = Array.from({ length: ROWS }, () =>
         Array.from({ length: COLS }, () =>
            Array(k).fill(-1)));

      const dfs = (row, col, rum) => {
         if (row == ROWS || col == COLS) {
            return 0
         }

         const cell = grid[row][col];
         rum = (rum + cell) % k;

         if (row === ROWS - 1 && col === COLS - 1) {
            return rum % k == 0 ? 1 : 0
         } else if (memo[row][col][rum] !== -1) {
            return memo[row][col][rum]
         }

         const right = dfs(row, col + 1, rum);
         const down = dfs(row + 1, col, rum);
         const res = (down + right) % MOD;
         memo[row][col][rum] = res;
         return res
      }

      return dfs(0, 0, 0)
   };
}


const numberOfPaths = new Solution().numberOfPaths;
console.log(new Solution().numberOfPaths([[5, 2, 4], [3, 0, 5], [0, 7, 2]], 3) === 2)
console.log(new Solution().numberOfPaths([[0, 0]], 5) === 1)
console.log(new Solution().numberOfPaths([[0]], 1) === 1)
console.log(new Solution().numberOfPaths([[7, 3, 4, 9], [2, 3, 6, 2], [2, 3, 7, 0]], 1) === 10)
