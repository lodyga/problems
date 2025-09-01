class Solution {
   /**
    * Time complexity: O(n2)
    * Auxiliary space complexity: O(n2)
    * Tags: dfs, matrix, graph, pure functional 
    * @param {number[][]} grid
    * @return {number}
    */
   islandPerimeter(grid) {
      function getPerimeter(row, col) {
         if (
            row < 0 ||
            col < 0 ||
            row === rows ||
            col === cols ||
            grid[row][col] === 0
         ) {
            return 1
         }
         else if (visitedCells.has(`${row},${col}`)) {
            return 0
         }

         visitedCells.add(`${row},${col}`)

         let perimeter = 0;
         for (const [r, c] of DIRECTIONS) {
            perimeter += getPerimeter(row + r, col + c)
         }
         return perimeter
      }

      const rows = grid.length;
      const cols = grid[0].length;
      const visitedCells = new Set();
      const DIRECTIONS = [[-1, 0], [1, 0], [0, -1], [0, 1]];

      for (let row = 0; row < rows; row++) {
         for (let col = 0; col < cols; col++) {
            if (grid[row][col]) {
               return getPerimeter(row, col)
            }
         }
      }
   };
}
const islandPerimeter = new Solution().islandPerimeter;


class Solution {
   /**
    * Time complexity: O(n2)
    * Auxiliary space complexity: O(n2)
    * Tags: dfs, matrix, graph, outer variable
    * Imperative style with side effects
    * @param {number[][]} grid
    * @return {number}
    */
   islandPerimeter(grid) {
      function getPerimeter(row, col) {
         if (
            row < 0 ||
            col < 0 ||
            row === rows ||
            col === cols ||
            grid[row][col] === 0
         ) {
            perimeter++;
            return
         }
         else if (visitedCells.has(`${row},${col}`)) {
            return
         }

         visitedCells.add(`${row},${col}`)

         for (const [r, c] of DIRECTIONS) {
            getPerimeter(row + r, col + c)
         }
      }

      const rows = grid.length;
      const cols = grid[0].length;
      const visitedCells = new Set();
      const DIRECTIONS = [[-1, 0], [1, 0], [0, -1], [0, 1]];
      let perimeter = 0

      for (let row = 0; row < rows; row++) {
         for (let col = 0; col < cols; col++) {
            if (grid[row][col]) {
               getPerimeter(row, col)
               return perimeter
            }
         }
      }
   };
}
const islandPerimeter = new Solution().islandPerimeter;


console.log(new Solution().islandPerimeter([[1]]), 4)
console.log(new Solution().islandPerimeter([[1, 0]]), 4)
console.log(new Solution().islandPerimeter([[0, 1, 0, 0], [1, 1, 1, 0], [0, 1, 0, 0], [1, 1, 0, 0]]), 16)