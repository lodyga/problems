class Solution {
   /**
    * Time complexity: O(n2)
    * Auxiliary space complexity: O(n2)
    * Tags:
    *     DS: array (matrix)
    *     A: dfs, recursion
    * @param {number[][]} grid
    * @return {}
    */
   numEnclaves(grid) {
      const ROWS = grid.length;
      const COLS = grid[0].length;
      const DIRECTIONS = [[-1, 0], [1, 0], [0, -1], [0, 1]];
      const visited = grid.slice();

      const dfs = (row, col) => {
         if (
            row === -1 || row === ROWS ||
            col === -1 || col === COLS ||
            visited[row][col] === 0
         ) return

         visited[row][col] = 0

         for (const [dr, dc] of DIRECTIONS) {
            const [r, c] = [row + dr, col + dc];
            dfs(r, c)
         }
      }

      for (let row = 0; row < ROWS; row++) {
         for (let col = 0; col < COLS; col++) {
            if ((
               row === 0 || row === ROWS - 1 ||
               col === 0 || col === COLS - 1
            ) &&
               visited[row][col] === 1
            ) dfs(row, col)
         }
      }

      return visited
         .map(row => row.reduce((sum, val) => sum + val, 0))
         .reduce((sum, val) => sum + val, 0);
   };
}


const numEnclaves = new Solution().numEnclaves;
console.log(new Solution().numEnclaves([[0, 0, 0, 0], [1, 0, 1, 0], [0, 1, 1, 0], [0, 0, 0, 0]]) === 3)
console.log(new Solution().numEnclaves([[0, 1, 1, 0], [0, 0, 1, 0], [0, 0, 1, 0], [0, 0, 0, 0]]) === 0)
console.log(new Solution().numEnclaves([[0, 0, 0, 1, 1, 1, 0, 1, 0, 0], [1, 1, 0, 0, 0, 1, 0, 1, 1, 1], [0, 0, 0, 1, 1, 1, 0, 1, 0, 0], [0, 1, 1, 0, 0, 0, 1, 0, 1, 0], [0, 1, 1, 1, 1, 1, 0, 0, 1, 0], [0, 0, 1, 0, 1, 1, 1, 1, 0, 1], [0, 1, 1, 0, 0, 0, 1, 1, 1, 1], [0, 0, 1, 0, 0, 1, 0, 1, 0, 1], [1, 0, 1, 0, 1, 1, 0, 0, 0, 0], [0, 0, 0, 0, 1, 1, 0, 0, 0, 1]]) === 3)
