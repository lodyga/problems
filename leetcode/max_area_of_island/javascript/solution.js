class Solution {
   /**
    * Time complexity: O(n2)
    * Auxiliary space complexity: O(n2)
    * Tags: dfs, recursion, matrix, graph
    * @param {number[][]} grid
    * @return {number}
    */
   maxAreaOfIsland(grid) {
      const rows = grid.length;
      const cols = grid[0].length;
      const visitedCells = new Set();
      let maxArea = 0;
      const directions = [[-1, 0], [1, 0], [0, -1], [0, 1]];


      for (let row = 0; row < rows; row++) {
         for (let col = 0; col < cols; col++) {
            maxArea = Math.max(maxArea, dfs(row, col));
         }
      }

      return maxArea

      function dfs(row, col) {
         if (
            row < 0 ||
            col < 0 ||
            row === rows ||
            col === cols ||
            grid[row][col] === 0 ||
            visitedCells.has(`${row},${col}`)
         ) return 0

         visitedCells.add(`${row},${col}`);

         return (
            1 +
            directions
               .map(([r, c]) => dfs(row + r, col + c))
               .reduce((total, value) => total + value, 0)
         )
      }
   };
}


console.log(new Solution().maxAreaOfIsland([[0]]) === 0)
console.log(new Solution().maxAreaOfIsland([[1]]) === 1)
console.log(new Solution().maxAreaOfIsland([[0, 0], [0, 1]]) === 1)
console.log(new Solution().maxAreaOfIsland([[1, 0], [0, 1]]) === 1)
console.log(new Solution().maxAreaOfIsland([[1, 0, 0], [0, 1, 0], [0, 0, 1]]) === 1)
console.log(new Solution().maxAreaOfIsland([[1, 1, 0], [0, 1, 0], [0, 0, 1]]) === 3)
console.log(new Solution().maxAreaOfIsland([[0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0], [0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0], [0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0], [0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0], [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0]]) === 6)
console.log(new Solution().maxAreaOfIsland([[0, 0, 0, 0, 0, 0, 0, 0]]) === 0)