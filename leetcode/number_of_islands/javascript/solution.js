class Solution {
   /**
    * Time complexity: O(n2)
    * Auxiliary space complexity: O(n2)
    * Tags: dfs, recursion, graph, matrix
    * @param {string[][]} grid
    * @return {number}
    */
   numIslands(grid) {
      const rows = grid.length;
      const cols = grid[0].length;
      const visitedCells = new Set();
      let islandCounter = 0;
      const DIRECTIONS = [[-1, 0], [1, 0], [0, -1], [0, 1]];

      for (let row = 0; row < rows; row++) {
         for (let col = 0; col < cols; col++) {
            islandCounter += dfs(row, col)
         }
      }
      return islandCounter

      function dfs(row, col) {
         if (
            row < 0 ||
            col < 0 ||
            row === rows ||
            col === cols ||
            grid[row][col] === '0' ||
            visitedCells.has(`${row},${col}`)
         ) return 0
         
         visitedCells.add(`${row},${col}`)
         DIRECTIONS.map(([r, c]) => dfs(row + r, col + c));
         return 1
      }
   };
}


console.log(new Solution().numIslands([['0']]) === 0)
console.log(new Solution().numIslands([['1']]) === 1)
console.log(new Solution().numIslands([['0', '0'], ['0', '1']]) === 1)
console.log(new Solution().numIslands([['1', '0'], ['0', '1']]) === 2)
console.log(new Solution().numIslands([['1', '0', '0'], ['0', '1', '0'], ['0', '0', '1']]) === 3)
console.log(new Solution().numIslands([['1', '1', '0'], ['0', '1', '0'], ['0', '0', '1']]) === 2)
console.log(new Solution().numIslands([['1', '1', '1', '1', '0'], ['1', '1', '0', '1', '0'], ['1', '1', '0', '0', '0'], ['0', '0', '0', '0', '0']]) === 1)
console.log(new Solution().numIslands([['1', '1', '0', '0', '0'], ['1', '1', '0', '0', '0'], ['0', '0', '1', '0', '0'], ['0', '0', '0', '1', '1']]) === 3)